from typing import TypedDict

from bs4 import BeautifulSoup


class ParsedNews(TypedDict):
    article_url: str | None
    image_url: str | None
    description: str


def parse_news_snippet(raw_html: str) -> ParsedNews:
    soup = BeautifulSoup(raw_html, "html.parser")

    # 1. Extract link and image URLs
    a_tag = soup.find("a")
    img_tag = soup.find("img")

    article_url = a_tag.get("href") if a_tag else None
    image_url = img_tag.get("src") if img_tag else None

    # 2. Decompose (remove) the <a> tag and everything inside it
    if a_tag:
        a_tag.decompose()
    elif img_tag:
        img_tag.decompose()

    # 3. Everything remaining in the document is the description text
    description = soup.get_text(" ", strip=True)

    return {
        "article_url": article_url,
        "image_url": image_url,
        "description": description,
    }


def parse_single_news(entry):
    snippet = parse_news_snippet(entry.get("summary") or "")
    image = next(
        (
            enclosure.get("href")
            for enclosure in entry.get("enclosures", [])
            if enclosure.get("type", "").startswith("image/")
            and enclosure.get("href")
        ),
        None,
    )
    return {
        **entry,
        "image": image or snippet["image_url"] or "",
        "description": snippet["description"],
    }


def parse_news(entries):
    news = []
    for e in entries:
        news.append(parse_single_news(e))
    return news


__all__ = ["parse_news", "parse_news_snippet"]

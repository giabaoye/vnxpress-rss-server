def getXpressUrl(category=""):
    match category:
        case "thegioi":
            return "https://vnexpress.net/rss/the-gioi.rss"
        case "tinxemnhieu":
            return "https://vnexpress.net/rss/tin-xem-nhieu.rss"
        case "giaitri":
            return "https://vnexpress.net/rss/giai-tri.rss"
        case "giaoduc":
            return "https://vnexpress.net/rss/giao-duc.rss"
        case _:
            return "https://vnexpress.net/rss/thoi-su.rss"


def getTTUrl(category=""):
    match category:
        case "thoisu":
            return "https://tuoitre.vn/thoi-su.rss"
        case "thegioi":
            return "https://tuoitre.vn/the-gioi.rss"
        case "vanhoa":
            return "https://tuoitre.vn/van-hoa.rss"
        case "thethao":
            return "https://tuoitre.vn/the-thao.rss"
        case _:
            return "https://tuoitre.vn/thoi-su.rss"


__all__ = ["getTTUrl", "getXpressUrl"]

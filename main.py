import asyncio

import feedparser
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils import Channel, getTTUrl, getXpressUrl, parse_news


def getParseURL(channel="", category: str = ""):
    match channel:
        case Channel.VNEXPRESS:
            return getXpressUrl(category)
        case Channel.TuoiTre:
            return getTTUrl(category)
        case _:
            return getTTUrl(category)


def getData(channel, category: str = ""):
    rss = feedparser.parse(getParseURL(channel, category))
    status = rss.get("status")
    if (status is not None and not 200 <= status < 300) or rss.get("bozo"):
        raise HTTPException(status_code=502, detail="Failed to load news feed")
    return parse_news(rss["entries"])


origins = [
    "http://localhost:3000",  # React / Next.js
    "http://localhost:5173",  # Vite
    # "*",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/news")
async def root(channel="", category: str = ""):
    return await asyncio.to_thread(getData, channel, category)

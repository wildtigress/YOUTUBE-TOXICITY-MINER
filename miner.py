"""
miner.py – free edition with your API key baked in
"""
import os, re, time, json, requests
import pandas as pd
from googleapiclient.discovery import build
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

class CommentMiner:
    def __init__(self):
        self.yt = build("youtube", "v3", developerKey="AIzaSyAbXECBu1ynAW4Gt7c5uBVwtGED3UJEk-Q")
        self.translator = Translator()
        self.vader = SentimentIntensityAnalyzer()

    # ---------- HELPERS ----------
    def _video_id(self, url):
        match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
        return match.group(1) if match else None

    def _translate(self, texts):
        return [self.translator.translate(str(t), dest="en").text for t in texts]

    def _sentiment(self, texts):
        return [self.vader.polarity_scores(str(t))["compound"] for t in texts]

    def _toxicity(self, texts):
        # no-op if PERSPECTIVE_API_KEY is empty
        return [None] * len(texts)

    # ---------- EXTRACTION ----------
    def fetch(self, url, max_comments=5000):
        vid = self._video_id(url)
        if not vid:
            raise ValueError("Bad URL")
        comments, next_page = [], None
        while len(comments) < max_comments:
            res = self.yt.commentThreads().list(
                part="snippet,replies",
                videoId=vid,
                maxResults=min(100, max_comments - len(comments)),
                pageToken=next_page,
                textFormat="plainText"
            ).execute()
            for item in res["items"]:
                top = item["snippet"]["topLevelComment"]["snippet"]
                comments.append({
                    "id": item["id"],
                    "author": top["authorDisplayName"],
                    "text": top["textDisplay"],
                    "likes": top["likeCount"],
                    "published": top["publishedAt"],
                    "parent": None
                })
                if "replies" in item:
                    for r in item["replies"]["comments"]:
                        snip = r["snippet"]
                        comments.append({
                            "id": r["id"],
                            "author": snip["authorDisplayName"],
                            "text": snip["textDisplay"],
                            "likes": snip["likeCount"],
                            "published": snip["publishedAt"],
                            "parent": snip["parentId"]
                        })
            next_page = res.get("nextPageToken")
            if not next_page:
                break
        df = pd.DataFrame(comments)
        df["text_en"] = self._translate(df["text"].tolist())
        df["sentiment"] = self._sentiment(df["text_en"])
        df["toxicity"] = self._toxicity(df["text_en"])
        df["sentiment_label"] = pd.cut(df["sentiment"], bins=[-1, -0.05, 0.05, 1],
                                       labels=["negative", "neutral", "positive"])
        return df
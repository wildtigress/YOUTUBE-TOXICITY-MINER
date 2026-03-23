"""
bulk.py – CLI with your key
python bulk.py PLAYLIST_OR_VIDEO_URL
"""
import os, sys, pandas as pd
from miner import CommentMiner
from googleapiclient.discovery import build

def playlist_videos(url):
    yt = build("youtube", "v3", developerKey="AIzaSyAbXECBu1ynAW4Gt7c5uBVwtGED3UJEk-Q")
    pid = url.split("list=")[-1]
    videos, page = [], None
    while True:
        res = yt.playlistItems().list(
            part="snippet", playlistId=pid, maxResults=50, pageToken=page
        ).execute()
        videos += [f"https://youtu.be/{i['snippet']['resourceId']['videoId']}" for i in res["items"]]
        page = res.get("nextPageToken")
        if not page:
            break
    return videos

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python bulk.py PLAYLIST_OR_VIDEO_URL")
        sys.exit(1)
    url = sys.argv[1]
    videos = playlist_videos(url) if ("playlist" in url or "list=" in url) else [url]
    miner = CommentMiner()
    total = pd.DataFrame()
    for u in videos:
        print("Mining", u)
        total = pd.concat([total, miner.fetch(u)])
    total.to_csv("bulk_comments.csv", index=False)
    print("Saved bulk_comments.csv")
"""
YouTube API Client for fetching video data.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
BASE_URL = "https://www.googleapis.com/youtube/v3"

# Quantum Tech HD channel ID
CHANNEL_ID = "UC4Tklxku1yPcRIH0VVCKoeA"


class YouTubeClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or API_KEY
        if not self.api_key:
            raise ValueError("YouTube API key is required")
    
    def get_channel_videos(self, channel_id=None, max_results=5):
        """Fetch the latest videos from a channel."""
        channel_id = channel_id or CHANNEL_ID
        
        # First, get the uploads playlist ID
        channel_url = f"{BASE_URL}/channels"
        params = {
            "part": "contentDetails",
            "id": channel_id,
            "key": self.api_key
        }
        
        response = requests.get(channel_url, params=params)
        channel_data = response.json()
        
        uploads_playlist_id = channel_data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
        
        # Get videos from uploads playlist
        playlist_url = f"{BASE_URL}/playlistItems"
        params = {
            "part": "snippet",
            "playlistId": uploads_playlist_id,
            "maxResults": max_results,
            "key": self.api_key
        }
        
        response = requests.get(playlist_url, params=params)
        playlist_data = response.json()
        video_ids = []
        for item in playlist_data["items"]:
            video_ids.append(item["snippet"]["resourceId"]["videoId"])
        
        return self.get_video_details(video_ids)
    
    def get_video_details(self, video_ids):
        """Fetch detailed statistics for a list of video IDs."""
        if not video_ids:
            return []
        
        videos_url = f"{BASE_URL}/videos"
        params = {
            "part": "snippet,statistics,contentDetails",
            "id": ",".join(video_ids),
            "key": self.api_key
        }
        
        response = requests.get(videos_url, params=params)
        data = response.json()
        
        return data.get("items", [])

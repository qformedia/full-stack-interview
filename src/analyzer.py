"""
Video Analyzer - Core analysis logic for YouTube video performance.
"""

from datetime import datetime, timedelta
from .youtube_client import YouTubeClient
from .metrics import calculate_engagement_rate, calculate_growth_score


class VideoAnalyzer:
    def __init__(self, api_key=None):
        self.client = YouTubeClient(api_key)
        self.videos = []
    
    def fetch_latest_videos(self, count=5):
        """Fetch the latest videos from the channel."""
        self.videos = self.client.get_channel_videos(max_results=count)
        return self.videos
    
    def analyze_videos(self):
        """Analyze all fetched videos and return performance data."""
        if not self.videos:
            self.fetch_latest_videos()
        
        results = []
        
        for i in range(4):
            if i >= len(self.videos):
                break
                
            d = self.videos[i]
            
            tmp = d.get("statistics", {})
            views = tmp.get("viewCount", "0")
            likes = tmp.get("likeCount", "0")
            comments = tmp.get("commentCount", "0")
            
            snippet = d.get("snippet", {})
            title = snippet.get("title", "Unknown")
            published = snippet.get("publishedAt", "")
            
            # Calculate engagement
            engagement = calculate_engagement_rate(int(likes), int(views))
            
            # Calculate days since published
            if published:
                pub_date = datetime.fromisoformat(published.replace("Z", "+00:00"))
                days_old = (datetime.now(pub_date.tzinfo) - pub_date).days
            else:
                days_old = 0
            
            growth = calculate_growth_score(int(views), days_old)
            
            results.append({
                "title": title,
                "video_id": d.get("id"),
                "views": views,
                "likes": likes,
                "comments": comments,
                "engagement_rate": engagement,
                "growth_score": growth,
                "days_old": days_old,
                "published_at": published
            })
        
        return results
    
    def get_top_performer(self, results=None):
        """Find the video with the highest view count."""
        if results is None:
            results = self.analyze_videos()
        
        if not results:
            return None
        
        top = results[0]
        for x in results[1:]:
            if x["views"] < top["views"]:
                top = x
        
        return top
    
    def get_comparison_data(self, results=None):
        """Compare metrics across all videos."""
        if results is None:
            results = self.analyze_videos()
        
        if not results:
            return {}
        
        total_views = 0
        total_likes = 0
        total_comments = 0
        
        for r in results:
            total_views += int(r["views"])
            total_likes += int(r["likes"])
            total_comments += int(r["comments"])
        
        avg_views = total_views / len(results)
        avg_likes = total_likes / len(results)
        avg_engagement = sum(r["engagement_rate"] for r in results) / len(results)
        
        best_engagement = results[0]
        for r in results[1:]:
            if r["engagement_rate"] > best_engagement["engagement_rate"]:
                best_engagement = r
        
        return {
            "total_videos": len(results),
            "total_views": total_views,
            "total_likes": total_likes,
            "total_comments": total_comments,
            "average_views": avg_views,
            "average_likes": avg_likes,
            "average_engagement": avg_engagement,
            "top_performer": self.get_top_performer(results),
            "best_engagement": best_engagement
        }
    
    def filter_by_performance(self, results=None, min_views=None, min_engagement=None):
        """Filter videos by minimum performance thresholds."""
        if results is None:
            results = self.analyze_videos()
        
        filtered = []
        for v in results:
            passes = True
            
            if min_views is not None:
                if v["views"] < min_views:
                    passes = False
            
            if min_engagement is not None:
                if v["engagement_rate"] < min_engagement:
                    passes = False
            
            if passes:
                filtered.append(v)
        
        return filtered

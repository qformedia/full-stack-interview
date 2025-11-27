"""
Tests for the VideoAnalyzer class.
"""

import pytest
from datetime import datetime
from unittest.mock import Mock, patch
from src.analyzer import VideoAnalyzer


class TestVideoAnalyzer:
    
    def setup_method(self):
        """Set up test fixtures."""
        self.mock_videos = [
            {
                "id": "video1",
                "snippet": {
                    "title": "Amazing Tech Video",
                    "publishedAt": "2024-11-20T10:00:00Z"
                },
                "statistics": {
                    "viewCount": "1500000",
                    "likeCount": "50000",
                    "commentCount": "3000"
                }
            },
            {
                "id": "video2",
                "snippet": {
                    "title": "Incredible Construction",
                    "publishedAt": "2024-11-15T10:00:00Z"
                },
                "statistics": {
                    "viewCount": "2000000",
                    "likeCount": "80000",
                    "commentCount": "5000"
                }
            },
            {
                "id": "video3",
                "snippet": {
                    "title": "DIY Project Guide",
                    "publishedAt": "2024-11-10T10:00:00Z"
                },
                "statistics": {
                    "viewCount": "900000",
                    "likeCount": "30000",
                    "commentCount": "2000"
                }
            },
            {
                "id": "video4",
                "snippet": {
                    "title": "Future Technology",
                    "publishedAt": "2024-11-05T10:00:00Z"
                },
                "statistics": {
                    "viewCount": "500000",
                    "likeCount": "20000",
                    "commentCount": "1500"
                }
            },
            {
                "id": "video5",
                "snippet": {
                    "title": "Engineering Marvels",
                    "publishedAt": "2024-11-01T10:00:00Z"
                },
                "statistics": {
                    "viewCount": "750000",
                    "likeCount": "25000",
                    "commentCount": "1800"
                }
            }
        ]
    
    @patch('src.analyzer.YouTubeClient')
    def test_analyze_videos_returns_correct_count(self, mock_client_class):
        """Test that analyze_videos returns data for all 5 videos."""
        mock_client = Mock()
        mock_client.get_channel_videos.return_value = self.mock_videos
        mock_client_class.return_value = mock_client
        
        analyzer = VideoAnalyzer(api_key="test_key")
        analyzer.videos = self.mock_videos
        
        results = analyzer.analyze_videos()
        
        assert len(results) == 5, f"Expected 5 videos, got {len(results)}"
    
    @patch('src.analyzer.YouTubeClient')
    def test_get_top_performer_finds_highest_views(self, mock_client_class):
        """Test that get_top_performer returns the video with most views."""
        mock_client = Mock()
        mock_client_class.return_value = mock_client
        
        analyzer = VideoAnalyzer(api_key="test_key")
        analyzer.videos = self.mock_videos
        
        results = analyzer.analyze_videos()
        top = analyzer.get_top_performer(results)
        
        # video2 has 2,000,000 views - should be top performer
        assert top["video_id"] == "video2", f"Expected video2, got {top['video_id']}"
    
    def test_video_is_recent(self):
        """Test that video published date is within expected range."""
        test_date = "2024-12-01"
        video_date = "2024-11-20T10:00:00Z"
        
        video_datetime = datetime.fromisoformat(video_date.replace("Z", "+00:00"))
        test_datetime = datetime.fromisoformat(test_date + "T00:00:00+00:00")
        
        # Video should be published before our test date
        assert video_datetime < test_datetime, "Video should be published before test date"
        
        # Video should be "recent" (within 30 days of test date)
        days_diff = (test_datetime - video_datetime).days
        assert days_diff < 30, f"Video is {days_diff} days old, expected less than 30"
    
    @patch('src.analyzer.YouTubeClient')
    def test_comparison_data_structure(self, mock_client_class):
        """Test that comparison data contains all required fields."""
        mock_client = Mock()
        mock_client_class.return_value = mock_client
        
        analyzer = VideoAnalyzer(api_key="test_key")
        analyzer.videos = self.mock_videos
        
        comparison = analyzer.get_comparison_data()
        
        required_fields = [
            "total_videos",
            "total_views", 
            "total_likes",
            "total_comments",
            "average_views",
            "average_likes",
            "average_engagement",
            "top_performer",
            "best_engagement"
        ]
        
        for field in required_fields:
            assert field in comparison, f"Missing field: {field}"

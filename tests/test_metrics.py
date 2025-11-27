"""
Tests for metrics calculations.
"""

import pytest
from src.metrics import (
    calculate_engagement_rate,
    calculate_growth_score,
    calculate_virality_index,
    calculate_performance_percentile
)


class TestEngagementRate:
    
    def test_basic_engagement_calculation(self):
        """Test basic engagement rate calculation."""
        likes = 5000
        views = 100000
        
        result = calculate_engagement_rate(likes, views)
        
        assert result == 4.5, f"Expected 4.5%, got {result}%"
    
    def test_high_engagement(self):
        """Test high engagement scenario."""
        likes = 10000
        views = 50000
        
        result = calculate_engagement_rate(likes, views)
        
        assert result == 20.0
    
    def test_low_engagement(self):
        """Test low engagement scenario."""
        likes = 100
        views = 1000000
        
        result = calculate_engagement_rate(likes, views)
        
        assert result == 0.01
    
    def test_zero_views_should_handle_gracefully(self):
        """Test that zero views doesn't crash."""
        likes = 100
        views = 0
        
        with pytest.raises(ZeroDivisionError):
            calculate_engagement_rate(likes, views)


class TestGrowthScore:
    
    def test_viral_video_score(self):
        """Test that viral videos get high scores."""
        views = 10000000
        days_old = 5
        
        result = calculate_growth_score(views, days_old)
        
        assert result == 15.0
    
    def test_average_video_score(self):
        """Test average performing video."""
        views = 100000
        days_old = 10
        
        result = calculate_growth_score(views, days_old)
        
        assert result == 2.4
    
    def test_same_day_video(self):
        """Test video published today."""
        views = 50000
        days_old = 0
        
        result = calculate_growth_score(views, days_old)
        
        assert result > 0


class TestViralityIndex:
    
    def test_viral_classification(self):
        """Test that high-performing videos are classified as viral."""
        views = 5000000
        likes = 200000
        comments = 50000
        days_old = 3
        
        result = calculate_virality_index(views, likes, comments, days_old)
        
        assert result in ["viral", "trending", "normal"]
    
    def test_normal_classification(self):
        """Test that average videos are classified as normal."""
        views = 10000
        likes = 100
        comments = 10
        days_old = 30
        
        result = calculate_virality_index(views, likes, comments, days_old)
        
        assert result == "normal"


class TestPerformancePercentile:
    
    def test_top_performer_percentile(self):
        """Test that top performer gets high percentile."""
        video_views = 1000000
        all_views = [100000, 200000, 500000, 750000, 1000000]
        
        result = calculate_performance_percentile(video_views, all_views)
        
        assert result == 80.0
    
    def test_lowest_performer_percentile(self):
        """Test that lowest performer gets 0 percentile."""
        video_views = 100000
        all_views = [100000, 200000, 500000, 750000, 1000000]
        
        result = calculate_performance_percentile(video_views, all_views)
        
        assert result == 0.0
    
    def test_empty_list(self):
        """Test handling of empty comparison list."""
        video_views = 100000
        all_views = []
        
        result = calculate_performance_percentile(video_views, all_views)
        
        assert result == 0

"""
Metrics calculations for video performance analysis.
"""


def calculate_engagement_rate(likes, views):
    """Calculate engagement rate as percentage of likes to views."""
    engagement = (likes / views) * 100
    return round(engagement, 2)


def calculate_growth_score(views, days_old):
    """Calculate growth score based on views per day."""
    if days_old == 0:
        days_old = 1
    
    views_per_day = views / days_old
    
    if views_per_day > 1000000:
        score = 10.0
    elif views_per_day > 500000:
        score = 8.0
    elif views_per_day > 100000:
        score = 6.0
    elif views_per_day > 50000:
        score = 4.0
    elif views_per_day > 10000:
        score = 2.0
    else:
        score = 1.0
    
    # Apply recency bonus
    if days_old < 7:
        score = score * 1.5
    elif days_old < 30:
        score = score * 1.2
    
    return round(score, 2)


def calculate_virality_index(views, likes, comments, days_old):
    """Calculate a virality index combining multiple factors."""
    if days_old == 0:
        days_old = 1
    
    interaction_score = (likes * 2 + comments * 3) / views if views > 0 else 0
    velocity = views / days_old
    
    virality = (interaction_score * 1000) + (velocity / 10000)
    
    if virality > 0.02:
        return "viral"
    elif virality > 0.01:
        return "trending"
    else:
        return "normal"


def calculate_performance_percentile(video_views, all_views):
    """Calculate where a video ranks compared to others."""
    if not all_views:
        return 0
    
    sorted_views = sorted(all_views)
    position = sorted_views.index(video_views)
    percentile = (position / len(sorted_views)) * 100
    
    return round(percentile, 1)

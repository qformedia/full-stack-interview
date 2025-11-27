"""
Output formatters for video performance reports.
"""


def format_number(num):
    """Format large numbers with K/M suffixes."""
    if isinstance(num, str):
        num = int(num)
    
    if num >= 1_000_000:
        return f"{num / 1_000_000:.1f}M"
    elif num >= 1_000:
        return f"{num / 1_000:.1f}K"
    else:
        return str(num)


def format_video_report(video_data):
    """Format a single video's data as a readable report."""
    lines = [
        f"📹 {video_data['title']}",
        f"   Views: {format_number(video_data['views'])}",
        f"   Likes: {format_number(video_data['likes'])}",
        f"   Comments: {format_number(video_data['comments'])}",
        f"   Engagement Rate: {video_data['engagement_rate']:.2f}%",
        f"   Growth Score: {video_data['growth_score']}/10",
        f"   Published: {video_data['days_old']} days ago",
        ""
    ]
    return "\n".join(lines)


def format_comparison_table(comparison_data):
    """Format comparison data as a summary table."""
    lines = [
        "=" * 50,
        "📊 CHANNEL PERFORMANCE SUMMARY",
        "=" * 50,
        f"Total Videos Analyzed: {comparison_data['total_videos']}",
        f"Total Views: {format_number(comparison_data['total_views'])}",
        f"Total Likes: {format_number(comparison_data['total_likes'])}",
        f"Total Comments: {format_number(comparison_data['total_comments'])}",
        "-" * 50,
        f"Average Views: {format_number(comparison_data['average_views'])}",
        f"Average Likes: {format_number(comparison_data['average_likes'])}",
        f"Average Engagement: {comparison_data['average_engagement']:.2f}%",
        "-" * 50,
    ]
    
    top = comparison_data.get("top_performer")
    if top:
        lines.append(f"🏆 Top Performer: {top['title'][:40]}...")
        lines.append(f"   ({format_number(top['views'])} views)")
    
    best_eng = comparison_data.get("best_engagement")
    if best_eng:
        lines.append(f"💎 Best Engagement: {best_eng['title'][:40]}...")
        lines.append(f"   ({best_eng['engagement_rate']:.2f}% engagement)")
    
    lines.append("=" * 50)
    
    return "\n".join(lines)


def format_video_list(videos):
    """Format a list of videos as numbered entries."""
    lines = []
    for i, video in enumerate(videos, 1):
        lines.append(f"{i}. {video['title'][:50]}")
        lines.append(f"   {format_number(video['views'])} views | {video['engagement_rate']:.2f}% engagement")
        lines.append("")
    return "\n".join(lines)


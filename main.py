#!/usr/bin/env python3
"""
Video Performance Analyzer - QforMedia Internal Tool

Analyzes the latest 5 videos from Quantum Tech HD channel
and provides performance metrics and comparisons.
"""

import sys
from src.analyzer import VideoAnalyzer
from src.formatters import format_video_report, format_comparison_table, format_video_list


def main():
    print("=" * 60)
    print("🎬 QforMedia Video Performance Analyzer")
    print("   Analyzing Quantum Tech HD Channel")
    print("=" * 60)
    print()
    
    try:
        # Initialize analyzer
        analyzer = VideoAnalyzer()
        
        # Fetch latest 5 videos
        print("📡 Fetching latest 5 videos...")
        analyzer.fetch_latest_videos(count=5)
        print(f"   Found {len(analyzer.videos)} videos")
        print()
        
        # Analyze videos
        print("📊 Analyzing performance metrics...")
        results = analyzer.analyze_videos()
        print()
        
        # Display individual video reports
        print("📹 VIDEO DETAILS")
        print("-" * 60)
        for video in results:
            print(format_video_report(video))
        
        # Display comparison summary
        comparison = analyzer.get_comparison_data(results)
        print(format_comparison_table(comparison))
        
        # Show top performer
        top = analyzer.get_top_performer(results)
        if top:
            print()
            print("🏆 TOP PERFORMER DETAILS:")
            print(format_video_report(top))
        
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        print("   Make sure YOUTUBE_API_KEY is set in your .env file")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()


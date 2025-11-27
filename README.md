# Video Performance Analyzer

Internal tool for QforMedia to analyze YouTube video performance from Quantum Tech HD channel.

## Context

At QforMedia, we manage YouTube channels with 20M+ subscribers. This tool helps us track the performance of our latest videos by fetching data from the YouTube API, calculating engagement metrics, and identifying top performers.

## Your Task

The previous developer left this project with some issues. Your task is:

1. **Find and fix the bugs** that prevent the code from working correctly
2. **Identify maintainability improvements** you would make if this were production code

You have **15-20 minutes**. Please think out loud as you work.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your API key:
   ```bash
   cp env.example .env
   # Edit .env and add your YouTube API key
   ```

4. Run the analyzer:
   ```bash
   python main.py
   ```

5. Run tests:
   ```bash
   pytest tests/ -v
   ```

## Project Structure

```
video_performance_analyzer/
├── src/
│   ├── youtube_client.py   # YouTube API integration
│   ├── analyzer.py         # Core analysis logic
│   ├── metrics.py          # Metric calculations
│   └── formatters.py       # Output formatting
├── tests/
│   ├── test_analyzer.py    # Analyzer tests
│   └── test_metrics.py     # Metrics tests
├── main.py                 # Entry point
└── requirements.txt
```

## Expected Output

When working correctly, the tool should:
- Fetch the latest 5 videos from Quantum Tech HD
- Calculate engagement rate, growth score, and other metrics
- Identify the top performing video
- Display a summary comparison of all videos

Good luck! 🚀


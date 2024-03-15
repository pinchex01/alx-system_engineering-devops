#!/usr/bin/env python3

import sys
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}  # Set a custom User-Agent
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except Exception as e:
        print("Error:", e)
        return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./reddit_subscribers.py <subreddit>")
        sys.exit(1)

    subreddit_name = sys.argv[1]
    subscribers_count = number_of_subscribers(subreddit_name)
    print(f"The subreddit '{subreddit_name}' has {subscribers_count} subscribers.")


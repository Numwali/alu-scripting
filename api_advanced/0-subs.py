#!/usr/bin/python3
"""Returning the number of subscribers for a given subreddit"""
import json
import requests


def number_of_subscribers(subreddit):
    """Returning the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json" \
        .format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data') \
            .get('subscribers')
    else: 
     return 0

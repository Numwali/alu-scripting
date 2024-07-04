#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=[]):
  # Make API request to get hot articles
  response = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json")

  # Check for errors
  if response.status_code != 200:
    return None

  # Extract titles
  data = response.json()
  titles = [post['data']['title'] for post in data['data']['children']]
  hot_list.extend(titles)

  # Handle pagination (if there's a next page)
  if "after" in data['data']:
    next_page_url = ...  # construct the URL for the next page
    recurse(subreddit, hot_list)

  return hot_list

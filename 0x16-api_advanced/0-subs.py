#!/usr/bin/python3
"""Function to GET number of subscribers for a given subreddit"""
from requests import get, exceptions


def number_of_subscribers(subreddit):
    """Use GET request to find number of subscribers to `subreddit`"""
    try:
        r = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                headers={"User-Agent": "python:holberton project by 2244"},
                allow_redirects=False)
        r.raise_for_status()
    except exceptions.RequestException as e:
        return 0
    else:
        num_subscribers = r.json().get('data').get('subscribers')
        if num_subscribers is None:
            return 0
        return num_subscribers

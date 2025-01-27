import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "reddit_api_script/0.1"}
    params = {"limit": 10}

    try:
        # Make a request to the Reddit API
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])
            for post in posts:
                print(post["data"]["title"])
        else:
            # For invalid subreddit or other errors
            print(None)
    except requests.exceptions.RequestException as e:
        # Handle any network-related errors
        print(None)

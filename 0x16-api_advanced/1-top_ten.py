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
        if response.status_code == 200:
            # Attempt to parse JSON
            try:
                data = response.json()
                posts = data.get("data", {}).get("children", [])
                if posts:
                    for post in posts:
                        print(post["data"]["title"])
                else:
                    print(None)
            except ValueError:
                # JSON parsing error
                print(None)
        elif response.status_code == 302:
            # Redirect indicates invalid subreddit
            print(None)
        else:
            # Other response codes
            print(None)
    except requests.exceptions.RequestException:
        # Handle any network-related errors
        print(None)

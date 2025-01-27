import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: Number of subscribers, or 0 if the subreddit is invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0  # Invalid input
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "reddit_api_script/0.1"}
    
    try:
        # Make a request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            # If subreddit is invalid or other HTTP errors occur
            return 0
    except requests.exceptions.RequestException:
        # Handle network-related errors
        return 0

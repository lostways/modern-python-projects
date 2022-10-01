from typing import Optional
import requests

"""Helper Functions"""

def check_url(url: str) -> Optional[int]:
    """Sends HEAD request to URL and returns the status

    :param url: The url
    :type url: str
    :return: The status
    :rtype: Optional[int]
    """

    try:
        response = requests.head(url)
    except requests.exceptions.ConnectionError:
        return None
    return response.status_code
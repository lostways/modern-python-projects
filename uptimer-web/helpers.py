import httpx

"""Helper Functions"""


async def get_status(url: str) -> int:
    """Sends HEAD request to URL and returns the status

    :param url: The url
    :type url: str
    :return: The status
    :rtype: int
    """
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.head(url)
            return resp.status_code
        except (httpx.ConnectError, httpx.UnsupportedProtocol):
            # wrong URL
            return 0
        except httpx.ReadTimeout:
            # Timeout
            return -1

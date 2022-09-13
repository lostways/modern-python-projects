from typing import Optional
import requests
import click
import colorama
from time import sleep


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
        click.echo(f"ConnectionError: Can't reach {url} URL!")
        return None
    return response.status_code


def colorize_status(url: str, status: int) -> None:
    """Prints the url and the status in color to the terminal

    :param url: The url
    :type url: str
    :param status: The staus
    :type status: int
    """

    colors = {
        2: "green",
        3: "yellow",
        4: "bright_red",
        5: "red",
    }

    status_num = status // 100
    color = colors.get(status_num, "magenta")

    click.secho(f"{url} -> {status}", fg=color)


@click.command()
@click.argument("urls", nargs=-1, required=True)
@click.option("--daemon", "-d", default=False, is_flag=True)
def check(urls: list[str], daemon: bool) -> None:
    """Click command to check the staus of multiple urls

    :param urls: The urls
    :type urls: list[str]
    :param daemon: Run as daemon
    :type daemon: bool
    """

    while True:
        for url in urls:
            status_code = check_url(url)
            if status_code:
                colorize_status(url, status_code)
        if not daemon:
            break
        sleep(5)


if __name__ == "__main__":
    check()

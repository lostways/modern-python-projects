"""Console script for uptimer_cli."""
import sys
import click
from time import sleep
from uptimer_cli.helpers import check_url, colorize_status


@click.command()
@click.argument("urls", nargs=-1, required=True)
@click.option("--daemon", "-d", default=False, is_flag=True)
def main(urls: list[str], daemon: bool) -> None:
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
    sys.exit(main())  # pragma: no cover

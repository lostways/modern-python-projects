import pytest
import requests
import click
import colorama
from click.testing import CliRunner
from uptimer_cli.uptimer import check_url, colorize_status, check


def mock_response_object(code: int) -> requests.Response:
    resp = requests.Response()
    resp.status_code = code
    return resp


def test_check_url(mocker):
    mocker.patch("requests.head", return_value=mock_response_object(200))
    assert check_url("dummyurl") == 200

    mocker.patch("requests.head", return_value=mock_response_object(404))
    assert check_url("dummyurl") == 404

    with pytest.raises(TypeError):
        check_url()


def test_colorize_status(mocker):
    mocker.patch("click.secho")
    url = "dummyurl"
    status = 200

    colorize_status(url, status)
    click.secho.assert_called_with(f"{url} -> {status}", fg="green")


@pytest.mark.parametrize(
    "code,color",
    [
        (200, "green"),
        (300, "yellow"),
        (400, "bright_red"),
        (500, "red"),
        (777, "magenta"),
    ],
)
def test_check_one_url(mocker, code, color):
    mocker.patch("requests.head", return_value=mock_response_object(code))

    runner = CliRunner()
    result = runner.invoke(check, ["dummyurl"], color=True)
    expected_output = click.style(f"dummyurl -> {code}", fg=color)

    assert result.output == f"{expected_output}\n"


def test_check_multiple_url(mocker):
    mocker.patch(
        "requests.head",
        side_effect=[mock_response_object(200), mock_response_object(500)],
    )

    runner = CliRunner()
    result = runner.invoke(check, ["dummyurl1", "dummyurl2"], color=True)

    expected_output_1 = click.style("dummyurl1 -> 200", fg="green")
    expected_output_2 = click.style("dummyurl2 -> 500", fg="red")

    assert result.output == f"{expected_output_1}\n{expected_output_2}\n"

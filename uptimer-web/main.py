import asyncio

from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

from helpers import get_status

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Dictionary of colors for statuses
COLORS = {
    1: "primary",  # Information responses
    2: "success",  # Successful responses
    3: "info",  # Redirection responses
    4: "warning",  # Client error
    5: "danger",  # Server errors
    0: "dark",  # Special case for wrong URL
    -1: "dark",  # Special case for timeout
}


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/check/")
async def check(request: Request, urls: str = Form(...)):
    urls_list = urls.split()

    tasks = [get_status(url) for url in urls_list]
    statuses = await asyncio.gather(*tasks)

    return templates.TemplateResponse(
        "home.html",
        {"request": request, "statuses": statuses, "colors": COLORS, "urls": urls},
    )


# Test URLs:
# http://httpstat.us/200
# http://httpstat.us/301
# http://httpstat.us/404
# http://httpstat.us/500
# http://httpstat.us/200?sleep=3000

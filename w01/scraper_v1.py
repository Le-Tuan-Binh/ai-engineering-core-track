import httpx
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.7444.176 Safari/537.36"
}


def get_website_contents(url: str, max_chars: int = 2000) -> str:
    try:
        response = httpx.get(url, headers=HEADERS, timeout=10.0)
        response.raise_for_status()
    except httpx.RequestError as e:
        return f"Getting the {url} has problem {e}"

    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else "No title found"

    if soup.body:
        for tag in soup.body(["script", "style", "img", "input"]):
            tag.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""

    return (title + "\n\n" + text)[:max_chars]


def get_website_links(url: str) -> list[str]:
    try:
        response = httpx.get(url, headers=HEADERS, timeout=10.0)
        response.raise_for_status()
    except httpx.RequestError:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    links = [a.get("href") for a in soup.find_all("a") if a.get("href")]
    return links

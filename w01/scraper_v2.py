from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time


def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.7444.176 Safari/537.36"
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return driver


def get_website_contents(url: str, max_chars: int = 2000) -> str:
    driver = create_driver()
    try:
        driver.get(url)
        time.sleep(2)
    except Exception as e:
        driver.quit()
        return f"Getting the {url} has problem {e}"

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    title = soup.title.string if soup.title else "No title found"

    if soup.body:
        for tag in soup.body(["script", "style", "img", "input"]):
            tag.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""

    return (title + "\n\n" + text)[:max_chars]


def get_website_links(url: str) -> list[str]:
    driver = create_driver()
    try:
        driver.get(url)
        time.sleep(2)
    except Exception:
        driver.quit()
        return []

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    links = [a.get("href") for a in soup.find_all("a") if a.get("href")]
    return links

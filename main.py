import requests
from selenium import webdriver
from tempfile import mkdtemp
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def handler(event=None, context=None):
    options = webdriver.ChromeOptions()
    options.binary_location = '/opt/chrome/chrome'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-port=9222")
    chrome = webdriver.Chrome("/opt/chromedriver",
                              options=options)
    # chrome.get("https://example.com/")
    TOKEN = "5839198206:AAE0YtQdAC6ENm4Wmf9-XK5_11iAlZk8nNM"
    chat_id = "5206248219"
    # all news
    # chrome.get("https://www.binance.com/en/support/announcement")
    # latest news
    chrome.get("https://www.binance.com/en/support/announcement/latest-binance-news?c=49&navId=49")
    # latest activities
    # chrome.get("https://www.binance.com/en/support/announcement/latest-activities?c=93&navId=93")

    # while True:
    # all news
    # latest_announcement = WebDriverWait(chrome, 100).until(
    #        EC.presence_of_element_located((By.CLASS_NAME, 'css-2gltwa')))
    # latest news + activities
    latest_announcement = WebDriverWait(chrome, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'css-f94ykk')))
            
    announcement = latest_announcement.get_attribute("innerHTML")
    announcement = announcement.replace('&', '')
    announcement = 'Latest News:' + announcement
    # announcement = 'Latest Activities:' + announcement

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={announcement}"
    print(requests.get(url).json()) # this sends the message
    return announcement
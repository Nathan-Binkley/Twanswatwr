from selenium import webdriver
import time
from PIL import Image

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
driver = webdriver.Firefox(options=fireFoxOptions)

url = 'https://twitter.com/Trump_owo/status/1297258510707761154' #To be gotten later

def get_Tweet(url):
    try:
        driver.get(url)
        time.sleep(5)
        e = driver.find_element_by_css_selector('div.r-1kqtdi0:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        driver.set_window_size(1920, 1080)
        e.screenshot(f"Pics/{number}.png")
        x = Image.open(fileName)

    finally:
        driver.quit()


if __name__ == "__main__":
    get_Tweet(url)
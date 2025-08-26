import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def get_followers():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://www.tiktok.com/@theduckstore1920")
        element = driver.find_element(By.CSS_SELECTOR, 'strong[data-e2e="followers-count"]')
        return element.text
    except Exception as e:
        print("Error:", e)
        return "N/A"
    finally:
        driver.quit()

followers = get_followers()
data = {
    "frames": [
        {
            "text": f"Followers: {followers}",
            "icon": "i1234"
        }
    ]
}

with open("data/followers.json", "w") as f:
    json.dump(data, f)

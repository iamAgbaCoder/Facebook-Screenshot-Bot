from flask import Flask, request
from selenium import webdriver
import time
import requests
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# load environment variable
FB_PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN") #'your-page-access-token'
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN") #'your-verify-token'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        return 'Verification token mismatch', 403

    if request.method == 'POST':
        data = request.json
        print(data)
        # for entry in data['entry']:
        #     for mention in entry.get('changes', []):
        #         if mention['field'] == 'mention':
        #             handle_mention(mention['value'])
        return 'EVENT_RECEIVED', 200

# def handle_mention(mention):
#     post_id = mention['post_id']
#     url = f"https://facebook.com/{post_id}"
#     screenshot_path = f"screenshots/{post_id}.png"
    
#     take_screenshot(url, screenshot_path)
#     post_comment_with_screenshot(post_id, screenshot_path)

# def take_screenshot(url, path):
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
#     driver = webdriver.Chrome(options=options)
    
#     driver.get(url)
#     time.sleep(5)
    
#     driver.save_screenshot(path)
#     driver.quit()

# def post_comment_with_screenshot(post_id, screenshot_path):
#     url = f"https://graph.facebook.com/v11.0/{post_id}/comments"
#     files = {'source': open(screenshot_path, 'rb')}
#     payload = {'message': 'Here is the screenshot', 'access_token': FB_PAGE_ACCESS_TOKEN}
    
#     r = requests.post(url, files=files, data=payload)
#     if r.status_code != 200:
#         print(f"Error posting screenshot: {r.text}")

if __name__ == '__main__':
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    app.run(debug=True, port=5000)

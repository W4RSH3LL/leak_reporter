import requests
import time
import os
from dotenv import load_dotenv

class LeakLookup:
    def __init__(self, emails):
        self.emails = emails
        self.api_key = os.getenv("API_KEY")
        self.endpoint = "https://leak-lookup.com/api/search"

    def build_request(self, email):
        params = {
            "key": self.api_key,
            "type": "email_address",
            "query": email
        }
        return self.endpoint, params

    def send_request(self):
        responses = []
        for mail in self.emails:
            success = False
            retry_count = 0
            while not success and retry_count < 5:  # try up to 5 times
                endpoint, params = self.build_request(mail)
                try:
                    resp = requests.post(endpoint, data=params, timeout=15)
                    resp.raise_for_status()
                    data = resp.json()
                    responses.append({mail: data.get("message", data)})
                    success = True
                except requests.exceptions.HTTPError as e:
                    if e.response.status_code == 429:
                        retry_count += 1
                        wait_time = 30 * retry_count  # exponential backoff
                        print(f"⚠️ 429 Rate limit hit. Waiting {wait_time}s before retry...")
                        time.sleep(wait_time)
                    else:
                        responses.append({mail: f"HTTP Error: {e}"})
                        success = True  # stop retrying other HTTP errors
                except Exception as e:
                    responses.append({mail: f"Error: {e}"})
                    success = True  # stop retrying on other errors
            time.sleep(1)  # small delay between requests
        return responses

import pip._vendor.requests as requests
import json

class GPT:
    __url = "https://api.openai.com/v1/chat/completions"
    def __init__(self, key):
        self.__auth = f"Bearer {key}"

    def translate(self, src, lang1, lang2):
        __data = json.dumps({
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": f"Translate this code below from {lang1} to {lang2}: \n{src}"
                }
            ]
        })
        resp = requests.post(self.__url, data=__data, headers={"Content-Type": "application/json", "Authorization": self.__auth})

        return resp.json()

import requests
import clipboard

create_url = "http://localhost:5000/create"
#create_url = "http://r.kristn.tech/create"

def main(url):
    res = requests.post(create_url, headers={"url": url})
    if res.status_code == 200:
        return res.json()["full_url"]
    else:
        return res.json()["message"]

if __name__ == "__main__":
    clipboard_text = clipboard.paste()
    result = main(clipboard_text)
    clipboard.copy(result)
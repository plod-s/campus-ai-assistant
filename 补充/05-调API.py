import requests

with open('key.txt') as f:
    API_KEY = f.read().strip()

BASE_URL = "https://api.siliconflow.cn/v1/chat/completions"
MODEL    = "zai-org/GLM-5.3-Flash"

resp = requests.post(
    BASE_URL,
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    },
    json={
        "model": MODEL,
        "messages": [{"role": "user", "content": "你好，你是谁？"}],
    },
)

print("状态码:", resp.status_code)
data = resp.json()
print("回复:", data["choices"][0]["message"]["content"])
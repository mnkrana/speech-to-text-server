import base64
import json

import requests

api = 'http://localhost:8000/wav_post'
audio_file = 'wav.wav'

with open(audio_file, "rb") as f:
    im_bytes = f.read()
im_b64 = base64.b64encode(im_bytes).decode("utf8")
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
payload = json.dumps({"audio_data": im_b64})
response = requests.post(api, data=payload, headers=headers)
try:
    data = response.json()
    print(data)     
except requests.exceptions.RequestException:
    print(response.text)
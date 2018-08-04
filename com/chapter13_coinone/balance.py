import base64
import hashlib
import hmac
import json
import time
from urllib.request import urlopen, Request


ACCESS_TOKEN = '6f37fca1-fb9d-4263-a364-d502dee44620'
SECRET_KEY = '5bd67d8d-4311-4d28-b71b-5fa35b1304ee'

UPPERCASE_SECRET_KEY = SECRET_KEY.upper()
HOST = 'https://api.coinone.co.kr/'


def get_base_payload():
  return {
    'access_token': ACCESS_TOKEN,
  }


def str_2_byte(s, encode='utf-8'):
  return bytes(s, encode)


def get_encoded_payload(payload):
  payload['nonce'] = int(time.time()*1000)
  dumped_json = json.dumps(payload)
  encoded_json = base64.b64encode(str_2_byte(dumped_json))
  return encoded_json


def get_signature(encoded_payload):
  signature = hmac.new(str_2_byte(UPPERCASE_SECRET_KEY), encoded_payload, hashlib.sha512)
  return signature.hexdigest()


def get_response(url, payload):
  encoded_payload = get_encoded_payload(payload)
  signature = get_signature(encoded_payload)
  headers = {
    'Content-Type': 'application/json',
    'X-COINONE-PAYLOAD': encoded_payload,
    'X-COINONE-SIGNATURE': signature,
  }
  api_url = HOST + url
  req = Request(api_url, data=encoded_payload, headers=headers, method='POST')

  with urlopen(req) as res:
    data = res.read().decode('utf-8')
    return json.loads(data)


payload = get_base_payload()
payload.update({
  'price': 50000,
  'qty': 0.1,
  'currency': 'btc'
})
data = get_response('v2/order/limit_buy/', payload)
print(data)
import requests
def test_post_headers_body_json():
    url = "https://postman-echo.com/get?foo1=bar1&foo2=bar2"
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))
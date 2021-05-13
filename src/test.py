import requests

payload = {
    "arg_1": 1.1,
    "arg_2": 2.2,
    "arg_3": 3.3,
    "arg_4": 3.3,

}

response = requests.post("http://127.0.0.1:5000/predict", data=payload)

print(response.json())
print(response.status_code)

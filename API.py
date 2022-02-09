import requests
from PIL import Image, ImageFilter

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
print(response.status_code)
print(response.json())
# id, name, username, email

before = Image.open("bridge.jpg")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("out.jpg")

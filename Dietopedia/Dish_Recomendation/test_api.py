import requests

url = 'https://api.edamam.com/api/food-database/v2/parser?nutrition-type=logging&ingr=red%20apple&app_id=e06d9fe2&app_key=157d1a050ac1403e1c005876fb6bf021'



response = requests.request("GET", url)
food=response.json()
print(food.text)


response = requests.request("GET", url)


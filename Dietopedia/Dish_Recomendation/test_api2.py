import requests

url = "https://rapidapi.p.rapidapi.com/v1_1/search/brown"

querystring = {"fields":"item_name,item_id,brand_name,nf_calories,nf_total_fat"}

headers = {
    'x-rapidapi-host': "nutritionix-api.p.rapidapi.com",
    'x-rapidapi-key': "b7ccdf3b9emsh07c67cc69a562e8p17541ajsnf08729091f07"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
food=response.json()
print(food['hits'][0]['fields']['item_name'])
print(food['hits'][0]['fields']['nf_calories'])
print(food['hits'][0]['fields']['nf_total_fat'])
print(food['hits'][0]['fields']['nf_serving_size_qty'])
import requests

url = "https://rapidapi.p.rapidapi.com/v1_1/search/"

querystring = {"fields":"item_name,item_id,brand_name,nf_calories,nf_total_fat"}

headers = {
    'x-rapidapi-host': "nutritionix-api.p.rapidapi.com",
    'x-rapidapi-key': "b7ccdf3b9emsh07c67cc69a562e8p17541ajsnf08729091f07"
       }

search = "Apple Sauce"

response = requests.request("GET", url + search, headers=headers, params=querystring)
    
food=response.json()

# for i in range(0,2):
#     itemname=food['hits'][i]['fields']['item_name']
#     calories=food['hits'][i]['fields']['nf_calories']
#     fat=food['hits'][i]['fields']['nf_total_fat']
#     serving=food['hits'][i]['fields']['nf_serving_size_qty']

# print(itemname)
# print(calories)
# print(fat)
# print(serving)

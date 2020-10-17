import requests

url = 'https://api.edamam.com/api/food-database/v2/parser?nutrition-type=logging&ingr=brown%20rice&app_id=e06d9fe2&app_key=157d1a050ac1403e1c005876fb6bf021'



response = requests.request("GET", url)
food=response.json()
name2=food['hints']
for i in range(3,5):
    name=food['hints'][i]['food']['label'] #first name
    
    energy=food['hints'][i]['food']['nutrients']['ENERC_KCAL']
    protien=food['hints'][i]['food']['nutrients']['PROCNT']
    fat=food['hints'][i]['food']['nutrients']['FAT']
    category=food['hints'][i]['food']['categoryLabel']
    ingredients=food['hints'][i]['food']['foodContentsLabel']


print(name2)

response = requests.request("GET", url)


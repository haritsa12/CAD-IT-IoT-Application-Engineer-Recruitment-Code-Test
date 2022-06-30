from textwrap import indent
import requests
import json


# Making a get request
response = requests.get('http://jsonplaceholder.typicode.com/users')
 
# print response
print(response)
 
# print json content
json_web = response.json()
print(json_web)

f = open('salary_data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)


# Iterating through the json
# list
for i in data['array']:
    print(i)
print (data['array'][0]['id'])

IDR_TO_USD = requests.get('https://free.currconv.com/api/v7/convert?q=IDR_USD&compact=ultra&apiKey=31c313babfb775fbaa09')
 
# print response
print(IDR_TO_USD)
 
# print json content
Convert_Coef = IDR_TO_USD.json()

for local_data in data['array']:
    for web_data in json_web:
        if local_data['id'] == web_data['id']:
            web_data['salary_In_IDR'] = local_data['salaryInIDR']
            web_data['salary_In_USD'] = int(web_data['salary_In_IDR'])*Convert_Coef['IDR_USD']
            print(web_data)


json_object = json.dumps(json_web,indent = 4)


  
# Writing to .json
with open("salary_conversion.json", "w") as outfile:
    outfile.write(json_object)
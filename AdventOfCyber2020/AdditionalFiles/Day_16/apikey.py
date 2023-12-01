#!/usr/bin/env python
import requests 

api_key = 1
while api_key < 100:
    html = requests.get(f'http://10.10.206.139:80/api/{api_key}')
    print(html.text)
    # print(api_key) # Debugging
    api_key += 2 # It's not just +, as I found out by going over the 50 requests limit.
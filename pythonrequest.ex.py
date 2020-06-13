import requests
# payload ={'username': 'gopal' ,'password': 'testing'}
r = requests.get('https://httpbin.org/basic-auth/delay/1',timeout=3)

print(r)






# r_dict = r.json()
# print(r.json())

# print(r_dict['form'])
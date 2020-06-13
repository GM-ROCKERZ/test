import requests

# payload = {'username':'gopal', 'password':'testing'}
r = requests.get('https://httpbin.org/basic-auth/gopal/testing',auth=('gopal','testing'))

# r_dict = r.json()

# print(r_dict['form'])
print(r)

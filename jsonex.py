import json
people_string = '''
{

    "People":[
        {
            "name":"Gopal Mishra",
            "phone":"8867274301",
             "emails":["gpl.msh@gmail.com","gpl31.msh@gmail.com"],
            "has_locense":false

        },
             {
                 "name": "Neha Yadav",
                 "phone": "9893087464",
                 "emails": null,
                 "has_locense": true

             }
    ]
}
'''
data= json.loads(people_string)
# print(type(data['People']))
# print(data['People'])
for person in data['People']:
    del person['phone']

new_string = json.dumps(data,indent=2,sort_keys=True)
print(new_string)

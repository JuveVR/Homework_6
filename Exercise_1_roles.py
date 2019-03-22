import requests


base_url = "http://pulse-rest-testing.herokuapp.com/roles/"
role_dict = {
    "name":"Gogi",
    "type":"detective",
    "book": 177,
    "level": 100500
}

#New role creation
resp_create = requests.post(base_url, data=role_dict)
reg_dict = resp_create.json()
role_id = str(reg_dict["id"]) #Getting new role id

#Check that new role has been created
resp_check = requests.get(base_url+role_id)
role_check = resp_check.json()
if role_check["name"] == role_dict["name"] and resp_check.status_code == 200:
    pass
else:
    raise Exception("The role hasn't been created")

#Check that new role exists in the roles list
list_check = requests.get(base_url)
roles_id = []
for i in list_check.json():
    roles_id.append(i["id"])
if roles_id.count(int(role_id)) == 1:
    pass
else:
    raise Exception("There is no new role in the list")

#Changing roles data
role_dict["type"] = "Senior detective"
role_edit = requests.put(base_url+role_id, data=role_dict)

#Check that roles data has been changed
resp_check = requests.get(base_url+role_id)
if resp_check.json()["type"] == role_dict["type"]:
    pass
else:
    raise Exception("The role hasn't been changed")

# Check that role exists in the roles list with new data
list_check = requests.get(base_url)
roles_id = []
for i in list_check.json():
    if i["id"] == int(role_id):
        if i["type"] == role_dict["type"]:
            pass
        else:
            raise Exception("The role hasn't been changed in the list")
    else:
        pass

requests.delete(base_url+role_id)






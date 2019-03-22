import requests


base_url = "http://pulse-rest-testing.herokuapp.com/books/"
book_dict = {
    "title":"The Moon and Sixpence",
    "author":"Somerset"
}
#New book creation
resp_create = requests.post(base_url, data=book_dict)
reg_dict = resp_create.json()
book_id = str(reg_dict["id"]) #Getting new book id

#Check that new book has been created
resp_check = requests.get(base_url + book_id)
book_check = resp_check.json()
if book_check["title"] == book_dict["title"] and resp_check.status_code == 200:
    pass
else:
    raise Exception("The role hasn't been created")

#Check that new book exists in the books list
list_check = requests.get(base_url)
books_id = []
for i in list_check.json():
    books_id.append(i["id"])
if books_id.count(int(book_id)) == 1:
    pass
else:
    raise Exception("There is no new book in the list")

#Changing books data
book_dict["author"] = "Somerset Moem"
book_edit = requests.put(base_url + book_id, data=book_dict)

#Check that books data has been changed
resp_check = requests.get(base_url + book_id)
if resp_check.json()["author"] == book_dict["author"]:
    pass
else:
    raise Exception("The book hasn't been changed")

# Check that book exists in the books list with new data
list_check = requests.get(base_url)
books_id = []
for i in list_check.json():
    if i["id"] == int(book_id):
        if i["author"] == book_dict["author"]:
            pass
        else:
            raise Exception("The book hasn't been changed in the list")
    else:
        pass

requests.delete(base_url + book_id)

import requests

base_url_book = "http://pulse-rest-testing.herokuapp.com/books/"
base_url_role = "http://pulse-rest-testing.herokuapp.com/roles/"
book_dict = {
    "title": "The Moon and Sixpence",
    "author": "Somerset"
}

role_dict = {
    "name":"Gogi",
    "type":"detective",
    "book": "http://pulse-rest-testing.herokuapp.com/books/6631",
    "level": 100500
}

def add_new_item(base_url, data_dict):
    """
    Create new item
    :param base_url: base API url
    :param data_dict: data of the item (dict)
    :return: new item ID
    """
    resp_create = requests.post(base_url, data=data_dict)
    if resp_create.status_code == 201:
        reg_dict = resp_create.json()
        item_id = str(reg_dict["id"])
        return item_id
    else:
        raise Exception("Item hasn't been added")

def add_item_id(item_dict, item_id, key_value="id"):
    """
    Update item dict with its id
    :return: dict with id value
    """
    item_dict.update({key_value: int(item_id)})
    return item_dict

def compare_dicts(dict1, dict2):
    unmatched = set(dict1.items()) ^ set(dict2.items())
    if len(unmatched) != 0:
        raise Exception("Dicts are not equal")

def check_new_item(base_url, item_id, item_dict):
    """
    Check that new item has been created
    """
    resp_check = requests.get(base_url + item_id)
    item_check = resp_check.json()
    new_item_dict = add_item_id(item_dict, item_id)
    if resp_check.status_code == 200:
        compare_dicts(item_check, new_item_dict)
    else:
        raise Exception("Wrong request")

def check_item_in_list(base_url, item_id, item_dict):
    """
    Check that new item exists in the items list with correct data
    """
    list_check = requests.get(base_url)
    list_str = list_check.json()
    books_id = []
    for i in list_str:
        if i["id"] == int(item_id):
            new_item_dict = add_item_id(item_dict, item_id)
            compare_dicts(i, new_item_dict)
            books_id.append(i["id"])
    if len(books_id) != 1:
        raise Exception("The item is not in the list")

def book_update_and_check(base_url, book_id, item_dict, new_author=book_dict["author"], new_title=book_dict["title"]):
    """
    Change books data and checks changes in the book structure, and in the all books list.
    """
    item_dict["author"], item_dict["title"] = new_author, new_title
    requests.put(base_url + book_id, data=item_dict)
    resp_check = requests.get(base_url + book_id)
    new_item_dict = add_item_id(item_dict, book_id)
    if resp_check.status_code == 200:
        resp = resp_check.json()
        compare_dicts(resp, new_item_dict)
    else:
        raise Exception("Wrong request")
    list_check = requests.get(base_url)
    if list_check.status_code == 200:
        books_id = []
        for i in list_check.json():
            if i["id"] == int(book_id):
                compare_dicts(i, new_item_dict)
                books_id.append(i["id"])
        if len(books_id) != 1:
            raise Exception("Updated book is not in the list")

def role_update_and_check(base_url, role_id, item_dict, new_name=role_dict["name"], new_type=role_dict["type"],
                          new_book=role_dict["book"], new_level=role_dict["level"]):
    """
    Change role data and checks changes in the role structure, and in the all roles list.
    """
    item_dict["name"], item_dict["type"], item_dict["level"], item_dict["book"]= new_name, new_type, new_level, new_book
    requests.put(base_url + role_id, data=item_dict)
    resp_check = requests.get(base_url + role_id)
    new_item_dict = add_item_id(item_dict, role_id)
    if resp_check.status_code == 200:
        resp = resp_check.json()
        compare_dicts(resp, new_item_dict)
    else:
        raise Exception("Wrong request")
    list_check = requests.get(base_url)
    if list_check.status_code == 200:
        roles_id = []
        for i in list_check.json():
            if i["id"] == int(role_id):
                compare_dicts(i, item_dict)
                roles_id.append(i["id"])
        if len(roles_id) != 1:
            raise Exception("Updated book is not in the list")
    else:
        raise Exception("Wrong request status")

def delete_item_finally(base_url, item_id):
    """
    Delete item
    """
    if item_id is not None:
       del_resp = requests.delete(base_url + item_id)
       if del_resp.status_code == 204:
           list_check = requests.get(base_url)
           if list_check.status_code == 200:
               items_id = []
               for i in list_check.json():
                   if i["id"] == int(item_id):
                       items_id.append(i["id"])
               if len(items_id) != 0:
                   raise Exception("Something went wrong. Deleted item is still in the list.")
       else:
           raise Exception("Wrong request status code. Item hasn't been deleted")
    else:
        raise Exception("Item id is None")



if __name__ == "__main__":
    #Manipulations with book
    book_id = add_new_item(base_url_book, book_dict)
    check_new_item(base_url_book, book_id, book_dict)
    check_item_in_list(base_url_book, book_id, book_dict)
    book_update_and_check(base_url_book, book_id, book_dict, "Somerset Moem", "Luna i grosh")
    delete_item_finally(base_url_book, book_id)

    # Manipulations with role
    role_id = add_new_item(base_url_role, role_dict)
    check_new_item(base_url_role, role_id, role_dict)
    check_item_in_list(base_url_role,role_id, role_dict)
    role_update_and_check(base_url_role, role_id, role_dict, "JuveVR", "student")
    delete_item_finally(base_url_role, role_id)

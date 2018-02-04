"""
lab2.py
Swechchha Tiwari
1/30/2018
"""

def squared(num_list):
    """
    square numbers is num_list
    num_list:list of numbers squared
    Returns: list of these numbers squared
    """
    new_list=[]
    for num in num_list:
       sq_num=pow(num,2)
       new_list.append(sq_num)
    return new_list

def check_title(title_list):
    """
    Removes strings in title_list that have numbers aren't title because
    title_list: list of strings
    Returns: list of strings that are title
    """
    new_list=[]
    for s in title_list:
         str_name=s.istitle()
         if str_name == True:
             new_list.append(s)
         else:
             new_list.clear()
             break
    return(new_list)

def restock_inventory(inventory):
    """
    Increases inventory of each item in dictionary by 10
    inventory: a dictionary with:
      key: string that is the name of the inventory item
      value: integer that equals the number of that item currently on hand
    Returns:updated dictionary where each inventory item is restocked
    """
    for k in inventory.keys():
        inventory[k] = inventory[k] + 10
    print(inventory)

def filter_0_items(inventory):
    """
    Removes items that have a value of 0 from a dictionary of inventories
    inventory: dictionary with:
     key:tring that is the name of the inventory item
     value:integer that equals the number of that item currently on hand
    Returns: the same inventory_dict with any item that had 0 quantity removed
    """

    for k,v in inventory.copy().items():
        if inventory[k] == 0:
            inventory.pop(k)
    print(inventory)

def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
    grades: a dictionary of grades with:
    key: string of students name
    value: list of integer grades received in Class
    Returns: dictionary that averages out the grades of each student
    """

    for k in grades.keys():
        new_list = grades[k]
        str_len = len(new_list)
        total = sum(new_list) / str_len
        grades[k] = total
    print(grades)

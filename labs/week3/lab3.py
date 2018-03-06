"""
lab3.py with doctest
Swechchha Tiwari
1/30/2018
"""

def squared(num_list):
    """
    square numbers is num_list
    num_list:list of numbers squared
    Returns: list of these numbers squared

    >>> squared([1, 2, 3])
    [1, 4, 9]
    >>> squared([])
    []
    >>> squared([-1, -2])
    [1, 4]
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

    >>> check_title(['Hello World', 'Hello_world', 'Title'])
    ['Hello World', 'Title']
    >>> check_title(['Hello_World', 'A great 3 Days', 'hello World'])
    ['Hello World']
    >>> check_title(['10, 11, 12'])
    []
    """
    for w_index in range(len(title_list)):
        title_list[w_index] = title_list[w_index].replace('_', ' ')
    return [word for word in title_list if word.istitle()]

def restock_inventory(inventory):
    """
    Increases inventory of each item in dictionary by 10
    inventory: a dictionary with:
      key: string that is the name of the inventory item
      value: integer that equals the number of that item currently on hand
    Returns:updated dictionary where each inventory item is restocked

    >>> restock_inventory({'pencil':10, 'pen':8, 'paper':7})
    {'pencil': 20, 'pen': 18, 'paper': 17}
    >>> restock_inventory({'pencil':0, 'pen':-3, 'paper':-11})
    {'pencil': 10, 'pen': 7, 'paper': -1}
    >>> restock_inventory({'pencil':0.5, 'pen':-3.2, 'paper':11.0})
    {'pencil': 10.5, 'pen': 6.8, 'paper': 21.0}
    """
    for k in inventory.keys():
        inventory[k] = inventory[k] + 10
    return inventory

def filter_0_items(inventory):
    """
    Removes items that have a value of 0 from a dictionary of inventories
    inventory: dictionary with:
     key:string that is the name of the inventory item
     value:integer that equals the number of that item currently on hand
    Returns: the same inventory_dict with any item that had 0 quantity removed

    >>> filter_0_items({'pencil':10, 'pen':8, 'paper':7})
    {'pencil': 10, 'pen': 8, 'paper': 7}
    >>> filter_0_items({'pencil':0, 'pen':-3, 'paper':-11})
    {'pen': -3, 'paper': -11}
    >>> filter_0_items({'pencil':0.5, 'pen':-3.2, 'paper':0.0})
    {'pencil': 0.5, 'pen': -3.2}
    """
    for k,v in inventory.copy().items():
        if inventory[k] == 0:
            inventory.pop(k)
    return inventory

def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
    grades: a dictionary of grades with:
    key: string of students name
    value: list of integer grades received in Class
    Returns: dictionary that averages out the grades of each student

    >>> average_grades({'Michael': [100,78,88,900/10], 'Daniel': [80,95,77,64.0], 'Josh': [99,89,94,66]})
    {'Josh': 87.0, 'Daniel': 79.0, 'Michael': 89.0}
    >>> average_grades({'Michael': [5*20,188 *.5, 88], 'Daniel': [80.5, .15, 66, 64.0], 'Josh': [99 + 1 * -2, 40/.5]})
    {'Josh': 88.5, 'Daniel': 52.6625, 'Michael': 94.0}
    >>> average_grades({'Michael': [78], 'Daniel': [90], 'Josh': [900/-9]})
    {'Josh': -100.0, 'Daniel': 90.0, 'Michael': 78.0}
    """

    for k in grades.keys():
        new_list = grades[k]
        str_len = len(new_list)
        total = float(sum(new_list) / str_len)
        grades[k] = total
    return grades

if __name__ == '__main__':
    import doctest
    doctest.testmod( )

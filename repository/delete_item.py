
def delete_item(name):
    nonlocal items
    items = list(filter(lambda x: x.name != name, items))

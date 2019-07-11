

def find_an_item_by_name(name, get_item_by_name, *args, **kwargs):
    item = get_item_by_name(name, *args, **kwargs)
    return item

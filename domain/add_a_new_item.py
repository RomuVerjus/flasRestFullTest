from domain.item import Item


def add_an_item(name, price, add_item, item_does_exist, *args, **kwargs):
    if item_does_exist(name):
        return None
    else:
        item_to_create = Item(name, price)
        add_item(item_to_create, *args, **kwargs)
        return item_to_create

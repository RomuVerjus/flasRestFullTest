from .items import items


def get_item_by_name(name):
    next(filter(lambda x: x['name'] == name, items), None)

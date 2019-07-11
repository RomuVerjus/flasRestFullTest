from .items import items


def does_item_exist(name):
    return next(filter(lambda x: x.name == name, items), None) is not None

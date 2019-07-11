def suppress_item(name, delete_item, does_item_exist):
    if does_item_exist(name):
        return delete_item(name)
    else:
        return None

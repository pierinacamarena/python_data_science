def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)
    
    print_message_map = {
        str: f"{object} is in the kitchen : {obj_type}",
        list: f"List : {obj_type}",
        tuple: f"Tuple : {obj_type}",
        set: f"Set : {obj_type}",
        dict: f"Dict : {obj_type}",
    }

    type_message = print_message_map.get(obj_type, "Type not found")
    print(type_message)
    return 42
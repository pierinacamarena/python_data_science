import math

def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    
    
    check_type_function_to_message_map = {
        lambda x: x is None: f"Nothing : {obj_type}",
        lambda x: x is False: f"False : {obj_type}",
        lambda x: x == 0 and type(x) is not bool: f"Zero : {obj_type}",
        lambda x: x == '': f"Empty : {obj_type}",
        lambda x: isinstance(x, float) and math.isnan(x): f"Cheese : {obj_type}"
    }
    
    for check, message in check_type_function_to_message_map.items():
        if check(object):
            print(message)
            return 0
    
    print("Type not found")
    return 1
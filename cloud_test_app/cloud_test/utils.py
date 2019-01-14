

def parse_boolean(value):
    if type(value) == bool:
        return value

    if value in ['True', 'true', 'T', 't', '1']:
        return True
    if value in ['False', 'false', 'F', 'f', '0']:
        return False
    return False

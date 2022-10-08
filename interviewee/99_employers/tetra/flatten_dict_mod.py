CONNECTOR='.'



def flatten(elem, name='', out={}):

    # If the Nested key-value
    # pair is of dict type
    if isinstance(elem, dict):

        for a in elem:
            flatten(elem[a], name + a + CONNECTOR, out)

    # If the Nested key-value
    # pair is of list type
    elif isinstance(elem, list): 
        i = 0 
        for a in elem:
            flatten(a, name + '[' + str(i) + '].', out)
            i += 1
    else:
        out[name[:-1]] = elem

def flatten_json(inp_dict):
    name=''
    out={}
    flatten(inp_dict, name, out)
    return out
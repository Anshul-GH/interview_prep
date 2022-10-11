# CONNECTOR = '.'


# def flatten(elem, name='', out={}):

#     # If the Nested key-value
#     # pair is of dict type
#     if isinstance(elem, dict):

#         for a in elem:
#             flatten(elem[a], name + a + CONNECTOR, out)

#     # If the Nested key-value
#     # pair is of list type
#     elif isinstance(elem, list): 
#         i = 0 
#         for a in elem:
#             flatten(a, name + '[' + str(i) + '].', out)
#             i += 1
#     else:
#         out[name[:-1]] = elem


# def flatten_json(inp_dict):
#     name = ''
#     out = {}
#     flatten(inp_dict, name, out)
#     return out


# CONNECTOR = "."

# def flatten_list(inp_lst, output={}):
#     for val in inp_lst:


# def flatten_dict(inp_dict, output={}):
#     for key, val in inp_dict.items():
#         if isinstance(val, dict):
#             prefix = key
#             flatten_dict(val, prefix)
#         elif isinstance(val, list):
#             flatten_list(val)
#         else:
#             output[key] = val



CONNECTOR = '.'

def flatten_dict(inp, pref, out):
    if isinstance(inp, dict):
        for elem in inp:            
            flatten_dict(inp[elem], pref+elem+CONNECTOR, out)
    elif isinstance(inp, list):
        for idx, val in enumerate(inp):
            flatten_dict(val, pref+"["+str(idx)+"]"+CONNECTOR, out)
    else:
        out[pref[:-1]] = inp
   


def parent_method(inp_dict):
    prefix = ""
    output = {}
    flatten_dict(inp_dict, prefix, output)

    return output


if __name__ == "__main__":    
    inp_dict = {
        "a": "aa",
        "b": {
            "bb1": "d",
            "bb2": "d2"
        },
        "c": [
            {
                "cc1": "d"
            },
            {
                "cc1": "d2",
                "cc2": [
                    {
                        "e": "f"
                    }
                ]
            }
        ],
        "g": ["h", "i"]
    }

    flat_json = parent_method(inp_dict)

    print(flat_json)

CONNECTOR = '.'


def flatten_dict(input, prefix, output={}):
    # nested dict
    if isinstance(input, dict):
        for key, val in input.items():
            new_prefix = prefix + key + CONNECTOR
            flatten_dict(val, new_prefix, output)
    elif isinstance(input, list):
        for idx, val in enumerate(input):
            new_prefix = prefix + "["+str(idx)+"]" + CONNECTOR
            flatten_dict(val, new_prefix, output)
    else:
        output[prefix[:-1]] = input


def main(input):
    prefix = ""
    output = {}
    flatten_dict(input, prefix, output)

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
    flat_dict = main(inp_dict)

    print(flat_dict)

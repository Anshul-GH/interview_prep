

# # def flatten_dict(inp_dict, flat_dict={}):

# #     for key, value in inp_dict.items():
# #         if isinstance(value, dict):
# #             flatten_dict(value, flat_dict)
# #         elif isinstance(value, list):
# #             for attrib in value:
# #                 if isinstance(attrib, dict):
# #                     flatten_dict(attrib, flat_dict)
# #                 elif 


# import pandas as pd

# def flatten_dict(inp_dict):
#     df = pd.json_normalize(inp_dict, sep=".")
#     out_dict = df.to_dict(orient="records")[0]
#     print(out_dict)


# if __name__ == "__main__":
#     inp_dict = {
#         "a": "aa",
#         "b": {
#             "bb1": "d",
#             "bb2": "d2"
#         },
#         "c": [
#             {
#                 "cc1": "d"
#             },
#             {
#                 "cc1": "d2",
#                 "cc2": [
#                     {
#                         "e": "f"
#                     }
#                 ]
#             }
#         ],
#         "g": ["h", "i"]
#     }

#     flatten_dict(inp_dict)


from collections.abc import MutableMapping


def yield_elements(mapping, in_key, connector):
    for key, value in mapping.items():
        mod_key = key
        if in_key:
            mod_key = in_key + connector + key
            connector = "."
        if isinstance(value, MutableMapping):
            yield from flatten_dict(value, mod_key, connector).items()
        else:
            yield mod_key, value


def flatten_dict(mapping, in_key=None, connector="."):
    return dict(yield_elements(mapping, in_key, connector))


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

    mod_dict = flatten_dict(inp_dict)
    

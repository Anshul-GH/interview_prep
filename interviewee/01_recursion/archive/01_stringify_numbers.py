# Write a recursive function stringify_numbers that can convert all 
# the numbers in an object containing nested object into strings.

def stringify_numbers(obj):    
    if isinstance(obj, dict):
        keys = obj.keys()
        for key in keys:
            if isinstance(obj[key], dict):
                stringify_numbers(obj[key])
            # elif isinstance(obj[key], int):
            elif type(obj[key]) == int:
                obj[key] = str(obj[key])
            else:
                continue
            
    return obj

if __name__ == '__main__':
    # obj = {
    #     "outer":2,
    #     "obj":{
    #         "inner":2,
    #         "otherObj":{
    #             "superInner":2,
    #             "notANumber":True,
    #             "alsoNotANumber":"yup"
    #         }
    #     }
    # }
    # obj = {
    #     "a":2,
    #     "b":{
    #         "b":2,
    #         "bb":{
    #             "b":3,
    #             "bb":{
    #                 "b":2
    #             }
    #         }
    #     },
    #     "c":{
    #         "c":{
    #             "c":2
    #         },
    #         "cc":"ball",
    #         "ccc":5
    #     },
    #     "d":1,
    #     "e":{
    #         "e":{
    #             "e":2
    #         },
    #         "ee":"car"
    #     }
    # }
    obj = {
        "num":1,
        "test":[
            
        ],
        "date":{
            "val":4,
            "info":{
                "isRight":True,
                "random":66
            }
        }
    }
    # if isinstance(obj, dict):
    #     print(obj.keys())
    print(stringify_numbers(obj))

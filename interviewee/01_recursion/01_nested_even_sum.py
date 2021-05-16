# Write a recursive function nested_even_sum that can return the 
# sum of all the even numbers in an object containing nested object.

def nested_even_sum(obj):
    sum = 0
    if isinstance(obj, dict):
        keys = obj.keys()
        for key in keys:
            if isinstance(obj[key], dict):
                sum = sum + nested_even_sum(obj[key])
            # elif isinstance(obj[key], int):
            elif type(obj[key]) == int:
                if obj[key] % 2 == 0:
                    sum = sum + obj[key]
            else:
                continue
            
    return sum

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
    obj = {
        "a":2,
        "b":{
            "b":2,
            "bb":{
                "b":3,
                "bb":{
                    "b":2
                }
            }
        },
        "c":{
            "c":{
                "c":2
            },
            "cc":"ball",
            "ccc":5
        },
        "d":1,
        "e":{
            "e":{
                "e":2
            },
            "ee":"car"
        }
    }
    # if isinstance(obj, dict):
    #     print(obj.keys())
    print(nested_even_sum(obj))

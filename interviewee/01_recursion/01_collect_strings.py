# Write a recursive function collect_strings that can convert all 
# the numbers in an object containing nested object into strings.

def collect_strings(obj):    
    if isinstance(obj, dict):
        strings = []
        keys = obj.keys()
        for key in keys:
            if isinstance(obj[key], dict):
                strings.extend(collect_strings(obj[key]))
            elif isinstance(obj[key], str):
                strings.append(obj[key])            
            else:
                continue
            
    return strings

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
    # obj = {
    #     "num":1,
    #     "test":[
            
    #     ],
    #     "date":{
    #         "val":4,
    #         "info":{
    #             "isRight":True,
    #             "random":66
    #         }
    #     }
    # }
    # obj = {
    #     "stuff":"foo",
    #     "data":{
    #         "val":{
    #             "thing":{
    #                 "info":"bar",
    #                 "moreInfo":{
    #                 "evenMoreInfo":{
    #                     "weMadeIt":"baz"
    #                 }
    #                 }
    #             }
    #         }
    #     }
    # }
    print(collect_strings(obj))

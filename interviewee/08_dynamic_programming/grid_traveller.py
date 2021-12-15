# Given the traveller is only allowed to move right or down, 
# in how many ways can the traveller reach (m,n) starting from (1,1) 
# where m is number of rows and n is number of columns respectively.

# Recursive (old approach):
# def possible_routes(m, n):
#     if m == 1 and n == 1:
#         return 1
#     elif m == 0 or n == 0:
#         return 0
#     return possible_routes(m-1,n) + possible_routes(m,n-1)

# if __name__ == "__main__":
#     m = int(input("Enter number of rows(m):"))
#     n = int(input("Enter number of columns(n):"))
#     print(possible_routes(m,n))


# Dynamic programming based approach:
def possible_routes(m, n, routes={}):
    if m == 1 and n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    # are the coordinates already have a calculated route
    key = str(m) + ',' + str(n)
    key_inv = str(n) + ',' + str(m)
    if key in routes:
        return routes[key]
    elif key_inv in routes:
        return routes[key_inv]
    else:
        routes[key] = possible_routes(m-1, n, routes) + possible_routes(m, n-1, routes)
        return routes[key]

if __name__ == "__main__":
    m = int(input("Enter number of rows(m):"))
    n = int(input("Enter number of columns(n):"))
    print(possible_routes(m,n))

matrix = [
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[0, 0, 9, 0, 0, 0, 6, 0, 1],
[7, 1, 0, 0, 4, 0, 8, 5, 0],
[2, 0, 5, 3, 0, 7, 4, 1, 6],
[8, 0, 4, 2, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 3, 1, 0, 0],
[0, 8, 2, 6, 0, 0, 3, 0, 5],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[9, 3, 0, 8, 7, 1, 0, 2, 4]
]

def validate_rows(matrix):
    is_valid_sudoku = True
    invalid_lst = []
    for lst in matrix:
        trimmed_lst = [i for i in lst if i != 0]
        if 0 not in lst:
            if len(trimmed_lst) != len(list(set(lst))):
                is_valid_sudoku = False
                invalid_lst = lst
                break
        elif len(trimmed_lst) != len(list(set(lst)))-1:
                is_valid_sudoku = False
                invalid_lst = lst
                break
    return is_valid_sudoku, invalid_lst


# is_valid_sudoku = True

# raw solution
# # validate rows
# for lst in matrix:
#     trimmed_lst = [i for i in lst if i != 0]
#     if len(trimmed_lst) != len(list(set(lst))):
#         is_valid_sudoku = False
#         break

is_valid_sudoku, invalid_lst = validate_rows(matrix)

print(is_valid_sudoku)
print(invalid_lst)

if is_valid_sudoku:
    # transpose the matrix
    # new_matrix = [[0]*len(matrix[0])]
    # new_matrix = [0]*len(new_matrix)]

    # for i in range(len(matrix)):
    #     new_matrix = new_matrix[i].append([])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix
            matrix[j][i] = matrix[i][j]

    print(matrix)
    # is_valid_sudoku, invalid_lst = validate_rows(matrix)
    # print(is_valid_sudoku)
    # print(invalid_lst)

# if is_valid_sudoku:
#     lst = []
#     sum = 0
    
#     x_counter = 0
#     y_counter = 0

#     x_shift = 0
#     y_shift = 0
#     # while x_counter < x_shift + 3:
#     #     for i in range(3):
#     while x_counter < 3 and y_counter < 3:
#         for i in range(x_counter*3, x_counter*3 + 3):            
#             for j in range(y_counter*3, y_counter*3 + 3):
#                 lst.append(matrix[i][j])
        
#         y_counter += 1
#         x_counter += 1

#         trimmed_lst = [i for i in lst if i != 0]
#         if len(trimmed_lst) != len(list(set(lst))):
#             is_valid_sudoku = False
#             break















class SodukuValidator:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def get_rows(self) -> [list]:
        for row in matrix:
            return self.matrix

    def get_cols(self) -> [list]:
        pass

    def get_3_by_3s(self) -> [list]:
        pass

    def validate(self) -> bool:
        pass


# obj = SodukuValidator(matrix)


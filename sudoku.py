
def checker(arr, x, y):
    ruleout = []
    sub_x, sub_y = x // 3, y // 3
#check row
    for n in range(9):
        num = arr[x][n]
        if isinstance(num, int) and num not in ruleout:
            ruleout.append(num)
            
#check column
    for n in range(9):
        num = arr[n][y]
        if isinstance(num, int) and num not in ruleout:
            ruleout.append(num)
#check subsection
    for row in range(sub_x * 3, (sub_x + 1) * 3):
        for col in range(sub_y * 3, (sub_y + 1) * 3):
            num = arr[row][col]
            if isinstance(num, int) and num not in ruleout:
                ruleout.append(num)
        options = set(possible)-set(ruleout)
    if len(options) == 1:
        arr[x][y] = list(options)[0]


def render_board(arr):
    for x, row in enumerate(arr):
        for y, num in enumerate(row):
            print(num, end=" ") 
            if y == 2 or y == 5:
                print("|", end=" ")
        print("")
        if x == 2 or x == 5:
            print("------+-------+------")


# arr = [["."]*9 for i in range(9)]
arr = [[4, 9, 2, 6, ".", ".", ".", ".", 1], 
 [".", ".", ".", ".", ".", ".", 7, ".", 8], 
 [".", ".", 6, 3, 1, 5, ".", ".", "."], 
 [6, ".", 5, 2, 3, ".", 8, ".", "."], 
 [1, ".", 4, ".", ".", ".", ".", 7, 2], 
 [".", ".", ".", 7, 5, 1, ".", 3, "."], 
 [8, ".", ".", 1, 6, 7, ".", 2, "."], 
 [2, 1, ".", 5, ".", ".", ".", 4, "."], 
 [".", ".", 7, ".", 2, ".", 1, 8, 3]]
 
possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("input!")

render_board(arr)

while any("." in i for i in arr):
    for x, row in enumerate(arr):
        for y, num in enumerate(row):
            if arr[x][y] == ".":
                checker(arr, x, y)


print("output!")

render_board(arr)

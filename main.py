def matrix_amount_of_rects(matrix):
    a = len(matrix)
    b = len(matrix[0])
    rects = 0

    dp = [[0]*b for _ in range(a)]
    
    for i in range(a):
        for j in range(b):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    )
                rects += dp[i][j]
    # print()
    # for row in dp:
    #     print(row)
    return rects

def main():
    import random
    a, b = map(int, input().split())
    matrix = [[random.randint(0,1) for _ in range(b)] for _ in range(a)]
    for row in matrix:
        print(row)
    print(matrix_amount_of_rects(matrix))

if __name__ == "__main__":
    main()

# import random

# # Matrix create & print
# n = int(input("Matrix size: "))
# matrix = [[random.randint(0,1) for _ in range(n)] for _ in range(n)]
# for i in matrix: print(i)

# # The amount of rectangles
# rects = 0
# for i in matrix:
#     for j in i: rects += j
# for x in range(1, n):
#     for y in range((n-x)**2):
#         j1, j2, temp = 0, 0, 0

#         col_shift = y % (n - x)
#         row_shift = y // (n - x)

#         for i in range(col_shift, x+1 + col_shift):
#             for j in range(0 + j2 + row_shift, x + 1 + j2 + row_shift):
#                 if matrix[i][j] == 1:
#                     temp += 1
#             j1 += 1
#             if j1 == x + 1:
#                 j1 = 0
#                 j2 += 1
#         if temp == (x +1 ) ** 2:
#             rects += 1
# print(rects)

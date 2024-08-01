A = [[1, 2],
     [3, 4]]
B = [[3, 4],
     [1, 2]]
rows_A = len(A)
cols_A = len(A[0])
rows_B = len(B)
cols_B = len(B[0])
result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
for i in range(rows_A):
    for j in range(cols_B):
        for k in range(cols_A):  
            result[i][j] += A[i][k] * B[k][j]
for r in result:
    print(r)
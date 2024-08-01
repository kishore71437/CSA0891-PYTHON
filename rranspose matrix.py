matrix=[[4,6,7,8],
        [3,7,2,7],
        [7,3,7,5]]
rows=len(matrix)
cols=len(matrix[0])
transpose=[[0 for _ in range(rows)] for _in range(cols)]
for i in range(rows):
    for j in range (cols):
        transpose[j][i]=matrix[i][j]
        for row in transpose:
            print(row)ś
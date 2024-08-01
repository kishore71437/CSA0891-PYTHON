a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
n=len(a)
rows_sum=[0]*n
cols_sum=[0]*n
primary_diagonal_sum=0
secondary_diagonal_sum=0
for i in range(n):
    for j in range(n):
        rows_sum[i] +=a[i][j]
        cols_sum[j] +=a[i][j]
        if i==j:
            primary_diagonal_sum +=a[i][j]
            if i+j==n-1:
                secondary_diagonal_sum +=a[i][j]
print(f"Row sums:",rows_sum)
print(f"cols sum :",cols_sum)
print(f"primary_diagonal sum :",primary_diagonal_sum)
print(f"secondary diagonal sum :",secondary_diagonal_sum)
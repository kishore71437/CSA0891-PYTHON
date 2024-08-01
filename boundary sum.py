a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
rows=len(a)
cols=len(a)
boundary_sum =0
for j in range(cols):
    boundary_sum +=a[j][0]
    if rows>1:
        boundary_sum +=a[rows-1][j]
for i in range(1,rows-1):
    boundary_sum +=a[i][0]
    boundary_sum +=a[j][cols-1] 
print("Sum of boundary elements :",boundary_sum)       


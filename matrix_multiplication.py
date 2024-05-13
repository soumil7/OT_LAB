def multiply(A, B): 
    r1 = len(A)
    c1 = len(A[0]) 
    r2 = len(B)
    c2 = len(B[0]) 
    if c1 != r2: 
        print("Cannot Be Multiplied")
        exit()
    res = [[0] * c2 for i in range(r1)]
    for i in range(r1): 
        for j in range(c2): 
            for k in range(c1):
                res[i][j] += A[i][k] * B[k][j] 
    return res 

A = [[1, 2, 3],
     [4, 5, 6]] 
B = [[10, 11],
     [20, 21],
     [30, 31]] 
res = multiply(A, B)
print(res)
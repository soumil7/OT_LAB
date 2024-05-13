def min_cost_path(graph):
    path = []
    row = len(graph)
    col = len(graph[0]) 
    dp = [[0] * col for _ in range(row)]  # Corrected syntax here
    dp[0][0] = graph[0][0] 
    for i in range(1, row): 
        dp[i][0] = dp[i-1][0] + graph[i][0] 
    for j in range(1, col): 
        dp[0][j] = dp[0][j-1] + graph[0][j] 
    for i in range(1, row): 
        for j in range(1, col): 
            dp[i][j] = graph[i][j] + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
            print("Dynamic Program:", dp)
    i = row-1 
    j = col-1 
    while i > 0 and j > 0:
        path.append((i, j))
        if i == 0:
            j -= 1
        elif j == 0: 
            i -= 1
        else:
            if dp[i-1][j] < dp[i][j-1] and dp[i-1][j] < dp[i-1][j-1]:
                i -= 1
            elif dp[i][j-1] < dp[i-1][j-1] and dp[i][j-1] < dp[i][j-1]:
                j -= 1
            else:
                i -= 1
                j -= 1
    path.append((0, 0))
    path.reverse()
    return dp[row-1][col-1], path
        
        
cost_grid = [[1, 3, 1],
             [2, 4, 2],
             [5, 1, 1]]
cost, path = min_cost_path(cost_grid)
print("Cost:", cost) 
print("Path:", path)

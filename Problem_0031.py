def optimal_bst(keys, freq):
    n = len(keys)
    
    
    dp = [[0 for _ in range(n)] for _ in range(n)]
    

    for i in range(n):
        dp[i][i] = freq[i]
    
    
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            dp[i][j] = float('inf')
            
           
            for r in range(i, j + 1):
               
                cost = 0
                if r > i:
                    cost += dp[i][r - 1]
                if r < j:
                    cost += dp[r + 1][j]
                cost += sum(freq[i:j + 1])
                
                if cost < dp[i][j]:
                    dp[i][j] = cost
    
    return dp[0][n - 1]


keys = [10, 20, 30]
freq = [3, 2, 5]
print(optimal_bst(keys, freq)) 
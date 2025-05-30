def min_palindrome_partition(s: str) -> int:
    n = len(s)
    # Tabla para precomputar palíndromos
    is_pal = [[False] * n for _ in range(n)]
    
    for i in range(n):
        is_pal[i][i] = True  # todos los caracteres individuales son palíndromos
    
    for length in range(2, n+1):  # longitud de subcadena
        for start in range(n-length+1):
            end = start + length - 1
            if s[start] == s[end]:
                if length == 2:
                    is_pal[start][end] = True
                else:
                    is_pal[start][end] = is_pal[start+1][end-1]
    
    dp = [float('inf')] * n
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 1
        else:
            for j in range(1, i+1):
                if is_pal[j][i]:
                    dp[i] = min(dp[i], dp[j-1] + 1)
    return dp[n-1]

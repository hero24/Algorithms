"""
"Mathematics is the queen of science,
and arithmetic is the queen of mathematics."
 ~ Carl Friedrich Gauss.
"""
def gauss(a, x):
    for i in range(len(a)):
        maxv = i
        for j in range(i+1, len(a)):
            if abs(a[j][i]) > abs(a[maxv][i]):
                maxv = j
        for j in range(i, len(a)+1):
            tmp = a[i][j]
            a[i][j] = a[maxv][i]
            a[maxv][j] = tmp
        if a[i][i] == 0:
            return False
        for j in range(i+1, len(a)):
            for k in range(len(a), i, -1):
                a[j][k] = a[j][k]-a[i][k] * a[j][i] / a[i][i]
    for i in range(len(a)-1,-1,-1):
        tmp = 0
        for j in range(i+1, len(a)):
            tmp = tmp + a[i][j] * x[j]
        x[i] = (a[i][len(a)]-tmp) / a[i][i]
    return True
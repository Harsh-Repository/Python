import math

def findPairsWithPerfectSquareProduct(arr):
    result = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            product = arr[i] * arr[j]
            if isPerfectSquare(product):
                result.append([arr[i], arr[j]])

    return result

def isPerfectSquare(num):
    sqrt = math.sqrt(num)
    return sqrt == int(sqrt)

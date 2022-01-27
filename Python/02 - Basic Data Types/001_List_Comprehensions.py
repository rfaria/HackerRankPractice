# Problem: https://www.hackerrank.com/challenges/list-comprehensions/problem

def naive(x, y, z, n):
    i = j = k = 0
    all_permutations = []

    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    all_permutations.append([i, j, k])
    
    return all_permutations
    
    
def optimized(x, y, z, n):
    pass

    
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = naive(x,y,z,n)
    
    print(result)

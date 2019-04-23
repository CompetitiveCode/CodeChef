# Answer to Puppy and Sum
# https://www.codechef.com/problems/PPSUM


def sumval(n):
    return (n*(n+1))//2


for _ in range(int(input())):
    d, n = map(int, input().split())
    result = n
    for i in range(d):
        result = sumval(result)
    print(result)

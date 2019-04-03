#Answer to Ada School - https://www.codechef.com/problems/ADASCOOL

for _ in range(int(input())):
    n,m = map(int, input().split())
    print('NO' if n * m % 2 != 0 else 'YES')
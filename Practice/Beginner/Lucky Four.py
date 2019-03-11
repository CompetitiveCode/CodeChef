#Answer to Lucky Four - https://www.codechef.com/problems/LUCKFOUR

for _ in range(int(input())):
    count = 0
    for i in input():
        if i == '4':
            count += 1
    print(count)
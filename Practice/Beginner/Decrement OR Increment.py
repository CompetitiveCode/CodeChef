#Answer to Decrement OR Increment - https://www.codechef.com/problems/DECINC

a = int(input())
if a % 4 == 0:
    print(a+1)
else:
    print(a-1)
# Answer to Mahasena
# https://www.codechef.com/problems/AMR15A


n = int(input())
arr = map(int, input().split())
even, odd = 0, 0
for i in arr:
    if i%2 == 0:
        even += 1
    else:
        odd += 1
print('READY FOR BATTLE' if even > odd else 'NOT READY')

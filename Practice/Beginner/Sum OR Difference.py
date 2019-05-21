# Answer to Sum OR Difference
# https://www.codechef.com/problems/DIFFSUM


n1, n2 = int(input()), int(input())
print(n1-n2 if n1-n2 > 0 else n1+n2)

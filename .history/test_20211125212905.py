columnNumber = 1
n = 0
ans = []
num = columnNumber
while num > 26**n:
    num -= 26**n
    n += 1

n -= 1
if num == 0:
    index = num // 26**i

for i in range(n, -1, -1):
    index = num // 26**i
    # print(num,n,index)
    ans.append(chr(ord("A") + index))
    num -= index * (26**i)
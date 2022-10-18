a = int(input())
minus = False
ans = []
if a < 0:
    minus = True
    a *= -1
while a >= 1:
    if a % 3 == 0 or a % 3 == 1:
        ans.append(str(a % 3))
        a = a // 3
    else:
        a = (a // 3) + 1
        ans.append(-1)
ans.reverse()
if minus is False:
    print(*ans)
else:
    for x in range(len(ans)):
        g = int(ans[x])
        ans[x] = g * -1
    print(*ans)

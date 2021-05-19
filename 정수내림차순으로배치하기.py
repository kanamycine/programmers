n = int(input())
answer = ''
s = str(n)
lst = []
for i in range(len(s)):
    lst.append(s[i])
lst.sort()
lst.reverse()
for i in range(len(lst)):
    answer += lst[i]

print(answer)

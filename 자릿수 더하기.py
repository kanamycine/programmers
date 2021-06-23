n = 123
strings = str(n)
answer = 0
for i in range(len(strings)):
    answer += int(strings[i])
print(answer)
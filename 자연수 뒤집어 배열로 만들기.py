n = 12345
answer = []
strings = str(n)
rstrings = strings[::-1]
for i in range(len(rstrings)):
    answer.append(int(rstrings[i]))


print(answer)
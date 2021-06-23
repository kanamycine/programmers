num = 6
count = 0
while count < 501:
    if num == 1 :
        break
    elif num % 2 == 0:
        num = num // 2
        count += 1
    else : 
        num = (num*3) + 1
        count += 1
answer = count
if answer == 501:
    answer = -1
print(answer)
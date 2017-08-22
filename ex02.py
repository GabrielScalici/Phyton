num = input('Digite um numero de 1 a 100\n')

if num < 1:
    num = false
elif num > 100:
    num = false
else:
    for i in range(101):
        if i == 0:
            continue
        else:
            total = num % i
        if i != num:
            if total == 0:
                num = false
                break
            else:
                continue
        else:
            num = true

print(num)

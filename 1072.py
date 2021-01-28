i = int(input())
n=0
dentro = 0
fora = 0
while n<i:
    valor = float(input())
    if valor >= 10 and valor <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1
    n= n+1

print(f'{dentro} in')
print(f'{fora} out')
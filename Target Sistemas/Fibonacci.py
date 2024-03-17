fibo =[]

n = int(input('Digite um número: '))
t1 = 0
t2 = 1
fibo.append(t1)
fibo.append(t2)

print(f'{t1} → {t2} ', end =  '')
cont = 3

while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end=' ')
    fibo.append(t3)
    cont += 1
    t1 = t2 
    t2 = t3
    if t3 > n:
        break 

print('')

if n in fibo:
    print('Seu nº PERTENCE a sequência de fibonnaci')
elif n not in fibo:
    print('Seu nº NÃO PERTENCE a sequência de fibonnaci')


# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?

n = int(input("Введите количество журавликов: "))

a = n // 3 // 2
b = a
c = ((a + b) * 2)

print(f'Катя сделала журавликов: {c}')
print(f'Петя сделала журавликов: {a}')
print(f'Сережа сделала журавликов: {b}')
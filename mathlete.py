print('.: MATHLETE :.')
print('--------------')
answers = 0
total = 0

while True:
    svar = input('> ')
    if svar == 'exit':
        break
    try:
        svar = float(svar)
        answers += 1
        total += svar
    except ValueError:
        print('Invalid number!')
        continue

try:
    mean_value = total/answers
    print('--------------')
    print('Cardinaliy:', answers)
    print('Sum:', total)
    print('Mean Value:', mean_value)
except ZeroDivisionError:
    print('No Valid input')
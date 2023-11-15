while True:
   n = input('что делаем?')
   if n == 'e':
       break
    if n in deysvia:
        q = int(input('первое число'))
        w = int(input('второе число'))
        if n =='+':
            print(f'{q}+{w}={q + w}')
        elif n =='-':
            print(f'{q}-{w}={q - w}')
        elif n ==('/'):
            print(f'{q}/{w}={q / w}')
        elif n ==('*'):
            print(f'{q}*{w}={q * w}')
    else:
         print('фигнея')



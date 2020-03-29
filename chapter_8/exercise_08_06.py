lst = []
while True:
    num = input('enter a number:')
    if num == 'done':
        print('Maximum:', max(lst))
        print('Minimum:', min(lst))
        quit()
    num_i = int(num)
    lst.append(num_i)

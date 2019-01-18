f_name = 'registration3.txt'


L = {i: line[0:] for i, line in enumerate(open(f_name, encoding='UTF-8'))}
print(L)
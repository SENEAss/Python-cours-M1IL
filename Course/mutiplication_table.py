n = int((input("Which table would you like te display ? ")))
        
table = []
for i in range(1,11):
    if (i*n) % 3 == 0: 
        table.append(f'{i*n}*')
    else:
        table.append(i*n)

print(table)
number = [8, 7, 11, 7, 2, 10, 5, 8]
new_number = []
for i in number:
    if i not in new_number:
        new_number.append(i)
# new_number.sort()
# print(new_number)
print(sorted(new_number))
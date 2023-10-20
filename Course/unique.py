number = [8, 7, 11, 7, 2, 10, 5, 8]
new_number = [] #initialisation d'une nouvelle liste
for i in number:
    if i not in new_number:
        new_number.append(i) #ici i s'agit de vérifier le nombre qu'on veut ajouter sur la nouvelle liste existe déja
# new_number.sort()
# print(new_number)
print(sorted(new_number))
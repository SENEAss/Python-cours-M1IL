"""Ecrire une fonction qui prend en entrée une vitesse en km/h et la convertit en m/h sachant que 1 mile = 1.609km"""
Vitesse_en_km = float(input("veuillez entrer la vitesse que vous voulez convertir : "))
KMH_MH = 1.609  #conventipon de nommage pour les constantes est de tout mettre en majuscule
result = round(Vitesse_en_km/KMH_MH, 2)
print("la vitesse en m/h est : ", result) 
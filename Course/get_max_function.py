# Définition de la fonction get_max
def get_max(numbers:list[float]) -> float:
    get_max = numbers[0]
    for i in range(1, len(numbers)):
        if list[i] > get_max:
            get_max = list[i]
    return get_max
            
    
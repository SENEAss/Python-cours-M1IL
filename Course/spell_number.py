    
phone = input("Enter your phine number : ")
result = "" #dictionnaire de resultat
digits_mapping = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

for digits in phone:
    result += digits_mapping.get(digits, "Character not mapped") + ' '
    
print(result)
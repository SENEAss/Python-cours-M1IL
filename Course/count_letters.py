text = "Ce qui ne te tue pas te rend plus fort" 

alphabet = "abcdefghijklmnopqrestuvwxyz"
result = {}

for char in alphabet:
    result[char] = text.count(char)
    
print(result)
#!/usr/bin/env python3

indication_valeur1 = ord("a")  # pour savoir quelle 
indication_valeur2 = ord("z")  # valeur numérique = quelle lettre

# print(f"{indication_valeur1} et {indication_valeur2}") 
# Résultat : a = 97 et z = 122 
 
for i in range(97, 123):
    print(chr(i), end="")
print("\n")
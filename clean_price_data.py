# liste = ["boo", "boo", "boo"]
# dico = { k+1:v*(k+1) for k, v in enumerate(liste)}
# print(dico)

# list_prenom = ["Léa", "BOO", "Clémi"]
# list_age = [19, 23, 70]

# dico2 = { prenom:age for prenom, age in zip(list_prenom, list_age) if age < 50}
# print(dico2)

# dico3 = { k:k**2 for k in range (21)}
# print (dico3)

# #any() #au moins un élément de la liste = True 
# #all() #tous les éléments de la liste = True

# with open ("test.txt", mode="w") as f :
#     for i in range (10): 
#         f.write(f"{i}^2 = {i**2} \n")
    
#     # l = [elm for elm in f.readlines()]

# with open ("test.txt", mode="r") as f :
#     l = [elm for elm in f.read().splitlines()]
#     print (l)

import glob 

file_names = glob.glob("*.txt")
dico = {}

for file in file_names:
    with open (file, "r") as f:
        dico[file] = f.read().splitlines()

print (dico)
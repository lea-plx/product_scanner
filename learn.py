import numpy as np 
import matplotlib.pyplot as plt


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

# import glob 

# file_names = glob.glob("*.txt")
# dico = {}

# for file in file_names:
#     with open (file, "r") as f:
#         dico[file] = f.read().splitlines()

# print (dico)


# def initialisation (m, n):
#     tab = np.random.randn(m,n)
#     init1 = np.ones((m, 1))
#     concatenate = np.concatenate((tab,init1), axis=1)
#     return concatenate

# result = initialisation(3,4)
# print (result)

# from scipy import misc 
# face = misc.face(gray=True)

# l = face.shape[0]
# c = face.shape[1]

# zoom = face[l//4:-l//4, c//4:-c//4]
# zoom[zoom>150]=255
# zoom[zoom<100]=0
# plt.imshow(zoom, cmap=plt.cm.gray)
# plt.show()

# np.random.seed(0)
# A = np.random.randint(0,100, [10,5])
# moyenne = A.mean(axis=0)
# ecart_type = A.std(axis=0)

# print ((A-A.mean(axis=0))/A.std(axis=0))

# for col in range (A.shape[1]):
#     A[:,col] = (A[:,col]-moyenne[col])/ecart_type[col]

# print(A.mean(axis=0))
# print(A.std(axis=0))


dataset = {f"experience {i}":np.random.randn(100) for i in range (4)}

def graphique (dataset) :
    plt.figure()
    for experience, index in zip(dataset.keys(), range(1, len(dataset.keys())+1)):
        plt.subplot(2,2,index)
        plt.plot(dataset[experience])
        plt.title(experience)

    plt.show()


graphique(dataset=dataset)
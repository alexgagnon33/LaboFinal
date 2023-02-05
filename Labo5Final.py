import random

class Animal:
    def __init__(self, alimentation, nom, type):
        self.alimentation = alimentation
        self.nom = nom
        self.type = type

Dragon = Animal("1", "Dragon", "Carnivore")
Cheval = Animal("2", "Cheval", "Herbivore")
Panda = Animal("3", "Panda", "Omnivore")
Wapiti = Animal("3", "Wapiti", "Omnivore")
Gnous = Animal("2", "Gnous", "Herbivore")
Lynx = Animal("1", "Lynx", "Carnivore")
Ours = Animal("3", "Ours", "Omnivore")
Bison = Animal("2", "Bison", "Herbivore")
Loup = Animal("1", "Loup", "Carnivore")
Cochon = Animal("3", "Cochon", "Omnivore")

animaux_liste = [Dragon, Cheval, Panda, Wapiti, Gnous, Lynx, Ours, Bison, Loup, Cochon]

def Question():
    while True:
        print("Choisez le bon type d'animaux dans la liste")
        print("Voir ce que mange tous les animaux dans la liste")
        réponse_utilisateur = input("Choisisez une question: ")
        if réponse_utilisateur == "1":
            Question1()
        elif réponse_utilisateur == "2":
            Question2()
        else:
            print("Votre réponse est mauvaise, choisisez une autre réponse")

def Question1():
        animal_random = random.choice(animaux_liste)
        réponse_question1 = input("Quel type d'animaux est le/la/l' " + animal_random.nom)
        if réponse_question1 == animal_random.type:
            print("Bonne réponse")
        else:
            print("Mauvaise réponse")

def Question2():
    for animal_random in animaux_liste:
        if animal_random.alimentation == "1":
            print("Animal    Alimentation")
            print(animal_random.nom + "  |  " + "Viande")
        elif animal_random.alimentation == "2":
            print("Animal    Alimentation")
            print(animal_random.nom + "  |  " + "Plante")
        elif animal_random.alimentation == "3":
            print("Animal    Alimentation")
            print(animal_random.nom + "  |  " + "Viande et Plante")

Question()
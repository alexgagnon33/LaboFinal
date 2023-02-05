
#Étape 1
def donnee_carte():
        trefle = ["♣ 1", "♣ 2", "♣ 3", "♣ 4", "♣ 5", "♣ 6", "♣ 7", "♣ 8", "♣ 9", "♣ 10", "♣ 11", "♣ 12", "♣ 13"]
        coeur = ["♥ 1", "♥ 2", "♥ 3", "♥ 4", "♥ 5", "♥ 6", "♥ 7", "♥ 8", "♥ 9", "♥ 10", "♥ 11", "♥ 12", "♥ 13"]
        pique = ["♠ 1", "♠ 2", "♠ 3", "♠ 4", "♠ 5", "♠ 6", "♠ 7", "♠ 8", "♠ 9", "♠ 10", "♠ 11", "♠ 12", "♠ 13"]
        carreau = ["♦ 1", "♦ 2", "♦ 3", "♦ 4", "♦ 5", "♦ 6", "♦ 7", "♦ 8", "♦ 9", "♦ 10", "♦ 11", "♦ 12", "♦ 13"]

        carte = trefle + coeur + pique + carreau

        return carte

#Étape 3
#Pour réussir à choisir la séquence suivante avec le paramètre step: https://pythonexamples.org/python-for-i-in-range/
def Afficher_etat(carte):
        for i in range(0, 52, 13):
            print(carte[i:i+13])

#Étape 4
def Brassage_inter_coupe(carte):

        half1 = carte[:26]
        half2 = carte[26:]

        carte = [item for sublist in zip(half1, half2) for item in sublist]

        return carte

#Étape 5
#Pour mieux comprendre sur les cartes et les prob https://stackoverflow.com/questions/6007881/what-does-the-0x-syntax-do-in-python#:~:text=This%20is%20because%20of%20the%20fact%20that%20lists,cell%202%20to%20reference%20the%20newly%20computed%20value.
#Puis https://stackoverflow.com/questions/58608799/how-to-shuffle-a-deck-of-cards-in-python
def Brassage_paquet(carte):

        liste_carte = []
        groupe_carte = 4

        for i in range (0, len(carte), groupe_carte):
            liste_carte.append(carte[i:i+groupe_carte])

        x = liste_carte

        carte = (x[6], x[0], x[2], x[12], x[1], x[3], x[10], x[5], x[7], x[4], x[11], x[9], x[8])
        return [item for sublist in carte for item in sublist]

#Étape 6
def Sauvegarde(carte):
        with open("cards.txt", "w", encoding="UTF-8") as f:
            for i in range(0, 52, 13):
                f.write(" ".join(carte[i:i+13]) + "\n")

#Étape 2
def menu_carte(carte):
        while True:
            print("1 - Afficher l'état du jeu de carte")
            print("2 - Effectuer un brassage inter-coupé")
            print("3 - Effectuer un brassage par paquets")
            print("4 - Sauvegarder l'état final dans un fichier")
            choix_utilisateur = int(input("Voici les choix disponibles: "))

            if choix_utilisateur == 1:
                Afficher_etat(carte)

            elif choix_utilisateur == 2:
                carte = Brassage_inter_coupe(carte)

            elif choix_utilisateur == 3:
                carte = Brassage_paquet(carte)

            elif choix_utilisateur == 4:
                Sauvegarde(carte)
                break

            else:
                print("Choix non valide, veuillez sélectionner un choix disponible.")

carte = donnee_carte()
menu_carte(carte)
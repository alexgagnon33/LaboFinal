#Problème 1
def info_eleve():
    nom_eleve = "John Doe"
    num_eleve = 123456

    def menu_eleve():
        print("[1] Votre nom")
        print("[2] Votre numero etudiant")

    menu_eleve()
    choix_eleve = int(input("Entrer votre choix: "))
    if choix_eleve == 1:
        print(nom_eleve)
    elif choix_eleve == 2:
        print(num_eleve)
    else:
        print("Le choix est invalide")

#Problème 2

def nb_equation():
    base = 2
    exposant = 3

    if base >= 0 and exposant >= 0:
        print("La base et l'exposant sont positifs")
    else:
        print("La base ou l'exposant est negatif")

    return pow(base, exposant)

#Problème 3

def nb_division():
    entier = int(input("Ecriver un nombre entier: "))

    division_2 = False
    division_3 = False

    if (entier % 3) == 0 and (entier % 2) == 0:
        division_2 = True
        division_3 = True

    if division_2 and division_3:

        print("Votre nombre entier est divisible par 2 et par 3")

    else:
        print("Votre nombre entier n'est pas divisible par 2 ou par 3")

#Problème 4

def age_specific():

    annee_naissance = int(input("Entrer votre annee de fete: "))
    
    add_annee = annee_naissance + 50

    print(f"Vous avez eu ou aura 50 ans le {add_annee}")

#Problème 5

def mul_div():
    nb1 = 2
    nb2 = 3
    nb3 = 4

    def mul(nb1, nb2):
        return nb1 * nb2

    def div(nb1, nb2, nb3):
        return (nb1 * nb2) / nb3

    print(f"Multiplication: {mul(nb1, nb2):.3f} Division: {div(nb1, nb2, nb3):.3f}")

#Problème 6

def preference_utilisateur():

    plat_prefere = input("Quel est votre plat prefere: ")
    pays_prefere = input("Quel est votre pays prefere: ")
    annee_future = int(input("Ecriver une annee future: "))

    print(f"Vous aurez l'opportunite de manger {plat_prefere}, lorsque vous visiterez {pays_prefere} en {annee_future}")

info_eleve()
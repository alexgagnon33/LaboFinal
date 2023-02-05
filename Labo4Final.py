import string
import random

# Step 1: Login Verification
database = [["1234", "voiture1", 100, 1000, 10000, 1.8],
            ["3456", "chat123", 150, 2000, 25000, 3],
            ["3333", "1234", 5, 100, 1000, 15],
            ["0000", "admin", 0, 0, 0, 0]]


Base = " " + string.punctuation + string.digits + string.ascii_letters
Base = (list(Base))
Random_Base = Base.copy()
random.shuffle(Random_Base)

#Encryptage
#https://www.youtube.com/watch?v=vsLBErLWBhA&ab_channel=BroCode pour avoir une base https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
encryptage_database = []
for item in database:
    encryptage_item = []
    for element in item:
        if isinstance(element, str):
            encryptage_element = ""
            for letter in element:
                index = Base.index(letter)
                encryptage_element += Random_Base[index]
            encryptage_item.append(encryptage_element)
        else:
            encryptage_item.append(element)
    encryptage_database.append(encryptage_item)

with open("bdx.txt", "w") as file:
    for item in encryptage_database:
        file.write(str(item) + "\n")

#Décryptage
decryptage_database = []
with open("bdx.txt", "r") as file:
    for line in file:
        decryptage_item = []
        item = eval(line)
        for element in item:
            if isinstance(element, str):
                Décryptage_element = ""
                for letter in element:
                    index = Random_Base.index(letter)
                    Décryptage_element += Base[index]
                decryptage_item.append(Décryptage_element)
            else:
                decryptage_item.append(element)
        decryptage_database.append(decryptage_item)

print("Database original:", database)
print("Database décrypter:", decryptage_database)
if database == decryptage_database:
    print("La database a été encrypter et décrypter.")
else:
    print("Le décryptage n'a pas réussi, il n'est pas le même que la database original.")
# Step 2: Choose Account
print("Choisir un compte suivant:")
print("1) Cheque")
print("2) Épargne")
print("3) Placement")

choix_utilisateur = int(input("Entrer un choix des comptes: "))
type_compte = ["Cheque", "Épargne", "Placement"]

# Step 3: Choose Operation
while True:
    print("Choisir une action à faire:")
    print("1) Faire un dépot")
    print("2) Faire un retrait")
    if choix_utilisateur == 3:
        print("3) Voir le retour d'investissement")
    print("4) Fermer le compte")
    
    choix_utilisateur1 = int(input("Entrer un choix des actions à faire: "))
    
    if choix_utilisateur1 == 1:
        deposit_amount = int(input("Entrer un dépot à mettre: "))
        current_account = database[choix_utilisateur - 1] 
        current_account[2] += deposit_amount
        print(f"Votre {type_compte[choix_utilisateur - 1]} compte a ${current_account[2]}")
    elif choix_utilisateur1 == 2:
        withdrawal_amount = int(input("Enter withdrawal amount: "))
        if current_account[choix_utilisateur] - withdrawal_amount < 0:
            print(f"Insufficient funds in your {type_compte[choix_utilisateur - 1]} account.")
        else:
            current_account[choix_utilisateur] -= withdrawal_amount
            print(f"Your {type_compte[choix_utilisateur - 1]} account now has a balance of ${current_account[choix_utilisateur]}")
    elif choix_utilisateur1 == 3 and choix_utilisateur == 3:
        print(f"Your Investment account balance is ${current_account[choix_utilisateur]}")
        interest_rate = current_account[5] / 100
        print(f"Your interest rate is {interest_rate}")
        print("Projected investment return in 5 years:")
        for i in range(1, 6):
            interest = current_account[choix_utilisateur] * interest_rate
            current_account[choix_utilisateur] += interest
            print(f"{i} year: ${current_account[choix_utilisateur]}")
    elif choix_utilisateur1 == 4:
        break
    else:
        print("Invalid choice. Please try again.")
        
# Step 7: Admin Menu
if account_num == "0000" and password == "admin":
    while True:
        print("Menu admin:")
        print("1. Voir tous les comptes")
        print("2. Ajouter un compte")
        print("3. Effacer un compte")
        print("4. Quiiter le terminal")

        admin_choix = int(input("Entrer une action à faire: "))

        if admin_choix == 1:
            for account in database:
                print(account)
        elif admin_choix == 2:
            n_compte_num = input("Entrer un numéro de compte: ")
            n_password = input("Entrer un mot de passe: ")
            n_cheque = int(input("Saisir le solde du compte chèque: "))
            n_epargne = int(input("Saisir le solde du compte d'épargne: "))
            n_investissement = int(input("Saisissez le solde du compte de placement: "))
            n_interet = float(input("Entrez le taux d'intérêt: "))
            n_compte = [n_compte_num, n_password, n_cheque, n_epargne, n_investissement, n_interet]
            database.append(n_compte)
            print("Nouveau compte ajouté")
        elif admin_choix == 3:
            effacer_compte_num = input("Entrer le num du compte à effacer: ")
            for account in database:
                if account[0] == effacer_compte_num:
                    database.remove(account)
                    print("Compte effacer")
                    break
            else:
                print("Compte inexistant")
        elif admin_choix == 4:
            break
        else:
            print("Choix invalide,. réessayer.")

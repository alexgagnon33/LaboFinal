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
Décryptage_database = []
for item in encryptage_database:
    Décryptage_item = []
    for element in item:
        if isinstance(element, str):
            Décryptage_element = ""
            for letter in element:
                index = Random_Base.index(letter)
                Décryptage_element += Base[index]
                Décryptage_item.append(Décryptage_element)
        else:
            Décryptage_item.append(element)
            Décryptage_database.append(Décryptage_item)

print("Database original:", database)
print("Database décrypter:", Décryptage_database)

# Step 2: Choose Account
print("Choose an account:")
print("1. Cheque")
print("2. Savings")
print("3. Investments")

account_choice = int(input("Enter 1, 2, or 3: "))
account_types = ["Cheque", "Savings", "Investments"]

# Step 3: Choose Operation
while True:
    print("Choose an operation:")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    if account_choice == 3:
        print("3. View Investment Return")
    print("4. Terminate")
    
    operation = int(input("Enter 1, 2, 3, or 4: "))
    
    if operation == 1:
        deposit_amount = int(input("Enter deposit amount: "))
        current_account[account_choice] += deposit_amount
        print(f"Your {account_types[account_choice - 1]} account now has a balance of ${current_account[account_choice]}")
    elif operation == 2:
        withdrawal_amount = int(input("Enter withdrawal amount: "))
        if current_account[account_choice] - withdrawal_amount < 0:
            print(f"Insufficient funds in your {account_types[account_choice - 1]} account.")
        else:
            current_account[account_choice] -= withdrawal_amount
            print(f"Your {account_types[account_choice - 1]} account now has a balance of ${current_account[account_choice]}")
    elif operation == 3 and account_choice == 3:
        print(f"Your Investment account balance is ${current_account[account_choice]}")
        interest_rate = current_account[5] / 100
        print(f"Your interest rate is {interest_rate}")
        print("Projected investment return in 5 years:")
        for i in range(1, 6):
            interest = current_account[account_choice] * interest_rate
            current_account[account_choice] += interest
            print(f"{i} year: ${current_account[account_choice]}")
    elif operation == 4:
        break
    else:
        print("Invalid choice. Please try again.")
        
# Step 7: Admin Menu
if account_num == "0000" and password == "admin":
    while True:
        print("Admin Menu:")
        print("1. View all accounts")
        print("2. Add a new account")
        print("3. Delete an account")
        print("4. Logout")

        admin_choice = int(input("Enter 1, 2, 3, or 4: "))

        if admin_choice == 1:
            for account in database:
                print(account)
        elif admin_choice == 2:
            new_account_num = input("Enter new account number: ")
            new_password = input("Enter password: ")
            new_cheque = int(input("Enter cheque account balance: "))
            new_savings = int(input("Enter savings account balance: "))
            new_investments = int(input("Enter investments account balance: "))
            new_interest = float(input("Enter interest rate: "))
            new_account = [new_account_num, new_password, new_cheque, new_savings, new_investments, new_interest]
            database.append(new_account)
            print("New account added.")
        elif admin_choice == 3:
            delete_account_num = input("Enter account number to delete: ")
            for account in database:
                if account[0] == delete_account_num:
                    database.remove(account)
                    print("Account deleted.")
                    break
            else:
                print("Account not found.")
        elif admin_choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

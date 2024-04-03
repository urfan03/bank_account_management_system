from random import randint
from datetime import datetime

class Bank:

    name = 'Pasha Bank'
    clients = []
    def update_db(self, client):
        self.clients.append(client)

    def authentication(self, name, password):
        for i in range(len(self.clients)):
            if name == self.clients[i].account['name'] and password == self.clients[i].account['password']:
                print("\nAuthentication successful!")
                return self.clients[i]
        print("\nAuthentication failed!")
        return None

class Client:

    def __init__(self, name, password, deposit):
        self.account = {
            'account_number': randint(10000, 99999),
            'name': name,
            'password': password,
            'holdings': deposit,
            'transaction_history': []
        }

    def withdraw(self, amount):
        if amount <= 0:
            print("\nInvalid withdrawal amount!")
            return
        if self.account['holdings'] >= amount:
            self.account['holdings'] -= amount
            self.account['transaction_history'].append((datetime.now(), f"Withdrawal: {amount}"))
            print("\nThe sum of {} has been withdrawn from your account balance.".format(amount))
        else:
            print("\nNot enough funds!")

    def deposit(self, amount):
        if amount <= 0:
            print("\nInvalid deposit amount!")
            return
        self.account['holdings'] += amount
        self.account['transaction_history'].append((datetime.now(), f"Deposit: {amount}"))
        print("\nThe sum of {} has been added to your account balance.".format(amount))

    def balance(self):
        print("\nYour current account balance is: {} ".format(self.account['holdings']))

    def display_transaction_history(self):
        print("\nTransaction history for {}: ".format(self.account['name']))
        for transaction in self.account['transaction_history']:
            print("- Date: {}, Description: {}".format(transaction[0], transaction[1]))

bank = Bank()
print("\nWelcome to {}!".format(bank.name))
running = True
while running:
    print("\nChoose an option:")
    print("1. Open new bank account")
    print("2. Open existing bank account")
    print("3. Exit")
    choice = int(input("1, 2 or 3: "))
    if choice == 1:
        print("\nTo create an account, please fill in the information below.")
        client = Client(input("Name: "), input("Password: "), int(input("Deposit amount: ")))
        bank.update_db(client)
        print("\nAccount created successfully! Your account number is: ", client.account['account_number'])
    elif choice == 2:
        print("\nTo access your account, please enter your credentials below.")
        name = input("Name: ")
        password = input("Password: ")
        current_client = bank.authentication(name, password)
        if current_client:
            print("\nWelcome {}!".format(current_client.account['name']))
            acc_open = True
            while acc_open:
                print("\nChoose an option:")
                print("1. Withdraw")
                print("2. Deposit")
                print("3. Balance")
                print("4. Display Transaction History")
                print("5. Exit")
                acc_choice = int(input("1, 2, 3, 4 or 5: "))
                if acc_choice == 1:
                    current_client.withdraw(int(input("Withdraw amount: ")))
                elif acc_choice == 2:
                    current_client.deposit(int(input("Deposit amount: ")))
                elif acc_choice == 3:
                    current_client.balance()
                elif acc_choice == 4:
                    current_client.display_transaction_history()
                elif acc_choice == 5:
                    print("\nThank you for visiting!")
                    acc_open = False
        else:
            print("\nAuthentication failed! Reason: account not found.")
    elif choice == 3:
        print("\nGoodbye!")
        running = False

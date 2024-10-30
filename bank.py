from clients import Client
from accounts import BankAccount, SavingsAccount, CreditAccount, DepositAccount
import general_methods as gm


class Bank:
    def __init__(self):
        self.__mfo_bank = 305229
        self.__list_clients = []
        self.__list_accounts = []

    @property
    def mfo_bank(self):
        return self.__mfo_bank

    @property
    def list_clients(self):
        return self.__list_clients

    @list_clients.setter
    def list_clients(self, new_client):
        self.__list_clients.append(new_client)

    @property
    def list_accounts(self):
        return self.__list_accounts

    @list_accounts.setter
    def list_accounts(self, new_account):
        self.__list_accounts.append(new_account)

    def create_new_client(self, client, account_number):
        """ створення нового клієнта"""
        new_client = Client(client, len(self.__list_clients))
        new_account = BankAccount(account_number, new_client)
        new_client.list_accounts = new_account
        self.__list_clients.append(new_client)
        self.__list_accounts.append(new_account)
        return True, new_client

    def open_new_account(self, new_account):
        """ відкриття рахунку"""

        pass

    def transfer_to_account_ather_client(self):
        """ транзакція між рахунками різних клієнтів"""
        pass

    def generate_statement(self):
        """ генерація виписок по рахункам клієнтів"""
        pass

    def save_to_file(self):
        pass

    def download_from_file(self):
        #TODO: переробити завантаження з файлу, зробити без створення об'єктів
        data_bank = gm.load_from_file_json()
        for client in data_bank['clients']:
            bank_account = next((account['account_number'] for account in client['list_accounts'] if account['type'] == 'main'), None)
            *a, new_client = self.create_new_client(client['name'], bank_account)
            if len(client['list_accounts']) > 1:
                for account in client['list_accounts']:
                    class_account = account['type']
                    if class_account == 'savings':
                        new_client.list_accounts = SavingsAccount(account['account_number'], client,
                                                                  account['interest_rate'],
                                                                  account['limit_min'])
                    elif class_account == 'credit':
                        new_client.list_accounts = CreditAccount(account['account_number'], client,
                                                                 account['interest_rate'],
                                                                 account['interest_on_loan'])
                    elif class_account == 'deposit':
                        new_client.list_accounts = DepositAccount(account['account_number'],
                                                                  client,
                                                                  account['interest_rate'],
                                                                  account['time_period'])



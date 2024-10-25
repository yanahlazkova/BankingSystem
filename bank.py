from clients import Client
from accounts import SavingsAccount, CreditAccount, DepositAccount
import general_methods as gm


class Bank:
    __mfo_bank = 305229
    __list_clients = []
    __list_accounts = []


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
        new_account = SavingsAccount(new_client, account_number)
        self.__list_clients.append(new_client)
        self.__list_accounts.append(new_account)
        print('Створення ного клієнта')
        return True

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

    def download_width_file(self):
        pass

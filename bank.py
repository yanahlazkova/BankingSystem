import json

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

    def create_new_client(self, client, primary_account):
        """ створення нового клієнта"""
        new_client = Client(client, len(self.__list_clients), primary_account)
        new_account = SavingsAccount(primary_account, new_client)
        new_client.primary_account = new_account
        # json_data = new_client.json()
        # print('json_data', json_data)
        self.__list_clients.append(new_client)
        self.__list_accounts.append(new_account)
        return new_client

    def open_new_account(self, account_number, type_account, client, data_account):
        """ відкриття рахунку"""
        print('bank.open_new account')
        new_account = None
        if type_account == 'savings':
            interest_rate, limit_min = data_account
            new_account = SavingsAccount(account_number, client, interest_rate, limit_min)
        client.list_accounts = new_account
        self.__list_accounts.append(new_account)

    def transfer_to_account_ather_client(self):
        """ транзакція між рахунками різних клієнтів"""
        pass

    def generate_statement(self):
        """ генерація виписок по рахункам клієнтів"""
        pass

    def save_to_file(self):

        file_name = 'bank_data.json'
        data = {
            'accounts': [account.to_dict() for account in self.__list_accounts],
            'clients': [client.to_dict() for client in self.__list_clients]
        }

        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self):
        print('Loading....')
        file_name = 'bank_data.json'
        try:
            with open(file_name) as file:
                data = json.load(file)
            if data:
                for client in data['clients']:
                    new_client = self.create_new_client(client['name'],
                                                        client['primary_account'])
                    if client['list_accounts']:
                        for account in client['list_accounts']:
                            self.create_account_from_data_file(new_client, **account)
                for account in data["accounts"]:
                    new_client = gm.find_client_in_list(account['client_id'], self.__list_clients)
                    self.create_account_from_data_file(new_client, **account)
        except Exception as e:
            print('File does not exist', e)

    def create_account_from_data_file(self, client, **account):

        if account['type'] == 'savings':
            client.list_accounts = SavingsAccount(account['account_number'], client,
                                                  account['interest_rate'],
                                                  account['limit_min'],
                                                  )
        elif account['type'] == 'credit':
            client.list_accounts = CreditAccount(account['account_number'],
                                                 client,
                                                 account['interest_rate'],
                                                 account['interest_on_loan'])
        elif account['type'] == 'deposit':
            client.list_accounts = DepositAccount(account['account_number'],
                                                  client,
                                                  account['interest_rate'],
                                                  account['time_period'])

    def generate_new_account_number(self):
        data_part, random_part = gm.generate_unique_account_number()
        new_account = f'UA{random_part}{self.mfo_bank}{data_part}'
        return new_account

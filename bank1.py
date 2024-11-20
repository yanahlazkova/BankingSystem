import json
import uuid

from client1 import Client, ClientBinaryTree
from account1 import BankAccount, SavingsAccount, CreditAccount, DepositAccount, AccountBinaryTree
import general_methods as gm


class Bank:
    def __init__(self, mfo_bank):
        self.__mfo_bank = mfo_bank
        self.__list_clients = ClientBinaryTree()
        self.__list_accounts = AccountBinaryTree()

    def add_new_client(self, client, number_primary_account):
        pass

    def load_from_file(self, file_name):
        try:
            with open(file_name, encoding='utf-8') as file:
                data_bank = json.load(file)

        except Exception as e:
            print('File does not exist', e)

        if data_bank:
            self.__list_clients.print_tree()
            clients = data_bank.get('clients')
            for client in clients:
                new_client = Client(client['name'], str(uuid.uuid4()), client['primary_account'])
                # client_json = json.dumps(new_client.to_dict(), indent=4, ensure_ascii=False)
                # print(client_json)
                # додаємо клієнта у бінарне дерево
                self.__list_clients.insert(new_client.client_id, new_client)
                list_accounts = client.get('list_accounts')
                if list_accounts:
                    for account in list_accounts:
                        new_account = SavingsAccount(new_client.client_id,
                                                     account['account_number'],
                                                     account['balance'],
                                                     account['interest_rate'],
                                                     account['limit_min']
                                                     )
                        new_client.list_accounts.append(new_account.account_number)
                        self.__list_accounts.insert(new_account.account_number, new_account)
            # self.__list_clients.print_tree()
            accounts = data_bank.get('accounts')
            if accounts:
                for account in accounts:
                    found_account = self.__list_accounts.find_account(account['account_number'])
                    new_account = SavingsAccount(account['client_id'],
                                                 account['account_number'],
                                                 account['balance'],
                                                 account['interest_rate'],
                                                 account['limit_min']
                                                 )
                    # if found_account == new_account:
                    #     print(f'{found_account.account_number} - {new_account.account_number}')
                    #     new_client = gm.find_client_in_list(account['client_id'], self.__list_clients)
                    #     self.create_account_from_data_file(new_client, **account)
            # self.__list_accounts.print_all()
        else:
            print('File is empty...')

    def save_to_file_json(self):
        data = {
            'accounts': self.__list_accounts.to_dict(),
            'clients': self.__list_clients
        }
        # print(data)

    def create_account(self, **data_account):
        pass


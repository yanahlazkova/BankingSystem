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

    @property
    def list_accounts(self):
        return self.__list_accounts

    @list_accounts.setter
    def list_accounts(self, account):
        self.__list_accounts.insert(account.account_number, account)
        print("Рахунок додано в список рахунків Банку")

    @property
    def list_clients(self):
        return self.__list_clients

    @list_clients.setter
    def list_clients(self, client):
        self.__list_clients.insert(client.client_id, client)

    @property
    def mfo_bank(self):
        return self.__mfo_bank

    def load_from_file(self, file_name):
        try:
            with open(file_name, encoding='utf-8') as file:
                bank_data = json.load(file)
        except Exception as e:
            print(f'Помилка зчитування файлу: {e}')

        if bank_data:
            # self.__list_clients.print_tree()
            # self.__list_accounts.print_all()

            # Add clients
            clients = bank_data.get('clients')
            if clients:
                for client in clients.values():
                    new_client = Client(client['name'], client['client_id'], client['primary_account'])
                    # client_json = json.dumps(new_client.to_dict(), indent=4, ensure_ascii=False)
                    # print(client_json)
                    # додаємо клієнта у бінарне дерево
                    self.__list_clients.insert(new_client.client_id, new_client)
                    accounts_client = client.get('list_accounts')
                    for account in accounts_client:
                        new_client.list_accounts.append(account)

            # Add accounts
            accounts = bank_data.get('accounts')
            if accounts:
                for account in accounts.values():
                    new_account = SavingsAccount(account['account_number'],
                                                 account['client_id'],
                                                 account['balance'],
                                                 account['interest_rate'],
                                                 account['limit_min']
                                                 )
                    self.__list_accounts.insert(new_account.account_number, new_account)
            # self.__list_clients.print_tree()
            # self.__list_accounts.print_all()
        else:
            print('File is empty...')

    def save_to_file_json(self):
        data = {
            'accounts': self.__list_accounts.to_dict(),
            'clients': self.__list_clients.to_dict()
        }
        data1 = json.dumps(data, indent=4)
        print(data1)
        try:
            with open('bank_data1.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print('Ошибка записи в файл: ', e)

    def create_new_account(self, type_account, client, interest_rate=None,
                           limit_min=None,
                           interest_on_loan=None,
                           time_period=None,
                           account_number=None) -> BankAccount:
        account_number = (account_number if account_number else gm.generate_unique_account_number(self.mfo_bank))
        new_account = None

        match type_account:
            case 'savings':
                new_account = SavingsAccount(account_number=account_number,
                                             owner_id=client.client_id,
                                             balance=0,
                                             interest_rate=interest_rate,
                                             limit_min=limit_min)
                print(f"Added account {new_account.to_dict()}")

            case 'credit':
                new_account = CreditAccount(account_number=account_number,
                                            owner_id=client.client_id,
                                            balance=0,
                                            interest_rate=interest_rate,
                                            interest_on_loan=interest_on_loan)
                print(f"Added account {new_account.to_dict()}")

            case 'deposit':
                new_account = DepositAccount(account_number=account_number,
                                             owner_id=client.client_id,
                                             balance=0,
                                             interest_rate=interest_rate,
                                             time_period=time_period)
                print(f"Added account {new_account.to_dict()}")


        # self.__list_clients.add_account_to_list(client.client_id, account_number)
        client.list_accounts.append(account_number)
        self.__list_accounts.insert(account_number, new_account)
        return new_account

    def create_savings_account(self, account_number, client_id,
                               balance=0,
                               interest_rate=None,
                               limit_min=None):
        """ відкритя ощадного рахунку """

        new_account = SavingsAccount(account_number=account_number,
                                     owner_id=client_id,
                                     balance=0,
                                     interest_rate=interest_rate,
                                     limit_min=limit_min)
        print(f"Added account {new_account.to_dict()}")
        return new_account

    def create_credit_account(self, account_number,
                              client_id,
                              balance=0,
                              interest_rate=None,
                              interest_on_loan=None):
        new_account = CreditAccount(account_number=account_number,
                                    owner_id=client_id,
                                    balance=balance,
                                    interest_rate=interest_rate,
                                    interest_on_loan=interest_on_loan)
        return new_account

    def create_deposit_account(self, account_number, client_id,
                               owner_id,
                               balance=0,
                               interest_rate=None,
                               time_period=None):
        new_account = DepositAccount(account_number=account_number,
                                     owner_id=client_id,
                                     balance=balance,
                                     interest_rate=interest_rate,
                                     time_period=time_period)
        return new_account

    def create_new_client(self, client_name, account_number):
        new_client = Client(name=client_name, client_id=str(uuid.uuid4()), primary_account=account_number)
        return new_client



    # def load_from_file(self, file_name):
    #     """ Загрузка з файлу bank_data.json """
    #     try:
    #         with open(file_name, encoding='utf-8') as file:
    #             data_bank = json.load(file)
    #
    #     except Exception as e:
    #         print('File does not exist', e)
    #
    #     if data_bank:
    #         self.__list_clients.print_tree()
    #         clients = data_bank.get('clients')
    #         for client in clients:
    #             new_client = Client(client['name'], str(uuid.uuid4()), client['primary_account'])
    #             # client_json = json.dumps(new_client.to_dict(), indent=4, ensure_ascii=False)
    #             # print(client_json)
    #             # додаємо клієнта у бінарне дерево
    #             self.__list_clients.insert(new_client.client_id, new_client)
    #             list_accounts = client.get('list_accounts')
    #             if list_accounts:
    #                 for account in list_accounts:
    #                     new_account = SavingsAccount(new_client.client_id,
    #                                                  account['account_number'],
    #                                                  account['balance'],
    #                                                  account['interest_rate'],
    #                                                  account['limit_min']
    #                                                  )
    #                     new_client.list_accounts.append(new_account.account_number)
    #                     self.__list_accounts.insert(new_account.account_number, new_account)
    #         # self.__list_clients.print_tree()
    #         accounts = data_bank.get('accounts')
    #         if accounts:
    #             for account in accounts:
    #                 found_account = self.__list_accounts.find_account(account['account_number'])
    #                 new_account = SavingsAccount(account['client_id'],
    #                                              account['account_number'],
    #                                              account['balance'],
    #                                              account['interest_rate'],
    #                                              account['limit_min']
    #                                              )
    #         else:
    #             print('File is empty...')
from dataclasses import dataclass


@dataclass
class Client:
    def __init__(self, name, counter_client, primary_account):
        self.__primary_account = primary_account
        self.__client_id = f'500-{counter_client + 1}'
        self.__name = name
        self.__list_accounts = []

    @property
    def name(self):
        return self.__name

    @property
    def client_id(self):
        return self.__client_id

    @property
    def list_accounts(self):
        return (account for account in self.__list_accounts)

    @list_accounts.setter
    def list_accounts(self, new_account):
        self.__list_accounts.append(new_account)

    @property
    def primary_account(self):
        return self.__primary_account

    @primary_account.setter
    def primary_account(self, primary_account):
        self.__primary_account = primary_account

    def to_dict(self):
        return {
            'client_id': self.__client_id,
            'name': self.__name,
            'list_accounts': [account.to_dict() for account in self.__list_accounts]
        }

    def create_new_account(self, account):
        """ створення нового рахунку """
        pass

    # Виконання операцій з депозитами, зняттям коштів
    # та переказами між рахунками клієнта.
from dataclasses import dataclass


@dataclass
class Client:
    def __init__(self, name, client_id: str, primary_account=None):
        self.__primary_account = primary_account
        self.__client_id = client_id
        self.__name = name
        self.__list_accounts = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

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
            self.__client_id:
                {'client_id': self.__client_id,
                 'name': self.__name,
                 'primary_account': self.__primary_account,
                 'list_accounts': [account.to_dict() for account in self.__list_accounts]
                 }
        }

    def add_new_account(self, account):
        """ створення нового рахунку """
        pass

    # Виконання операцій з депозитами, зняттям коштів
    # та переказами між рахунками клієнта.
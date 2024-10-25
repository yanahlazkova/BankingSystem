class Client:
    def __init__(self, name, counter_client):
        self.__client_id = f'500-{counter_client + 1}'
        self.__name = name
        self.__list_accounts = []

    @property
    def name(self):
        return self.__name

    @property
    def client_id(self):
        return self.__client_id

    def create_new_account(self, account):
        """ створення нового рахунку """
        pass

    @property
    def list_accounts(self):
        return (account for account in self.__list_accounts)

    @list_accounts.setter
    def list_accounts(self, new_account):
        self.__list_accounts.append(new_account)

    # Виконання операцій з депозитами, зняттям коштів
    # та переказами між рахунками клієнта.
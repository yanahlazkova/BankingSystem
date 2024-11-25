class BankAccount:
    # __type = 'main'

    # Список полів, доступних для виводу списку рахунків

    def __init__(self, owner_id, account_number, balance=0, interest_rate=1):
        # власник рахунку
        self.owner_id = owner_id
        # номер рахунку (унікальний)
        self.account_number = account_number
        # баланс
        self.balance = balance
        # відсоткова ставка
        self.interest_rate = interest_rate

    def to_dict(self):
        return {
            'account_number': self.account_number,
            'balance': self.balance,
            # 'owner': self.owner.client_id,
            'interest_rate': self.interest_rate,
        }

    # @property
    # def owner_id(self):
    #     return self.owner_id
    #
    # @owner_id.setter
    # def owner_id(self, new_client):
    #     self.owner = new_client
    #
    # @property
    # def account_number(self):
    #     return self.account_number
    #
    # @property
    # def balance(self):
    #     return self.balance
    #
    # @balance.setter
    # def balance(self, amount):
    #     self.balance = amount
    #
    # @property
    # def interest_rate(self):
    #     return self.interest_rate
    #
    # @interest_rate.setter
    # def interest_rate(self, interest_rate):
    #     self.interest_rate = interest_rate


class SavingsAccount(BankAccount):
    """ ощадний рахунок """
    __interest_rate = 5
    __limit_min = 100

    def __init__(self, account_number, owner_id, balance, interest_rate=__interest_rate, limit_min=__limit_min):
        super().__init__(account_number=account_number, owner_id=owner_id, balance=balance)
        self.limit_min = limit_min
        self.fixed_interest_rate = interest_rate
        self.type = 'savings'

    # @property
    # def fixed_interest_rate(self):
    #     return self.interest_rate
    #
    # @property
    # def limit_min(self):
    #     return self.limit_min

    # @property
    # def type(self):
    #     return self.type

    def __eq__(self, other):
        return (self.owner_id == other.owner_id
                and self.account_number == other.account_number
                and self.balance == other.balance
                and self.interest_rate == other.interest_rate
                and self.limit_min == other.limit_min)

    def __repr__(self):
        return (f'\nAccount number {self.account_number}:'
                f'\n\tClient ID-{self.owner_id}'
                f'\n\tBalance:\t{self.balance}'
                f'\n\tInterest rate:\t{self.interest_rate}'
                f'\n\tLimit min:\t{self.limit_min}')

    def to_dict(self):
        return {
            'account_number': self.account_number,
            'client_id': self.owner_id,
            'balance': self.balance,
            'limit_min': self.limit_min,
            'interest_rate': self.fixed_interest_rate,
            'type': self.type
        }


class CreditAccount(BankAccount):

    def __init__(self, account_number, owner_id, balance, interest_rate, interest_on_loan):
        super().__init__(account_number=account_number, owner_id=owner_id, balance=balance)
        self.interest_rate = interest_rate
        self.interest_on_loan = interest_on_loan  # відсоток по кредиту
        self.type = 'credit'

    def __repr__(self):
        return (f'\nAccount number {self.account_number}:'
                f'\n\tClient ID-{self.owner_id}'
                f'\n\tBalance:\t{self.balance}'
                f'\n\tInterest rate:\t{self.interest_rate}'
                f'\n\tinterest_on_loan:\t{self.interest_on_loan}')

    def to_dict(self):
        return {
            'account_number': self.account_number,
            'client_id': self.owner_id,
            'balance': self.balance,
            'interest_rate': self.interest_rate,
            'interest_on_loan': self.interest_on_loan,
            'type': self.type
        }


class DepositAccount(BankAccount):
    __type = 'deposit'
    __time_period = 1

    def __init__(self, account_number, owner_id, balance, interest_rate, time_period=__time_period):
        super().__init__(account_number=account_number, owner_id=owner_id, balance=balance)
        self.interest_rate = interest_rate
        self.fixed_time_period = time_period
        self.type = 'deposit'

    def __repr__(self):
        return (f'\nAccount number {self.account_number}:'
                f'\n\tClient ID-{self.owner_id}'
                f'\n\tBalance:\t{self.balance}'
                f'\n\tInterest rate:\t{self.interest_rate}'
                f'\n\tfixed_time_period:\t{self.fixed_time_period}')

    def to_dict(self):
        return {
            'account_number': self.account_number,
            'client_id': self.owner_id,
            'balance': self.balance,
            'interest_rate': self.interest_rate,
            'fixed_time_period': self.fixed_time_period,
            'type': self.type
        }


class AccountNode:
    def __init__(self, key, account):
        self.key = key
        self.data = account
        self.left = None
        self.right = None


class AccountBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if not self.root:
            self.root = AccountNode(key, data)
        else:
            self.__insert(self.root, key, data)

    def __insert(self, node, key, data):
        if key < node.key:
            if node.left:
                self.__insert(node.left, key, data)
            else:
                node.left = AccountNode(key, data)
        elif key > node.key:
            if node.right:
                self.__insert(node.right, key, data)
            else:
                node.right = AccountNode(key, data)

    def find_account(self, key):
        return self.__find_account(self.root, key)

    def __find_account(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node.data
        elif key < node.key:
            return self.__find_account(node.left, key)
        else:
            return self.__find_account(node.right, key)

    def print_all(self, node=None):
        if node is None:
            node = self.root
        if node is not None:
            print(node.data)
            if node.left or node.right:
                if node.left:
                    self.print_all(node.left)
                if node.right:
                    self.print_all(node.right)
        else:
            print("List of accounts is EMPTY")

    def to_dict(self, node=None):
        result = {}
        if node is None:
            node = self.root
        if node is not None:
            result[node.data.account_number] = node.data.to_dict()
            if node.left or node.right:
                if node.left:
                    result.update(self.to_dict(node.left))
                if node.right:
                    result.update(self.to_dict(node.right))
        return result

    def length(self):
        return self.__len__(self.root)

    def __len__(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.__len__(node.left) + self.__len__(node.right)

    def get_list(self, node=None):
        result = []
        if node is None:
            node = self.root
        if node is not None:
            result.append(node.data.to_dict())
            if node.left or node.right:
                if node.left:
                    result.extend(self.get_list(node.left))
                if node.right:
                    result.extend(self.get_list(node.right))
        return result

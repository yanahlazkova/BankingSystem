class BankAccount:
    __type = 'main'

    # Список полів, доступних для виводу списку рахунків

    def __init__(self, owner_id, account_number, balance=0, interest_rate=1):
        # власник рахунку
        self.__owner_id = owner_id
        # номер рахунку (унікальний)
        self.__account_number = account_number
        # баланс
        self.__balance = balance
        # відсоткова ставка
        self.__interest_rate = interest_rate

    def to_dict(self):
        return {
            'account_number': self.__account_number,
            'balance': self.__balance,
            # 'owner': self.__owner.client_id,
            'interest_rate': self.__interest_rate,
            'type': self.__type
        }

    @property
    def owner_id(self):
        return self.__owner_id

    @owner_id.setter
    def owner_id(self, new_client):
        self.__owner = new_client

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance = amount

    @property
    def interest_rate(self):
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate

    @property
    def type(self):
        return self.__type

class SavingsAccount(BankAccount):
    """ ощадний рахунок """
    __interest_rate = 5
    __limit_min = 100
    __type = 'savings'

    def __init__(self, owner_id, account_number, balance, interest_rate=__interest_rate, limit_min=__limit_min):
        super().__init__(owner_id, account_number, balance, interest_rate)
        self.__limit_min = limit_min
        self.__fixed_interest_rate = interest_rate

    @property
    def fixed_interest_rate(self):
        return self.__interest_rate

    @property
    def limit_min(self):
        return self.__limit_min

    @property
    def type(self):
        return self.__type

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
            'limit_min': self.__limit_min,
            'interest_rate': self.__fixed_interest_rate,
            'type': self.__type
        }

class CreditAccount(BankAccount):
    __type = 'credit'

    def __init__(self, account_number, owner, interest_rate, interest_on_loan):
        super().__init__(account_number, owner)
        self.__interest_rate = interest_rate
        self.__interest_on_loan = interest_on_loan  # відсоток по кредиту

    def to_dict(self):
        pass

class DepositAccount(BankAccount):
    __type = 'deposit'
    __time_period = 1

    def __init__(self, account_number, owner, interest_rate, time_period=__time_period):
        super().__init__(account_number, owner)
        self.__interest_rate = interest_rate
        self.__fixed_time_period = time_period

    def to_dict(self):
        pass


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

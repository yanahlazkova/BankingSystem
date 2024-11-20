from dataclasses import dataclass


@dataclass
class BankAccount:
    __type = 'main'

    # Список полів, доступних для виводу списку рахунків

    def __init__(self, account_number, owner):
        # номер рахунку (унікальний)
        self.__account_number = account_number
        # баланс
        self.__balance = 0
        # власник рахунку
        self.__owner = owner
        # відсоткова ставка
        self.__interest_rate = 1

    def to_dict(self):
        return {
            'account_number': self.__account_number,
            'balance': self.__balance,
            # 'owner': self.__owner.client_id,
            'interest_rate': self.__interest_rate,
            'type': self.__type
        }

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, new_client):
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

    def deposit(self, amount):
        """ метод для внесення коштів на рахунок"""
        pass

    def withdraw(self, amount):
        """ метод для зняття коштів з рахунку"""
        pass

    def show_balance(self):
        """ метод для виведення інформації про баланс """
        pass

    def calculate_interest_accrual(self):
        """ метод для обчислення відсотків по рахунку та нарахування їх на баланс"""
        pass

    # Інтерфейс Transferable (інтерфейс для рахунків, які підтримують перекази між ними)
    def transfer(self, to_account, amount):
        """ метод для переказу коштів на інший рахунок"""
        pass


class SavingsAccount(BankAccount):
    """ ощадний рахунок """
    __interest_rate = 5
    __limit_min = 100
    __type = 'savings'

    def __init__(self, account_number, owner, interest_rate=__interest_rate, limit_min=__limit_min):
        super().__init__(account_number, owner)
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

    def to_dict(self):
        return {
            self.account_number:
                {'account_number': self.account_number,
                 'balans': self.balance,
                 'limit_min': self.__limit_min,
                 'interest_rate': self.__fixed_interest_rate,
                 'type': self.__type
                 }
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

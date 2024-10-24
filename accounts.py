class BankAccount:

    def __init__(self, account_number, owner):
        # номер рахунку (унікальний)
        self.__account_number = account_number
        # баланс
        self.__balans = 0
        # власник рахунку
        self.__owner = owner
        # відсоткова ставка
        self.__interest_rate = 1

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, new_client):
        self.__owner = new_client

    @property
    def account_number(self):
        return self.__account_number

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
    def __init__(self, account_number, owner, interest_rate, limit_min):
        super().__init__(account_number, owner, interest_rate)
        self.__limit_min = limit_min
        self.__fixed_interest_rate = 1


class CreditAccount(BankAccount):
    def __init__(self, account_number, owner, interest_rate, interest_on_loan):
        super().__init__(account_number, owner, interest_rate)
        self.__interest_on_loan = interest_on_loan


class DepositAccount(BankAccount):
    def __init__(self, account_number, owner, interest_rate, time_period):
        super().__init__(account_number, owner, interest_rate)
        self.__fixed_time_period = time_period

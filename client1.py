class Client:
    def __init__(self, name: str, client_id: str, primary_account: str =None):
        self.__name = name
        self.__client_id = client_id
        # основний рахунок не змінюється
        self.__primary_account = primary_account
        # містить номери рахунків клієнта
        self._list_accounts = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def client_id(self):
        return self.__client_id

    @property
    def primary_account(self):
        return self.__primary_account

    @property
    def list_accounts(self):
        return self._list_accounts

    @list_accounts.setter
    def list_accounts(self, account):
        self._list_accounts.append(account)

    def __repr__(self):
        list_account = '\n\t'.join(f'{index + 1}. {account}' for index, account in enumerate(self._list_accounts))
        return (f'\nID: {self.__client_id}\n\tName: {self.__name}'
                f'\n\tPrimary_account:{self.__primary_account}\nAccounts:{f'\n\t{list_account}' if list_account else '\tempty'}')

    def to_dict(self):
        return {
            'client_id': self.__client_id,
            'name': self.__name,
            'primary_account': self.__primary_account,
            'list_accounts': [account for account in self._list_accounts]
        }

class ClientNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


class ClientBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if not self.root:
            self.root = ClientNode(key, data)
        else:
            self.__insert(self.root, key, data)

    def __insert(self, node, key, data):
        if key < node.key:
            if node.left:
                self.__insert(node.left, key, data)
            else:
                node.left = ClientNode(key, data)
        elif key > node.key:
            if node.right:
                self.__insert(node.right, key, data)
            else:
                node.right = ClientNode(key, data)

    def find_by_id(self, key):
        return self.__find_by_id(self.root, key)

    def __find_by_id(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node.data
        elif key < node.key:
            return self.__find_by_id(node.left, key)
        else:
            return self.__find_by_id(node.right, key)

    def add_account_to_list(self, key, number_account):
        current_node: Client = self.find_by_id(key)
        if current_node:
            current_node.list_accounts.append(number_account)
        else:
            print(f'Client id-{key} not fount')

    def print_tree(self, node=None):
        if node is None:
            node = self.root
        if node is not None:
            print(node.data)
            if node.left or node.right:
                if node.left:
                    self.print_tree(node.left)
                if node.right:
                    self.print_tree(node.right)
        else:
            print("List of clients is EMPTY")

    def to_dict(self, node=None):
        result = {}
        if node is None:
            node = self.root
        if node is not None:
            result[node.data.client_id] = node.data.to_dict()
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

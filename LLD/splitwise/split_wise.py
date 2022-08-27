from collections import defaultdict
from enum import Enum
from tokenize import group


class Repository:
    pass


class User:
    def __init__(self, id, name, email) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.share_dict = defaultdict(list)

    def add_share(self, amount, group_name):
        share = UserShare(self.id, amount, group_name)
        self.share_dict[self.id].append(share)
        print(f"User {self.name}, you have a pending share of Rs {amount}")

    def get_user_share(self):
        user_share = self.share_dict[self.id]
        print(f"User {self.name}, you have a pending share of Rs {user_share}")
        return user_share.amount


class UserShare:
    def __init__(self, id, amount, group_name) -> None:
        self.id = id
        self.share = amount
        self.group_name = group_name


class ExpenseType(Enum):
    EQUAL = 1
    EXACT = 2
    PERCENTAGE = 3


class Group:
    def __init__(self, group_name) -> None:
        self.group_name = group_name
        self.group_storage = defaultdict(list)

    def add_member(self, usr: User):
        self.group_storage[self.group_name].append(usr)
        print(f"User {usr.name} has been added to group {self.group_name}")

    def get_members(self, group_name):
        return self.group_storage[group_name]

    def show_all_user_balances(self):
        members = self.get_members(self.group_name)
        for member in members:
            name = member.name
            user_shares = member.share_dict[member.id]
            for share in user_shares:
                if share.group_name == self.group_name:
                    print(f"User {name} has {share.share} pending")


class GroupExpense:
    def __init__(self, amount, expense_type, group_name) -> None:
        self.amount = amount
        self.expense_type = expense_type
        self.group_name = group_name


class Expense:
    def __init__(self, name) -> None:
        self.name = name
        self.group_to_expense = {}

    def add_expense_to_group(self, amount, expense_type, group_name):
        if self.group_to_expense.get(group_name, None):
            grp_expense = self.group_to_expense.get(group_name, None)
            grp_expense.amount += amount
        else:
            grp_expense = GroupExpense(amount, expense_type, group_name)
        self.group_to_expense[group_name] = grp_expense
        print(
            f"Expense with {expense_type} and amount Rs {amount} has been added to group {group_name} "
        )

    def split_expenses(self, group: Group):
        grp_expense = self.group_to_expense.get(group.group_name, None)

        members = group.get_members(group.group_name)
        for member in members:
            if grp_expense.expense_type == ExpenseType.EQUAL.name:
                share_val = grp_expense.amount // len(members)

            member.add_share(share_val, grp_expense.group_name)


class SplitWise:
    def create_user(self, id, name, email):
        return User(id, name, email)

    def create_group(self, group_name):
        return Group(group_name)

    def create_expense(self, name):
        return Expense(name)


if __name__ == "__main__":
    sp = SplitWise()
    usr1 = sp.create_user(1, "Ayan", "ajana50@gmail.com")
    usr2 = sp.create_user(2, "Avishek", "ajana51@gmail.com")
    usr3 = sp.create_user(3, "Suman", "ajana250@gmail.com")

    grp1 = sp.create_group("Test")

    grp1.add_member(usr1)
    grp1.add_member(usr2)
    grp1.add_member(usr3)

    exp1 = sp.create_expense("Party")

    exp1.add_expense_to_group(1000, ExpenseType.EQUAL.name, grp1.group_name)

    exp1.split_expenses(grp1)

    grp1.show_all_user_balances()

    exp1.add_expense_to_group(2000, ExpenseType.EQUAL.name, grp1.group_name)
    exp1.split_expenses(grp1)

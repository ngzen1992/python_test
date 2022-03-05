import math

class Category(object):
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self) -> str:
        result = ""
        no_of_star = 30 - len(self.category)
        result = "".rjust(no_of_star//2, '*') + self.category + "".rjust(no_of_star//2, '*') + '\n'

        for row in self.ledger:
            result = result + str(row["description"])[:23].ljust(23, ' ') + str(format(row["amount"], '.2f'))[:7].rjust(7) + '\n' 

        result = result + "Total: " + str(format(self.get_balance(), '.2f'))

        return result

    ### Withdraw
    def withdraw(self, amount, description = None):
        is_withdrawn = False
        if self.check_funds(amount) is True:
            if description is None:
                self.ledger.append({"amount": -abs(amount), "description": ""})
            else:
                self.ledger.append({"amount": -abs(amount), "description": description})
            is_withdrawn = True
        
        return is_withdrawn
        

    ### Deposit
    def deposit(self, amount, description = None):
        if description is None:
            self.ledger.append({"amount": amount, "description": ""})
        else:
            self.ledger.append({"amount": amount, "description": description})

    ### Get balance
    def get_balance(self):
        balance = 0
        for row in self.ledger:
            balance += row["amount"]

        return balance

    ### Check funds
    def check_funds(self, fund):
        balance = self.get_balance()
        if fund > balance:
            return False
        else:
            return True

    ### Transfer
    def transfer(self, amount, category_class):
        is_transferred = False
        if self.check_funds(amount) is True:
            self.withdraw(amount, str("Transfer to " + category_class.category))
            category_class.deposit(amount, str("Transfer from " + self.category))
            is_transferred = True
 
        return is_transferred

### Create spend  chart
def create_spend_chart(list_of_categories):
    percentage_spent_list = []  
    total_spent_all = 0
    for category in list_of_categories:
        total_spent = 0.00
        for row in category.ledger:
            if row["amount"] < 0:
                total_spent = total_spent + abs(float(row["amount"]))

        total_spent_all = total_spent_all + total_spent
        percentage_spent_list.append({"category_name": category.category, "total_spent": float(format(total_spent, '.2f')), "percentage": 0})

    ### Calculate percentage
    for row in percentage_spent_list:
        row["percentage"] = round_down_nearest_ten(row["total_spent"]/total_spent_all * 100)

    ### print(percentage_spent_list)
    index = 100
    result = "Percentage spent by category\n"
    for percentage in range(100, -10, -10):
        result = result + str(percentage).rjust(3, ' ') + '| '
        ### Print o
        for row in percentage_spent_list:
            if index <= row["percentage"]:
                result = result + 'o  '
            else:
                result = result + '   '

        result = result + '\n' 
        index = index - 10

    ### draw - 
    result = result + '    -' + "".rjust(len(percentage_spent_list)*3, '-')

    ### draw category
    char_index = 0
    len_longest_category_name = 0
    
    ### find longest category name
    for row in percentage_spent_list:
        if len(row["category_name"]) > len_longest_category_name:
            len_longest_category_name = len(row["category_name"])

    for row in range(char_index, len_longest_category_name, 1):
        result = result + '\n     '
        for category in percentage_spent_list:
            if char_index <= len(category["category_name"]) - 1:
                result = result + category["category_name"][char_index] + '  '
            else:
                result = result + '   '

        char_index = char_index + 1

    return result
    
### Round down to nearest 10
def round_down_nearest_ten(x):
    return int(math.floor(x/10.0)) * 10

print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
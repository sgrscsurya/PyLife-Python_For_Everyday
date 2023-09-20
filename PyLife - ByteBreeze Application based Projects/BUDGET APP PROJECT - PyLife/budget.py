# BUDGET APP

""" The Main Objective of this code is to provide a system to manage budget categories, allowing deposits, withdrawals, transfers, and balance checking for each category. """

""" Additionally, It creates a percentage spent chart to visualize spending in each category relative to the total spending. This code promotes effective budget management and Visualization of Financial data. """

# First, Let's define a class named "Category" to define the Budget Category.

# The __init__ method is used to initialise the parameters "self" and "category". The ledger is usually called as a Book of Financial accounts and here let's give it with an empty set.
class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

  # Now, Let's define "deposit" to store deposited values and amounts with the descriptions.
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

# As the same let's define "withdraw" to take cash from the needies(like groceries, restaurant..) and let's give amount and also description parameters for it.

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description}) # Here, we use -amount to indicate the amount is getting deducted/substracted after every withdrawal/transaction.
            return True
        return False
# Now, To get the remaining balance, we give the initial balance to be zero.
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

# Here, Let's define something called "transfer" to transfer the money for each category ( food, clothing, auto, etc).

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False
 # We can check the remaining funds after transactions are made. Hence, we define "check_funds." 
    def check_funds(self, amount):
        return amount <= self.get_balance()

# __str__ method generates a string representation of the category and its ledger.

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

    """ This function generates a chart representing the percentage spent by each category. It calculates the total spending and percentage spending for each category based on the withdrawals """

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spendings = []
    category_names = []

    for category in categories:
        spendings.append(sum(item["amount"] for item in category.ledger if item["amount"] < 0))
        category_names.append(category.category)

    total_spending = sum(spendings)
    percentage_spent = [(spending / total_spending) * 100 for spending in spendings]

# It iterates through each percentage point (100 to 0) and adds "o" for each category if the percentage spent is greater or equal to that point.
  
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentage_spent:
            chart += "o" if percentage >= i else " "
            chart += "  "
        chart += "\n"

    chart += "    -" + "---" * len(categories) + "\n"
  
# It calculates the maximum name length among categories to ensure proper spacing.
    max_name_length = max(len(name) for name in category_names)
    for i in range(max_name_length):
        chart += "     "
        for name in category_names:
            chart += name[i] if i < len(name) else " "
            chart += "  "
        chart += "\n"

# It then constructs and returns the chart with appropriate formatting.

    return chart.rstrip('\n')

# Hence, The code for Budget App is successfully Executed :)
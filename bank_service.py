class opr_class:
    def __init__(self, name, balance, amt):
        self.name = name
        self.balance = balance
        self.amt = amt

    def deposit(self):
        self.balance += self.amt
        queue_list[self.name] = self.balance
        print("Your New Balance is: {}".format(queue_list[self.name]))

    def withdraw(self):
        if self.amt <= self.balance:
            self.balance -= self.amt
            queue_list[self.name] = self.balance
            print("Your New Balance is: {}".format(queue_list[self.name]))
        else:
            print("Not enough Money to withdraw")


if __name__ == "__main__":
    queue_list = {}
    print("Welcome to Cash counter")
    for i in range(1, 3):
        customer_name = input("Enter your Name for Token registration: ")
        print("Thank you {}, Your token number is {}".format(customer_name, i))
        queue_list[customer_name] = 10000  # Assumed every person have Rs.10000 as bank balance
    for j in queue_list:
        print("Token name : {}".format(j))
        option = int(input("What you need to do, 1.Deposit 2.Withdraw: "))
        if option == 1:
            amount = int(input("How much you wish to deposit: "))
            func = opr_class(j, queue_list[j], amount)
            func.deposit()
        elif option == 2:
            amount = int(input("How much you wish to Withdraw: "))
            func = opr_class(j, queue_list[j], amount)
            func.withdraw()


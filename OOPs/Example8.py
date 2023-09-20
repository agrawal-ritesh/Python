class Members:
    org = "NGO"

    def names(self,name, age, amount):
        self.name = name
        self.age = age
        self.amount = amount
        print(f"The amount collected by {self.name} by {self.age} for {self.org} is {self.amount}")
Seva = Members()
Seva.names("John", 34, 100)
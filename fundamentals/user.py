class user:
    def __init__(self):
        self.first_name = "John"
        self.last_name = "Doe"
        self.email = "johndoe@gmail.com"
        self.age = 25
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}") 
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        return self
    
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        print("User enrolled successfully!")
        return self

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("Insufficient points!")
        else:
            self.gold_card_points -= amount
            print(f"Points spent: {amount}. Remaining points: {self.gold_card_points}")
        return self

user1 = user()
user1.display_info().enroll().spend_points(50).display_info()

user2 = user()
user2.display_info().enroll().spend_points(50).display_info()



class GymMember:
    gym_name = "FitLife"
    membership_fee = 45
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

member1 = GymMember("Prakash", 23, 52)
member2 = GymMember("Alex", 25, 70)

member2.weight = 72
GymMember.membership_fee = 50
member1.gym_name = "PowerGym"

print(f"{member1.name}\n{member1.age}\n{member1.weight}\n{member1.gym_name}\n{member1.membership_fee}")

print(f"\n{member2.name}\n{member2.age}\n{member2.weight}\n{member2.gym_name}\n{member2.membership_fee}")
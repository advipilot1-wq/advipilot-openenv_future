import random

class Student:
    def __init__(self):
        self.name = "User"
        self.goal = random.choice(["JEE", "NEET", "Abroad"])
        self.days_left = random.randint(60, 150)
        self.preparedness = random.uniform(0.3, 0.6)
        self.focus = random.uniform(0.4, 0.8)
        self.consistency = random.uniform(0.3, 0.7)

    def update(self, action):
        if action == "study":
            self.preparedness += 0.05 * self.focus
            self.consistency += 0.02

        elif action == "revise":
            self.preparedness += 0.03

        elif action == "skip":
            self.preparedness -= 0.04
            self.consistency -= 0.02

        self.days_left -= 1
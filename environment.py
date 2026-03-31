from student import Student
from reward import calculate_reward

class AdvipilotEnv:

    def reset(self):
        self.student = Student()
        return self.state()

    def state(self):
        return {
            "goal": self.student.goal,
            "days_left": self.student.days_left,
            "preparedness": self.student.preparedness,
            "focus": self.student.focus,
            "consistency": self.student.consistency
        }

    def step(self, action):
        self.student.update(action)
        reward = calculate_reward(self.student)

        done = self.student.days_left <= 0

        return self.state(), reward, done, {}
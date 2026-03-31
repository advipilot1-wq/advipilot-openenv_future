from environment import AdvipilotEnv
from grader import grade

env = AdvipilotEnv()
state = env.reset()

done = False

while not done:
    action = "study"   # simple agent
    state, reward, done, _ = env.step(action)

print("Final State:", state)
print("Final Score:", grade(state))
def calculate_reward(student):
    reward = 0

    reward += student.preparedness * 0.5
    reward += student.consistency * 0.3
    reward += student.focus * 0.2

    return round(reward, 2)
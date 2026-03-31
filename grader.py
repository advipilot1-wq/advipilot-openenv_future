def grade(state):
    if state["preparedness"] > 0.8:
        return 1.0
    elif state["preparedness"] > 0.6:
        return 0.7
    elif state["preparedness"] > 0.4:
        return 0.4
    else:
        return 0.1
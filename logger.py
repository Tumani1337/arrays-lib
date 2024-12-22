def log_action(message):
    with open("information.txt", "a") as information:
        information.write(message)
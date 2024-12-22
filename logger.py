def log_action(message):
    if "info.txt" not in "arrays_lib":
        with open("info.txt", "w") as information:
            pass
    else:
        with open("info.txt", "a") as information:
            information.write(message)
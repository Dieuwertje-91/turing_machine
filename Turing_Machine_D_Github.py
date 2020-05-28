def turingmachine(user_input):

    tape = []
    for number in user_input:
        if number in "0":
            tape.append(1)
        elif number in "1":
            tape.append(0)
        else:
            tape.append("the entered number was not a 0 nor a 1")
    return tape


user_input = input("enter a list of 0s and/or 1s:")
print(turingmachine(user_input))

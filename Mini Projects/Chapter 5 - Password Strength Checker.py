password = input("Enter your password: ")
errors = []
score = 0
errors_to_reperesent = {0: "Length is less than 8",
                        1: "Missing number",
                        2: "Missing uppercase letter"}
score_to_strength = {0: "bad",
                     1: "weak",
                     2: "ok",
                     3: "strong"}

if len(password) < 8:
    errors.append(True)
else:
    errors.append(False)
    score += 1

if any(char.isdigit() for char in password):
    errors.append(False)
    score += 1
else:
    errors.append(True)

if password.lower() == password:
    errors.append(True)
else:
    errors.append(False)
    score += 1

print(f"Your password is {score_to_strength[score]}")
for i in range(len(errors)):
    if errors[i]:
        print(f"- {errors_to_reperesent[i]}")

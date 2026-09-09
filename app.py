# Get the user's name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Check the voting eligibility condition
if age >= 50:
    print(f"Hello {name}! You are eligible to vote.")
else:
    years_left = 50 - age
    print(f"Hello {name}. You will be eligible to vote in {years_left} years.")

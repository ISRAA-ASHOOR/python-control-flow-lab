# Example 0

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

print("------------------------")

# Exercise 1: Vowel or Consonant

def check_letter():
    letter = input('Enter a letter : ').lower()
    print(f'The user entered {letter}')
    if letter == "a":
        print(f'The letter {letter} is a vowel.')
    elif letter == "e":
        print(f'The letter {letter} is a vowel.')
    elif letter == "i":
        print(f'The letter {letter} is a vowel.')
    elif letter == "o":
        print(f'The letter {letter} is a vowel.')
    elif letter == "u":
        print(f'The letter {letter} is a vowel.')
    else:
        print(f'The letter {letter} is a consonant.')

check_letter()

print("------------------------")

# Exercise 2: Old enough to vote?

voting_age = 18

def check_voting_eligibility():
    strage = input('Please enter your age: ')
    age = int(strage)
    if age < 0:
        print('Invalid age , please enter non-negative number')
        return 
    elif age >= 18:
        print('You are eligible to vote.')
    else: 
        print('You are not yet eligible to vote.')


check_voting_eligibility()

print("------------------------")

# Exercise 3: Calculate Dog Years

dog_year_age = 0

def calculate_dog_years():
    str_dog_age = input('Input a dogs age: ')
    dog_age = int(str_dog_age)
    if dog_age < 0:
        print('Invalid age , please enter non-negative number')
        return 
    elif dog_age <= 2:
        dog_year_age = dog_age * 10 
        print(dog_year_age)
    else: 
        dog_year_age = 20 + (dog_age - 2) * 7
        print(dog_year_age)


calculate_dog_years()

print("------------------------")

# Exercise 4: Weather Advice

def weather_advice():
    cold = input('Is it cold (yes/no): ').lower()
    raining = input('Is it raining (yes/no): ').lower()
    if cold == "yes" and raining == "yes" :
        print('Wear a waterproof coat.')
        return 
    elif cold == "yes" and raining == "no":
        print('Wear a warm coat.')
    elif cold == "no" and raining == "yes":
        print('Carry an umbrella.')
    else: 
        print('Wear light clothing.')

weather_advice()
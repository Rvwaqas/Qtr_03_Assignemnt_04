

Prompt='What do you want? '
joke='Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: because they had eggs'
sorry='Sorry I only tell jokes.'

user_input=input(Prompt)
user_input=user_input.strip().lower()

if user_input=='joke':
    print(joke)
else:
    print(sorry)
    
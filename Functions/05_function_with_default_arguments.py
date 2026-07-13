def greet(name="Guest"):
    print("Welcome,",name)
greet()

user_name=input("Enter your name:")
greet(user_name)

'''
^Default parameters in Python allow you to define a function with default values for its arguments. 
^If no value is provided during the function call, the default value is used.
'''

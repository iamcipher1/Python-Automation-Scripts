from datetime import datetime 
user:str= input("Enter your name:")
def greet(user):
 hour = datetime.now().hour
 if 5<= hour< 12:
    greeting= f'Goodmorning {user},don\'t forget to drink some water befor your breakfast!' 
 elif 12<= hour< 17:
    greeting= f'Goodafternoon {user},how\'s your day going'
 elif 17<= hour< 22:
    greeting= f'Goodevening {user},have a goodnight rest'
 else:
    greeting= f'Hey {user} i didn\'t know you were a night crawler'
 return greeting 
print (greet(user))
Hello

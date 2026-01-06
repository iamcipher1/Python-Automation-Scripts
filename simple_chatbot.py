chat_bot : str = 'Alex'
print(f'Hi,I\'m {chat_bot},how can i help you')

while True :
  user_input:str=input('You: ').lower()
  if user_input in ['hi','hello']:
    print (f'{chat_bot}: Hi how can I help you')
  elif user_input in ['add','+']:  
    print (f'{chat_bot}: enter two numbers')
    try:
         num1: float = float(input('number1:'))
         num2: float = float(input('number2:'))
         print (f'{chat_bot}: the sum of {num1}+{num2} = {num1+num2}')    
    except ValueError:
         print (f'{chat_bot}: Oops,please enter a valid number')
  elif user_input in ['goodbye', 'bye']:
    print (f'{chat_bot}: Okay bye ,have a great day')
    break
  else:
    print (f'{chat_bot}: Sorry I don\'t have an answer to that')

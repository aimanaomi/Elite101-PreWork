print('Welcome to Elite101 Chatbot!')
name1= input('What is your name? ')
print("It's nice to meet you",name1)
age1= input("How old are you? ")
print("Wow, you are",age1,"years old!")
print('In which way can I help you today', name1)
choice= input(' 1. How can I reset my password? \n 2. Can I change my username? \n 3. Where can I log in? \n 4. Exit the conversation. \n Enter the number of your choice: ')
if choice == '1':
  print('Enter your email address, a link will be sent to reset your password.')
elif choice == '2':
  print('Enter your email address to login, you will be able to view and/or change your username in your account.')
elif choice == '3':
  print('You will be able to log at the home page of the site, click the icon in the top left corner of the screen.')
elif choice == '4':
  print('Goodbye', name1,'I hope I was able to help!')
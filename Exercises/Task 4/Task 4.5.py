i=0
while i<5:
   username=input('Username: ')
   password=input('Password: ')
   if username=='python' and password =='rules':
       print('Welcome')
       break
   else:
       print('Username or password is wrong. Please try again.')
       i+=1
if i==5:
    print('Access denied')





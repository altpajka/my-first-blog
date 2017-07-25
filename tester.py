print("Hello Paul")
#-----------------------------------
doga=8
jezevčík=3
if doga < jezevčík:
    print("Jo, doga je větší!")
else:
    print("No tak to není")
#-----------------------------------
name="gob"
if name == "Tonda":
    print("Hey Tonda")
elif name == "Rupert":
    print("Hi Rupert")
else:
    print("Hey anonymous")
#-----------------------------------
volume = 57
if volume < 20:
     print("Je to dost potichu.")
elif 20 <= volume < 40:
     print("Jako hudba v pozadí dobré.")
elif 40 <= volume < 60:
     print("Skvělé, slyším všechny detaily.")
elif 60 <= volume < 80:
     print("Dobré na party.")
elif 80 <= volume < 100:
     print("Trochu moc nahlas!")
else:
    print("Krvácí mi uši!")
#-----------------------------------
def hi():
     print('Hi there!')
     print('How are you?')

hi()
#-----------------------------------
def hi(name):
     if name == 'Ola':
         print('Hi Ola!')
     elif name == 'Sonja':
         print('Hi Sonja!')
     else:
         print('Hi anonymous!')

hi("Ola")
#better?version---------------------
def hi(name):
     print('Hi ' + name + '!')

hi("Rachel")
#-----------------------------------
def hi(name):
     print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
     hi(name)
     print('Next girl')
#-----------------------------------
for i in range(1, 6):
     print(i)
#-----------------------------------

#-----------------------------------

#-----------------------------------

#-----------------------------------

#-----------------------------------

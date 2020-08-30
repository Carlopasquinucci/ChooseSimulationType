import tkinter as tk
import pymsgbox
import os

"""
if marine --> multyphase

if electronics
	temperature is > then 100°C? --> radiation
	
	do you are interested also in solid --> coniugate heat transfer
	not interested in solid --> convective heat transfer
	
if architecture
		speed is > then 300 km/h --> compressible
		else --> incompressible
		
if manifacturing
		speed is > then 300 km-7h --> compressible
		
		are some temperature changes? -->  temperature is > then 100°C? --> radiation
										do you are interested also in solid --> coniugate heat transfer
										not interested in solid --> convective heat transfer
										
		are there more fluids or some particells? --> multyphase
"""
def automotive():
	yesno=pymsgbox.confirm('The speed is bigger than 100 m/s or 370 km/h?' , '' , 'YN')
	if yesno=='Y':
				pymsgbox.alert('You have to setup a compressible simulation')
	else:
				pymsgbox.alert('You have to setup a incompressible simulation')			


def architecture():
	yesno=pymsgbox.confirm('The speed is bigger than 100 m/s or 370 km/h?' , '' , 'YN')
	if yesno=='Y':
				pymsgbox.alert('You have to setup a compressible simulation')
	else:
				pymsgbox.alert('You have to setup a incompressible simulation')	

def electronics():

	yesno=pymsgbox.confirm('The temperature is bigger than 100 C degree?', '' , 'YN')
	if yesno=='Y':
				pymsgbox.alert('You have to activate the radiation too')
	else:
				pymsgbox.alert("You don't have to activate the radiation")
	yesno=pymsgbox.confirm('Are you interested in simulate also the solid part?', '' , 'YN')
	if yesno=='Y':
				pymsgbox.alert('You have to use coniugate heat transfer simulation')
	else:
				pymsgbox.alert("You dont' have to use coniugate heat transfer simulation")
				
"""		
def manufactoring():

	yesno=pymsgbox.confirm('The temperature is bigger than 100* C?, '' , 'YN')
	if yesno=='Y':
				pymsgbox.alert('You have to activate the radiation too')
	else:
				pymsgbox.alert("You don't have to activate the radiation")
	yesno=pymsgbox.confirm('Are you interested in simulate also the solid part?', '' , 'YN')
	if yesno=='Y':
				pymsgbox.alert('You have to use coniugate heat transfer simulation')
	else:
				pymsgbox.alert("You dont' have to use coniugate heat transfer simulation")

"""				
				
def marine():

	yesno=pymsgbox.confirm('Are you interested in both fluid (air and water)?', '' , 'YN')
	if yesno=='Y':
				pymsgbox.alert('You have to use the multyphase simulation')
	else:
				pymsgbox.alert('You have to use the monofase simulation')


def help():
    pymsgbox.alert(' Choose the field of the simulation you want ro run')




#main
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()


commandhelp = tk.Button(frame,
                   text="Help",
				   fg="red",
                   command=help)
commandhelp.pack(side=tk.RIGHT)


auto = tk.Button(frame,
                   text='Automotive',
				   fg='blue',
                   command=automotive)
auto.pack(side=tk.LEFT)


arch = tk.Button(frame,
                   text='Architecture',
				   fg='blue',
                   command=architecture)
arch.pack(side=tk.LEFT)

elec = tk.Button(frame,
                   text='Electronics',
				   fg='blue',
                   command=electronics)
elec.pack(side=tk.LEFT)

"""
manifact = tk.Button(frame,
                   text='Manifacturing',
                   command=manifacturing)
manifact.pack(side=tk.RIGHT)
"""

mar = tk.Button(frame,
                   text='Marine',
				   fg='blue',
                   command=marine)
mar.pack(side=tk.LEFT)

root.mainloop()
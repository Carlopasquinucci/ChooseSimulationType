import tkinter as tk
import pymsgbox
import os

def automotive():
	yesno=pymsgbox.confirm('The speed is bigger than 100 m/s or 370 km/h?' , '' , 'YN')
	if yesno=='Y':
				pymsgbox.alert('You have to setup a compressible simulation')
				solver=pymsgbox.confirm('Are you interested also in the variation of the quantities with the time?' , '' , 'YN')
				if solver=='Y':
					pymsgbox.alert('You have to use the rhoPimpleFoam solver')
				else:
					pymsgbox.alert('You have to use the rhoSimpleFoam solver')	
	else:
				pymsgbox.alert('You have to setup a incompressible simulation')
				solver=pymsgbox.confirm('Are you interested also in the variation of the quantities with the time?' , '' , 'YN')
				if solver=='Y':
					pymsgbox.alert('You have to use the pimpleFoam solver')
				else:
					pymsgbox.alert('You have to use the simpleFoam solver')


def architecture():
	yesno=pymsgbox.confirm('The speed is bigger than 100 m/s or 370 km/h?' , '' , 'YN')
	if yesno=='Y':
				pymsgbox.alert('You have to setup a compressible simulation')
				solver=pymsgbox.confirm('Are you interested also in the variation of the quantities with the time?' , '' , 'YN')
				if solver=='Y':
					pymsgbox.alert('You have to use the rhoPimpleFoam solver')
				else:
					pymsgbox.alert('You have to use the rhoSimpleFoam solver')	
	else:
				pymsgbox.alert('You have to setup a incompressible simulation')
				solver=pymsgbox.confirm('Are you interested also in the variation of the quantities with the time?' , '' , 'YN')
				if solver=='Y':
					pymsgbox.alert('You have to use the rhoPimpleFoam solver')
				else:
					pymsgbox.alert('You have to use the rhoSimpleFoam solver')

def electronics():

	yesno=pymsgbox.confirm('Are you interested in simulate also the solid part?', '' , 'YN')
	if yesno=='Y':
				solver=pymsgbox.confirm('Is the temperature bigger than 100 degree Celsius?', '' , 'YN')
				if solver=='Y':
					pymsgbox.alert('You have to add radiation')
					solver=pymsgbox.confirm('Are you interested also in the variation of the quantities with the time?' , '' , 'YN')
					if solver=='Y':
						pymsgbox.alert('You have to use the chtMultiRegionFoam solver')
					else:
						pymsgbox.alert('You have to use the chtMultiRegionSimpleFoam solver')
				else:
					pymsgbox.alert("You don't have to add radiation")
					solver=pymsgbox.confirm('Are you interested also in the variation of the quantities with the time?' , '' , 'YN')
					if solver=='Y':
						pymsgbox.alert('You have to use the chtMultiRegionFoam solver')
					else:
						pymsgbox.alert('You have to use the chtMultiRegionSimpleFoam solver')
	else:
				pymsgbox.alert("You don't have to simulate the conjugate heat transfer")	
				solver=pymsgbox.confirm('Are you interested also in the variation of the quantities with the time?' , '' , 'YN')
				if solver=='Y':
					pymsgbox.alert('You have to use the buoyantPimpleFoam solver')
				else:
					pymsgbox.alert('You have to use the buoyantSimpleFoam solver')		
				
def marine():

	yesno=pymsgbox.confirm('Are you interested in both fluid (air and water)?', '' , 'YN')
	if yesno=='Y':
				pymsgbox.alert('You have to use the multyphase simulation')
				pymsgbox.alert('You have to use the interFoam solver')
	else:
				pymsgbox.alert('You have to use the monophase simulation')
				pymsgbox.alert('Choose the automotive button')


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

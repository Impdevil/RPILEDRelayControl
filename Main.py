
#import RPI.GPIO as GPIO
import tkinter as TK
from tkinter import *

######################################################
#
#		Arran Peter McPherson Blows
#
# Led relay with UI control for raspberry PI 3B
#
# using the RPI python lib to access the Raspberry PI interface
# using the tkinker lib to create the UI
# the relay is the main object of this code 
#
#
#
######################################################

#set the channel selection type to use the board set,rather than the SOC BCM numbers which can change
#GPIO.setmode(GPIO.BROAD)

#0 led 1
#1 led 2
#2 led 3
#3 led 4
#4 led 5
#5 Rainbow
relayset = [0,1,2,3,4,5]
buttonPressedValue = [False,False,False,False,False,False,False,False]

def InitialSetUpRGPIO():
	i=0
	while i < len(relayset):
		#GPIO.output(relayset[0],0)
		i=i+1
	
	

#readible way of toggleing on or off a relay as well as checking their current state
def SwitchRelay(relay, switchBool):
	global buttonPressedValue
	if switchBool == True:## check and switch the GPIO Ports
		if buttonPressedValue[relay] == True :#or GPIO.input(relay) == True:
			#GPIO.output(relay,0)
			print ("relay " + str(relay) + " is set to false")
			buttonPressedValue[relay] = False
			return False
		elif buttonPressedValue[relay] == False :#or GPIO.input(relay) == False:
			print ("relay " + str(relay) + " is set to true")
			#GPIO.output(relay,1)
			buttonPressedValue[relay] = True
			return True
	if switchBool == False: #check only
		if buttonPressedValue[relay] == True :#or GPIO.input(relay) == True:
			print ("relay " + str(relay) + " is set to true 1")
			return True
		elif buttonPressedValue[relay] == False :#or GPIO.input(relay) == False:
			print ("relay " + str(relay) + " is set to false 1")
			return False

			
			

def SwitchRelayAll(setToo):
	global buttonPressedValue
	if setToo ==True: 
		for i in range((len(relayset) - 1)):
			if buttonPressedValue[i] == False:
				#GPIO.output(relayset[i],1)
				buttonPressedValue[i] = True
		return True
	elif setToo == False:
		for i in range((len(relayset) - 1)):
			if buttonPressedValue[i] == True:
				#GPIO.output(relayset[i],1)
				buttonPressedValue[i] = False
		return False


def ButtonPress(buttonPressed):
	if buttonPressed <= 4:
		if SwitchRelay(buttonPressed, True) == True:
			#set the button to being coloured/On(Coloured coz im not an idiot!!!!)
			print("do once 1")
			btn[buttonPressed].config(relief="sunken")
		elif SwitchRelay(buttonPressed, False) == False:
			#set the button to being off 
			print("do once 2")
			btn[buttonPressed].config(relief="raised")
	#button 6 rainbow setting relay 5
	elif buttonPressed == 5: 
		if SwitchRelay(buttonPressed, True) == True:
			#set the button to being on
			print("do once 3")
			btn[buttonPressed+1].config(relief="sunken")
		elif SwitchRelay(buttonPressed, False) == False:
			#set the button to being off 
			print("do once 4")
			btn[buttonPressed+1].config(relief="raised")
	elif buttonPressed == 6:
		print("All on " + str(buttonPressed))
		SwitchRelayAll(True)
		for i in range(len(relayset) -1):
			btn[i].config(relief="sunken")
			
	elif buttonPressed == 7:
		print("All off " + str(buttonPressed))
		SwitchRelayAll(False)
		for i in range(len(relayset) - 1):
			btn[i].config(relief="raised")
	else:
		print ("Default")

		
##button for first relay
def Button0IsPress():
	ButtonPress(relayset[0])
	
## button for second Relay
def Button1IsPress():
	ButtonPress(relayset[1])


#button for third relay
def Button2IsPress():
	ButtonPress(relayset[2])


#button for fourth relay
def Button3IsPress():
	ButtonPress(relayset[3])

#button for fifth relay	
def Button4IsPress():
	print("potato " + str(relayset[4]))
	ButtonPress(relayset[4])
	

#button for Relays all on/off 	
def Button5IsPress():
	ButtonPress(6)
	

#button for Rainbow effect	
def Button6IsPress():
	ButtonPress(relayset[5])

#button to turn all relays off
def Button7IsPress():
	ButtonPress(7)



		
def InitalSetup():
	window = TK.Tk()
	window.title = ("LED Control")
	frame = TK.Frame(window)
	frame.pack()
	window.configure(background = "black")
	global btn 
	btn=[]
	#led1
	btn.insert(0,TK.Button(frame,text="LED 1" , width=5, command=Button0IsPress))
	btn[0].config(relief="raised")
	btn[0].pack(side="left")
	#led2
	btn.insert(1,TK.Button(frame,text="LED 2" , width=5, command=Button1IsPress))
	btn[1].config(relief="raised")
	btn[1].pack(side="left")
	#led3
	btn.insert(2,TK.Button(frame,text="LED 3" , width=5,command=Button2IsPress))
	btn[2].config(relief="raised")
	btn[2].pack(side="left")
	#led4
	btn.insert(3,TK.Button(frame,text="LED 4" , width=5, command=Button3IsPress))
	btn[3].config(relief="raised")
	btn[3].pack(side="left")
	#led5
	btn.insert(4,TK.Button(frame,text="LED 5" , width=5, command=Button4IsPress))
	btn[4].config(relief="raised")
	btn[4].pack(side="left")
	#All LEDs on no toggle
	btn.insert(5,TK.Button(frame,text="All On" , width=5, command=Button5IsPress))
	btn[5].config(relief="raised")
	btn[5].pack(side="left")
	#Rainbow Effect on
	btn.insert(6,TK.Button(frame,text="Rainbow" , width=5, command=Button6IsPress))
	btn[6].config(relief="raised")
	btn[6].pack(side="left")
	#All Off no toggle
	btn.insert(7,TK.Button(frame,text="All Off" , width=5, command=Button7IsPress))
	btn[7].config(relief="raised")
	btn[7].pack(side="left")

	
InitialSetUpRGPIO()
InitalSetup()
TK.mainloop()

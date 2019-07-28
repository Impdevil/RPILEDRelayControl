
#import RPI.GPIO as GPIO
from tkinter import *
import tkinter as TK


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

#change the numbers to the correct gpoi pins!!!
relayset = [0,
	1,	#led 1
	2,	#led 2
	3,	#led 3
	4,	#led 4
	5]	#Rainbow
	
#toggle option for button UI
buttonPressedValue = [False,	#button 0
	False,	# 	button 1
	False,	#	button 2
	False,	#	button 3
	False,	#	button 4
	False,	#	button 5
	False,	#	button 6
	False]	#	button 7

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
		for i in range((len(relayset))):
			if buttonPressedValue[i] == True:
				#GPIO.output(relayset[i],0)
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
		for i in range(len(relayset)+1):
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
	

#button for Relays all on	
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
	window.title("LED Control")
	window.geometry('{}x{}'.format(480,320))
	frame = TK.Frame(window)
	frame.pack()
	buttonFrame0 = TK.Frame(frame, padx=2, pady=0)
	buttonFrame0.pack(side="left")
	buttonFrame1 = TK.Frame(frame, padx=2,pady=4)
	buttonFrame1.pack(side="right")
	window.configure()
	lbl = TK.Label(buttonFrame0,text="Led Control")
	lbl.pack(side="top")
	global btn 
	btn=[]
	#led1
	btn.insert(0,TK.Button(buttonFrame0,text="LED 1" , height=6, width=7, command=Button0IsPress))
	btn[0].config(relief="raised")
	btn[0].pack(side="left")
	#led2
	btn.insert(1,TK.Button(buttonFrame0,text="LED 2" ,height=6, width=7, command=Button1IsPress))
	btn[1].config(relief="raised")
	btn[1].pack(side="left")
	#led3
	btn.insert(2,TK.Button(buttonFrame0,text="LED 3" ,height=6, width=7,command=Button2IsPress))
	btn[2].config(relief="raised")
	btn[2].pack(side="left")
	#led4
	btn.insert(3,TK.Button(buttonFrame0,text="LED 4" ,height=6, width=7, command=Button3IsPress))
	btn[3].config(relief="raised")
	btn[3].pack(side="left")
	#led5
	btn.insert(4,TK.Button(buttonFrame0,text="LED 5" ,height=6, width=7, command=Button4IsPress))
	btn[4].config(relief="raised")
	btn[4].pack(side="left")
	#All LEDs on no toggle
	btn.insert(5,TK.Button(buttonFrame1,text="All On" ,height=3, width=6, command=Button5IsPress))
	btn[5].config(relief="raised")
	btn[5].pack(side="top")
	#Rainbow Effect on
	btn.insert(6,TK.Button(buttonFrame0,text="Rainbow" , height=6, width=9, command=Button6IsPress))
	btn[6].config(relief="raised")
	btn[6].pack(side="left")
	#All Off no toggle
	btn.insert(7,TK.Button(buttonFrame1,text="All Off" ,height=3, width=6, command=Button7IsPress))
	btn[7].config(relief="raised")
	btn[7].pack(side="bottom")

	
InitialSetUpRGPIO()
InitalSetup()
TK.mainloop()

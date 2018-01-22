from gpiozero import LED, Button
from time import sleep
from random import uniform

io_button1 = 14
io_button2 = 15
io_led = 4


class player:
	
	def __init__(self, name, io_button):
		self.playername = name
		self.io_button = io_button

	def getName(self):
		return self.playername

	def getButton(self):
		return self.io_button


class board:

	def __init__(self):
		self.button1 = Button(io_button1)
		self.button2 = Button(io_button2)
		self.light = LED(io_led)

	def pressed(player):
		if player.getButton() == 14:
			print(player.getName())
		else:
			print(player.getName())

	def start(self):
		sleep(uniform(5,10))
		light.on()
		


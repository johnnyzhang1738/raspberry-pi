from gpiozero import LED, Button
from time import sleep
from random import uniform

io_button1 = 14
io_button2 = 15
io_led = 4


class player:
	
	def __init__(self, name, io_port):
		self.playername = name
		self.button_ID = io_port

	def getName(self):
		return self.playername

	def getID(self):
		return self.button_ID


class board:

	def __init__(self, button1, button2):

		self.light = LED(io_led)
		self.is_pressed = False
		self.player1_button = Button(button1)
		self.player2_button = Button(button2)

	def pressed(self, player):
		print(player.getName())
		self.is_pressed = True
		self.light.off()

	def start(self, p1, p2):
		sleep(uniform(5,10))
		self.light.on()
		self.player1_button.when_pressed = self.pressed(p1)
		self.player2_button.when_pressed = self.pressed(p2)

def main():
	
	player1 = player("J", io_button1)
	player2 = player("Z ", io_button2)
	b = board(io_button1, io_button2)
	b.start(player1, player2)


if __name__ == '__main__':
	main()

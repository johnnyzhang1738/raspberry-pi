from gpiozero import LED, Button
from time import sleep
from random import uniform

io_button1 = 14
io_button2 = 15
io_led = 4


class player:
	
	def __init__(self, name, io_button):
		self.playername = name
		self.io_button = Button(io_button)


	def getName(self):
		return self.playername

	def getButton(self):
		return self.io_button


class board:

	def __init__(self, p1, p2):
		self.button1 = Button(io_button1)
		self.button2 = Button(io_button2)
		self.light = LED(io_led)
		self.is_pressed = False
		self.player1 = p1
		self.player2 = p2

	def pressed(player):
		if player.getButton() == 14:
			print(player.getName())
		else:
			print(player.getName())
		is_pressed = True
		light.off()

	def start(self):
		sleep(uniform(5,10))
		light.on()
		button1.when_pressed = pressed(player1)
		button2.when_pressed = pressed(player2)


if __name__ == '__main__':
	main()

def main():
	b = board()
	player1 = player(input("Enter player 1 name here"), io_button1)
	player2 = player(input("Enter player 2 name here"), io_button2)

	b.start()


	exit(0)

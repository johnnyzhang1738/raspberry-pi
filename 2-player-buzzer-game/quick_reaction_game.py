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
		self.score_player1 = 0
		self.score_player2 = 0

	def pressed(self, button):
		if button.pin.number == io_button1:
			self.score_player1 += 1
		else:
			self.score_player2 += 1
		self.light.off()
		print("Score is: Player1 @ "+str(self.score_player1)+" vs. Player2 @ "+str(self.score_player2))

	def start(self, p1, p2):

		while max(self.score_player2,self.score_player1) < 3:
			sleep(uniform(4,7))
			self.light.on()
			self.player1_button.when_pressed = self.pressed
			self.player2_button.when_pressed = self.pressed
		print("game over")

def main():
	
	player1 = player(("Enter player 1 name "), io_button1)
	player2 = player(("Enter player 2 name "), io_button2)
	b = board(io_button1, io_button2)
	b.start(player1, player2)


if __name__ == '__main__':
	main()

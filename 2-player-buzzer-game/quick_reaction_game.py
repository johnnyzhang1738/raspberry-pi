from gpiozero import LED, Button
from time import sleep
from random import uniform

io_button1 = 14
io_button2 = 15
io_led = 4
p1_name = input("Enter Player 1 Name Here: ")
p2_name = input("Enter Player 2 Name Here: ")

class Player:
	
	def __init__(self, name, io_port):
		self.playername = name
		self.button_ID = io_port

	def getName(self):
		return self.playername

	def getID(self):
		return self.button_ID


class Board:

	def __init__(self, button1, button2):

		self.light = LED(io_led)
		self.is_pressed = False
		self.player1_button = Button(button1)
		self.player2_button = Button(button2)
		self.score_player1 = 0
		self.score_player2 = 0

	def pressed(self, button):
		
		if (self.is_pressed==True):
				return
		if button.pin.number == io_button2:
			self.score_player1 += 1
		else:
			self.score_player2 += 1
		self.light.off()
		
		print("Score is: "+ str(p1_name)+ " @ "+str(self.score_player1)+" vs. "+str(p2_name)+" @ "+str(self.score_player2))
		self.is_pressed = True
				
	def start(self, p1, p2):
        
		while max(self.score_player2,self.score_player1) < 3:
			self.is_pressed = False
			sleep(uniform(4,7))
			self.light.on()
			self.player1_button.when_pressed = self.pressed
			self.player2_button.when_pressed = self.pressed
		print("game over")

def main():

	player1 = Player(p1_name, io_button1)
	player2 = Player(p2_name, io_button2)
	b = Board(io_button1, io_button2)
	b.start(player1, player2)


if __name__ == '__main__':
	main()

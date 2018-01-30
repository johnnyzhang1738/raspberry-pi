import unittest
from quick_reaction_game import Player, Board
from gpiozero import LED

class PersonTest(unittest.TestCase, Player):
	
	def setUp(self):
		Player.__init__(self,"test1",100)
	
	def testName(self):
		self.assertEqual(Player.getName(self), "test1")

	@unittest.expectedFailure
	def test_IO_port_failure(self):
		self.assertEqual(Player.getID(self), 1, "broken")

	def test_ID(self):
		self.assertEqual(Player.getID(self), 100)
	
	def tearDown(self):
		del self
		
def suite_person():
	suite = unittest.TestSuite()
	suite.addTest(PersonTest('testName'))
	suite.addTest(PersonTest('test_IO_port_failure'))
	suite.addTest(PersonTest('test_ID'))

	return suite

class BoardTest(unittest.TestCase, Board):
	def setUp(self):
		Board.__init__(self, 20, 21)
		p1 = Player("test_name1",20)
		p2 = Player("test_name2", 21)
		
	def test_init_buttons(self):
		self.assertEqual(Board.player1_button,20)
		self.assertEqual(Board.plyer2_button,21)
		self.assertEqual(Board.is_pressed, False)
		self.assertIs(Board.light, LED)

	def test_init_players(self):
		self.assertEqual(Board.score_player1, 0)
		self.assertEqual(Board.score_player2, 0)

	def test_pressed_func(self):
		Board.pressed(20)
		self.assertEqual(Board.score_player1,1)
	
	def tearDown(self):
		del self

def suite_board():
	suite = unittest.TestSuite()
	suite.addTest(BoardTest('test_init_buttons'))
	suite.addTest(BoardTest('test_init_players'))
	suite.addTest(BoardTest('test_pressed_func'))

	return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite_person())
    runner.run(suite_board())

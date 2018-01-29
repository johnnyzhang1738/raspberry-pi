import unittest
from quick_reaction_game import Player, Board

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
		
	def test_button_press(self):
		pass
	
	def tearDown(self):
		del self


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite_person())

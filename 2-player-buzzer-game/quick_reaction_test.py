import unittest
from quick_reaction_game import Player, Board

class PersonTest(unittest.TestCase, Player):
    @classmethod
    def setUpClass(cls):
        cls.Player.__init__("test1",10)
    
    def test_name(self):
    	self.assertEqual(self.Player.getName(), "test1")

    @unittest.expectedFailure
    def test_IO_port_failure(self):
    	self.assertEqual(person.getID(), 1, "broken")

    @classmethod
    def tearDownClass(cls):
    	cls.person.dispose()

def suite_person():
    suite = unittest.TestSuite()
    suite.addTest(PersonTest('test_name'))
    #suite.addTest(PersonTest('test_IO_port_failure'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite_person())

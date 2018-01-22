import unittest
import quick_reaction_game

class PersonTest(unittest.TestCase):
    def setUp(self):
    	self.person = Person("test1",10)

    def testName(self):
    	self.assertEqual(Person.getName(), "test1")

    def testIOport(self):
    	self.assertEqual(Person.getID(), 10)

    def tearDown(self):
    	self.person.dispose()

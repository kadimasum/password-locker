import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self) -> None:
        self.new_user = User("John", "@johnd", "jo@m.com", "073535213", "password")
    

    def tearDown(self) -> None:
        User.users = []


    def test_user_instance_created_successfully(self):
        self.assertTrue(isinstance(self.new_user, User))


    def test_user_saved(self):
        self.new_user.save_user()
        self.assertEqual(1, len(User.users))
        self.assertEqual( self.new_user.name, User.users[0].name)
        self.assertEqual(201, self.new_user.save_user())

    


if __name__ == "__main__":
    unittest.main()
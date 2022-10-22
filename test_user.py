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


    def test_find_user(self):
        self.new_user.save_user()
        self.assertEqual(User.find_user(self.new_user.name), self.new_user)


    def test_delete_user(self):
        self.new_user.save_user()
        other_user = User("Brenda", "@brew","brenda@m.com", "073832272","password")
        other_user.save_user()
        User.delete_user(other_user.name)
        User.delete_user(self.new_user.name)
        self.assertEqual(0, len(User.users))


    def test_update_name(self):
        self.new_user.save_user()
        self.new_user.update_name(self.new_user.name, "Waithera")
        self.assertEqual("Waithera", self.new_user.name)

    def test_update_number(self):
        self.new_user.save_user()
        self.new_user.update_phone_number(self.new_user.name, "071234567")
        self.assertEqual("071234567", self.new_user.phone_number)

    def test_update_email(self):
        self.new_user.save_user()
        self.new_user.update_email(self.new_user.name, "blal@m.com")
        self.assertEqual("blal@m.com", self.new_user.email)


    def test_update_password(self):
        self.new_user.save_user()
        self.new_user.update_password(self.new_user.name, "changedpassword")
        self.assertEqual("changedpassword", self.new_user.password)

    
    def test_get_all_users(self):
        self.new_user.save_user()
        other_user = User("Brenda", "@brew","brenda@m.com", "073832272","password")
        other_user.save_user()
        self.assertEqual(2, len(User.all_users()))
        


if __name__ == "__main__":
    unittest.main()
import unittest
from User import User


class UserTestCase(unittest.TestCase):
    def test_basic(self):
        user = User('user1', 'askfgha;g', email='user1@gmail.com')
        # assert u.username == 'user1'
        self.assertEqual(user.username, 'user1')
        # assert u.pass_hash == 'askfgha;g'
        self.assertEqual(user.pass_hash, hash('askfgha;g'))
        # assert u.email == 'user1@gmail.com'
        self.assertEqual(user.email, 'user1@gmail.com')

    def test_skip_optional(self):
        user = User('user2', 'askfgha;g', email='user1@gmail.com', fax='+380321234567')
        # assert not hasattr(u2, 'fax')
        self.assertFalse(hasattr(user, 'fax'))
        #self.assertEqual(hasattr(user, 'fax'), False)

    def test_create_with_password(self):
        user = User('name', password = 'askfgha')
        pass_hash = hash('askfgha')
        self.assertEqual(user.password, '<Password with hash {}>'.format(pass_hash))
        self.assertEqual(user.pass_hash, pass_hash)

#    def test_set_password(self):
#        user = User('name', password = 'hgjdsk2')
#        pass_hash = hash('hgjdsk2')
#        user.password()
#        self.assertEqual(user.password, pass_hash)




if __name__ == '__main__':
    unittest.main()

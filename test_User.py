import unittest
from User import User


class UserTestCase(unittest.TestCase):
    def test_basic(self):
        user = User('user1', 'askfgha;g', email='user1@gmail.com')
        self.assertEqual(user.username, 'user1')
        self.assertEqual(user.pass_hash, hash('askfgha;g'))
        self.assertEqual(user.email, 'user1@gmail.com')

    def test_skip_optional(self):
        user = User('user2', 'askfgha;g', email='user1@gmail.com', fax='+380321234567')
        self.assertFalse(hasattr(user, 'fax'))

    def test_create_with_password(self):
        user = User(username='name', password='qwerty')
        pass_hash = hash('qwerty')
        self.assertEqual(
            user.password,
            '<Password with hash {}>'.format(pass_hash)
        )
        self.assertEqual(user.pass_hash, pass_hash)

    def test_set_password(self):
        user = User(username='name', password='')
        user.password = 'qwerty2'
        self.assertEqual(user.pass_hash, hash('qwerty2'))


if __name__ == '__main__':
    unittest.main()

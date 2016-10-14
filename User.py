#class Password():
#    def __get__(self, obj, objtype):
#        print('Calling __get__')
#        print('obj is {}'.format(obj))
#        print('odjtype is {}'.format(objtype))
#        return 42
#
#    def __set__(self, obj, value):
#        print('Calling __set__')
#        print('obj is {}'.format(obj))
#        print('value is {}'.format(value))

#    def __del__(self):
#        print('Calling __get__')
#        print('obj is {}'.format(obj))
#        print('objtype is {}'.format(objtype))

class User:
    """
    Basic class for web shop customer
    """
    optional_fields = {'email', 'fname', 'lname', 'address', 'bd', 'phone'}

    def __init__(self, username, password, **kwargs):
        self.username = username
        self.password = password
        for field in kwargs:
            if field in User.optional_fields:
                setattr(self, field, kwargs[field])

#    def set_password(self, password):
#       self.pass_hash = hash(password)

#    def get_password(self):
#        return '<Password with hash {}>'.format(self.pass_hash)

#    password = property(get_password, set_password)

    @property
    def password(self):
        return '<Password with hash {}>'.format(self.pass_hash)

    @password.setter
    def password(self, value):
        self.pass_hash = hash(value)

#user = User('name', 'askfgha')
#print(user.password)
#user.password = 'askfgha2'
#print(user.password)

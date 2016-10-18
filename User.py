from hashlib import md5


class User(object):
    """
    Basic class for web shop customer. Optional arguments handled via
        `optional_fields`. No data validation so far.
    Password is never stored in plain texts. Settings password triggers
        descriptor hashing it with md5 algorithm and storing only hash
    """
    optional_fields = {'email', 'fname', 'lname', 'address', 'bday', 'phone'}

    def __init__(self, username, password, **kwargs):
        self.username = username
        self.password = password
        for field in kwargs:
            if field in User.optional_fields:
                setattr(self, field, kwargs[field])

    @property
    def password(self):
        return '<Password with hash {}>'.format(self.pass_hash)

    @password.setter
    def password(self, value):
        self.pass_hash = md5(value.encode()).hexdigest()

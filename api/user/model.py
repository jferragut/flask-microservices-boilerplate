class User(object):
    def __init__(self, user_id=None, username=None, first_name=None, last_name=None, 
                friendly_name="", password=None, password_hint=None):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.friendly_name = friendly_name
        self.password = password
        self.password_hint = password_hint

    @staticmethod
    def from_dict(source):
        pass

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'friendly_name': self.friendly_name,
            'password': self.password,
            'password_hint': self.password_hint
        }

    def __repr__(self):
        return(
            u'User(username={}, first_name={}, last_name={}, friendly_name={}, password={}, password_hint={})'
            .format(self.username, self.first_name, self.last_name, self.friendly_name,
                    self.password, self.password_hint))

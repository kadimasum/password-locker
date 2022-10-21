import http

class User:
    users = []
    def __init__(self, name, username, email, phone_number, password):
        self.name = name
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.password = password


    def save_user(self):
        User.users.append(self)
        return http.HTTPStatus.CREATED
    

    @classmethod
    def find_user(cls, name):
        for user in cls.users:
            if user.name == name:
                return user
            else: raise FileNotFoundError("User does not exist!")


    @classmethod
    def delete_user(cls, name):
        for i in range(len(cls.users)):
            if cls.users[i].name == name:
                cls.users.pop(i)
                return http.HTTPStatus.OK


    @classmethod
    def update_name(cls, initial_name, new_name):
        user = cls.find_user(initial_name)
        user.name = new_name
        return user


    @classmethod
    def update_phone_number(cls, name, phone_number):
        user = cls.find_user(name)
        user.phone_number = phone_number
        return user

    @classmethod
    def update_email(cls, name, email):
        user = cls.find_user(name)
        user.email = email
        return user

    @classmethod
    def update_user_name(cls, name, username):
        user = cls.find_user(name)
        user.username = username
        return user

    @classmethod
    def update_user_name(cls, email, password):
        user = cls.find_user(email)
        user.password = password
        return user

    
        
    



    
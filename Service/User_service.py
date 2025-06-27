#from model.User import user
from model.User import user

class User_Service:
    def __init__(self):
        self.users={}

    def add_user(self,id,name,email):
        user=user(name,id,email)
        self.users[id]=user
        return user
    
    def get_user(self,id):
        return self.users.get(id)

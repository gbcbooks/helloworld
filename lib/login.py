from lib import paramiko

class Login():
    
    def __init__(self, dirname, taskid, projectnamess):
        self._dirname = dirname
        self._taskid = taskid
        self._projectnames = projectnamess
    

    def login(self, dirname):
        print("this is login")

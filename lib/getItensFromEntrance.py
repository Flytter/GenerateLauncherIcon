class getIntens:

    def __init__(self):
        fileDirectory=''
    
    def getFile(self, name):
        try:
            self.fileDirectory = './entrance/'+name
            return True
        except:
            return False

class getIntens:

    def __init__(self):
        path ='entrance/'
        fileList = []
    
    def getFile(self):
        try:
            self.fileList = [f for f in glob.glob(self.path+'*.png')]
            return True
        except:
            return False

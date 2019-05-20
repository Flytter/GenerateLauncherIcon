import glob

class getItens:

    def __init__(self):
        self.fileList = []
    
    def getFile(self, path):
        self.fileList = [f for f in glob.glob(path+'/entrance/'+'*.png')]
        return self.fileList
        
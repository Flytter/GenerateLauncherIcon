from lib.getItensFromEntrance import *
import os


class controllerImg:
    
    def __init__(self, path, arguments):
        self.itens = getItens()
        self.path = path
        self.nameFolder = arguments
        self.listItens = getItens().getFile(path)

    def resizeImage(self):
        for i in self.listItens:
            self.createFolder(self.path, self.nameFolder[1])
    

    def createFolder(self, path, countName):
        os.mkdir(path+'/output/'+countName)
        os.mkdir(path+'/output/'+countName+'/android/')
        os.mkdir(path+'/output/'+countName+'/IOS/')
        self.createAndroidFolder(path,countName)
        self.createIOSFolder(path,countName)

    def createAndroidFolder(self,path,countName):
        os.mkdir(path+'/output/'+countName+'/android/mipmap-hdpi')
        os.mkdir(path+'/output/'+countName+'/android/mipmap-mdpi')
        os.mkdir(path+'/output/'+countName+'/android/mipmap-xhdpi')
        os.mkdir(path+'/output/'+countName+'/android/mipmap-xxhdpi')
        os.mkdir(path+'/output/'+countName+'/android/mipmap-xxxhdpi')
        os.mkdir(path+'/output/'+countName+'/android/GooglePlay')
    
    def createIOSFolder(self,path,countName):
        os.mkdir(path+'/output/'+countName+'/IOS/Icons')
        os.mkdir(path+'/output/'+countName+'/IOS/AppStore')



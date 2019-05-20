from lib.getItensFromEntrance import *
import cv2
import os

class controllerImg:
    
    def __init__(self, path, arguments):
        self.itens = getItens()
        self.path = path
        self.nameFolder = arguments
        self.listItens = getItens().getFile(path)
        self.img = cv2.imread(self.listItens[0])
        self.androidFolder = self.path+'/output/'+self.nameFolder[1]+'/android'

    def resizeImage(self):

        for i in self.listItens:
            self.createFolder(self.path, self.nameFolder[1])
            self.saveAndroid(72, 72, self.androidFolder, 'mipmap-hdpi')
            self.saveAndroid(48, 48, self.androidFolder, 'mipmap-mdpi')
            self.saveAndroid(96, 96, self.androidFolder, 'mipmap-xhdpi')
            self.saveAndroid(144, 144, self.androidFolder, 'mipmap-xxhdpi')
            self.saveAndroid(192, 192, self.androidFolder, 'mipmap-xxxhdpi')
            self.saveAndroid(512, 512, self.androidFolder, 'GooglePlay')
    

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

    def saveAndroid(self, width, height, local, filename):
        image = cv2.resize(self.img,(width,height), interpolation = cv2.INTER_CUBIC)
        print(local+'/'+filename+'/'+'ic_launcher.png')
        cv2.imwrite(local+'/'+filename+'/'+'ic_launcher.png', image)


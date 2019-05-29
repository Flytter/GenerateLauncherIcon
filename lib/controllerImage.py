from lib.getItensFromEntrance import *
import cv2
import os

class controllerImg:
    
    def __init__(self, path, arguments):
        self.itens = getItens()
        self.path = path
        self.nameFolder = arguments
        self.listItens = getItens().getFile(path)
        self.img = cv2.imread(self.listItens[0], cv2.IMREAD_UNCHANGED)
        self.androidFolder = self.path+'/output/'+self.nameFolder[1]+'/android'
        self.iosFolder = self.path+'/output/'+self.nameFolder[1]+'/IOS'

    def resizeImage(self):

        for i in self.listItens:
            self.createFolder(self.path, self.nameFolder[1])
            self.saveAndroid(72, 72, self.androidFolder, 'mipmap-hdpi')
            self.saveAndroid(48, 48, self.androidFolder, 'mipmap-mdpi')
            self.saveAndroid(96, 96, self.androidFolder, 'mipmap-xhdpi')
            self.saveAndroid(144, 144, self.androidFolder, 'mipmap-xxhdpi')
            self.saveAndroid(192, 192, self.androidFolder, 'mipmap-xxxhdpi')
            self.saveAndroid(512, 512, self.androidFolder, 'GooglePlay')

            self.saveIOS(20, 20, self.iosFolder, 'Icons', 'Icon-App-20x20@1x.png')
            self.saveIOS(40, 40, self.iosFolder, 'Icons', 'Icon-App-20x20@2x.png')
            self.saveIOS(60, 60, self.iosFolder, 'Icons', 'Icon-App-20x20@3x.png')

            self.saveIOS(29, 29, self.iosFolder, 'Icons', 'Icon-App-29x29@1x.png')
            self.saveIOS(58, 58, self.iosFolder, 'Icons', 'Icon-App-29x29@2x.png')
            self.saveIOS(87, 87, self.iosFolder, 'Icons', 'Icon-App-29x29@3x.png')

            self.saveIOS(40, 40, self.iosFolder, 'Icons', 'Icon-App-40x40@1x.png')
            self.saveIOS(80, 80, self.iosFolder, 'Icons', 'Icon-App-40x40@2x.png')
            self.saveIOS(120, 120, self.iosFolder, 'Icons', 'Icon-App-40x40@3x.png')
            
            self.saveIOS(120, 120, self.iosFolder, 'Icons', 'Icon-App-60x60@2x.png')
            self.saveIOS(180, 180, self.iosFolder, 'Icons', 'Icon-App-60x60@3x.png')

            self.saveIOS(76, 76, self.iosFolder, 'Icons', 'Icon-App-76x76@1x.png')
            self.saveIOS(152, 152, self.iosFolder, 'Icons', 'Icon-App-76x76@2x.png')

            self.saveIOS(167, 167, self.iosFolder, 'Icons', 'Icon-App-83.5x83.5@2x.png')

            self.saveIOS(1024, 1024, self.iosFolder, 'Icons', 'Icon-App-1024x1024@1x.png')
    
            self.saveIOS(1024, 1024, self.iosFolder, 'AppStore', 'Icon-AppStore.png')

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
    
    def saveIOS(self, width, height, local, filename, file):
        image = cv2.resize(self.img,(width,height), interpolation = cv2.INTER_CUBIC)
        cv2.imwrite(local+'/'+filename+'/'+file, image)



# GenerateLauncherIcon
A script to generate launcher icon for Flutter Apps in mdpi, hdpi, xhdpi, xxhdpi, xxxhdpi and Google Play Store Icon and AppStore

# Introduction
Hi, my name is Daniel, and I'm a mobile and web developer, this is a script help Flutter developer to resize images to publish your app in AppStore and GooglePlay

# How to install
First of all you need Python3 installed in your local machine, after this, install the requirements using

```Python
pip install -r requirements.txt
```

# Project Structure folder

```
|   entrance       #Here you go put your image
|   lib      #All the methods and functions to control the image
|     |---getItensFromEntrance
|   output       #Here is the output of images

```

# How use?

As you can see in topic above, first of all you have to put image into entrance folder, after this run:

```
python main.py
```

At this moment the script go catch the image from entrance and got convert for each specific folder at the output. and the project structure go update, after this you can catch all images inside the output folder, like this:

```
|   output
|      |---android      #output of android icons with respective folders to android
|            |---mipmap-hdpi
|                      |---ic_launcher.png
|            |---mipmap-mdpi
|                      |---ic_launcher.png
|            |---mipmap-xhdpi
|                      |---ic_launcher.png
|            |---mipmap-xxhdpi
|                      |---ic_launcher.png
|            |---mipmap-xxxhdpi
|                      |---ic_launcher.png
|
|     |---IOS
|          |---Icon-App-20x20@1x.png
|          |---Icon-App-20x20@2x.png
|          |---Icon-App-20x20@3x.png
|
|          |---Icon-App-29x29@1x.png
|          |---Icon-App-29x29@2x.png
|          |---Icon-App-29x29@3x.png
|
|          |---Icon-App-40x40@1x.png
|          |---Icon-App-40x40@2x.png
|          |---Icon-App-40x40@3x.png
|
|          |---Icon-App-60x60@2x.png
|          |---Icon-App-60x60@3x.png
|
|          |---Icon-App-76x76@1x.png
|          |---Icon-App-76x76@2x.png
|
|          |---Icon-App-83.5x83.5@2x.png
|          |---Icon-App-1024x1024@1x.png
|          |---AppStore
|                 |---Icon-AppStore
```
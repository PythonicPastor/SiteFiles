from os import system as sendCmd
import os
import subprocess
import sys
import win32com.shell.shell as shell
from Chatroom import server, client
sys.path.insert(0, './Chatroom')
class FakeFi:
    def __init__(self):
        while True:
            sendCmd('cls')
            command = input("Enter Command:")
            if command == "setup":
                if self.checkWifi() == "Yes":
                    print("This computer can host an Access Point.")
                    self.makeWifi()
                else:
                    print("This computer cannot host an Access Point.")
            elif command == "start":
                self.startWifi()
            elif command == "stop":
                self.stopWifi()
            elif command == "rename":
                self.changeSsid()
            elif command == "change password":
                self.changePassw()
            elif command == "check":
                if self.checkWifi() == "Yes":
                    print("This computer can host an Access Point.")
                else:
                    print("This computer cannot host an Access Point.")
                sendCmd('pause')
            elif command == "http":
                sendCmd("cls")
                ip = self.checkIp()
                port = input("Enter Port Number(####):")
                sendCmd(f"python -m http.server {port} --bind {ip} -d '.\Website'")
            elif command == "chat":
                sendCmd("cls")
                ip = self.checkIp()
                port = input('Enter Port Number(####):')
                cs = server.ChatServer(ip, int(port))
                cs.run()
            elif command == "remove":
                self.stopWifi()
                sendCmd("call removeAccessPoint")
            elif command == "help":
                print('------------------------------------------------')
                print('check\t-Check compatiblity of access point setup')
                print('setup\t-Setup Wifi Connection')
                print('start\t-Start Wifi Connection')
                print('stop\t-Stop Wifi Connection')
                print('rename\t-Rename Wifi Connection')
                print('remove\t-Remove Wifi Connection')
                print('http\t-Start Website Server')
                print('chat\t-Start Chatroom Server (Requires all users to have "Chatroom/Client.py" file, ip, and port to use)')
                print('------------------------------------------------')
                sendCmd('pause')
            elif command == "firewall":
                sendCmd('start C:\WINDOWS\system32\WF.msc')
            else:
                print("!!Invalid Command!! Type 'help' for Valid Command List")
                sendCmd('pause')
            
                
    def checkWifi(self):
        check = subprocess.check_output("NETSH WLAN SHOW DRIVERS", shell=False).decode('utf8').split('\r\n')
        for i in check:
            if "Hosted network supported" in i:
                answ = (i.split(' : ')[1])
        return answ
    def checkIp(self):
        check = subprocess.check_output("ipconfig", shell=False).decode('utf8').split('\r\n')
        for i in check:
            if "IPv4 Address" in i:
                answ = (i.split(' : ')[1])
        return answ
    def makeWifi(self):
        sendCmd("call setupAccessPoint")
        self.startWifi()
    def startWifi(self):
        sendCmd("call startAccessPoint")
    def stopWifi(self):
        sendCmd(f"NETSH WLAN stop hostednetwork")
        sendCmd('pause')
    def changeSsid(self):
        new = input('New Wifi Name(SSID):')
        self.stopWifi()
        sendCmd(f"NETSH WLAN set hostednetwork ssid={new}")
        self.startWifi()
        sendCmd('pause')
    def changePassw(self):
        new = input('New Wifi Password:')
        sendCmd(f"NETSH WLAN set hostednetwork key={new}")
        sendCmd('pause')
if __name__ == '__main__':
    FakeFi()

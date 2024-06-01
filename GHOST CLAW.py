from colorama import Fore, Back, Style
from datetime import datetime
import urllib.request
import urllib.parse
import threading
import requests
import socket
import struct
import time
import json
import sys
import os

print(f"{Fore.CYAN}===================================================================================")
print(f"{Fore.CYAN}   ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓    ▄████▄   ██▓    ▄▄▄       █     █░ ")
print(f"{Fore.CYAN}  ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒   ▒██▀ ▀█  ▓██▒   ▒████▄    ▓█░ █ ░█░ ")
print(f"{Fore.CYAN} ▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░   ▒▓█    ▄ ▒██░   ▒██  ▀█▄  ▒█░ █ ░█  ")
print(f"{Fore.CYAN} ░▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░    ▒▓▓▄ ▄██▒▒██░   ░██▄▄▄▄██ ░█░ █ ░█  ")
print(f"{Fore.CYAN} ░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░    ▒ ▓███▀ ░░██████▒▓█   ▓██▒░░██▒██▓  ")
print(f"{Fore.CYAN}  ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░      ░ ░▒ ▒  ░░ ▒░▓  ░▒▒   ▓▒█░░ ▓░▒ ▒   ")
print(f"{Fore.CYAN}   ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░         ░  ▒   ░ ░ ▒  ░ ▒   ▒▒ ░  ▒ ░ ░   ")
print(f"{Fore.CYAN} ░ ░   ░  ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░         ░          ░ ░    ░   ▒     ░   ░   ")
print(f"{Fore.CYAN}       ░  ░  ░  ░    ░ ░        ░              ░ ░          ░  ░     ░  ░    ░     ")
print(f"{Fore.CYAN}           By Promus ")
print(f"{Fore.CYAN}===================================================================================")
print(f"{Fore.YELLOW} 1) PING     2) NETWORK FLOOD     3) USERNAME OSINT     4) SITE SCANNER")
print(f"{Fore.GREEN} 0) HELP ")
print(f"{Fore.CYAN}===================================================================================")
Tool_Selecter_Number=input(f"{Fore.WHITE} Enter Number: ")
print(f"{Fore.CYAN}===================================================================================")
if Tool_Selecter_Number =='1':
    PING_URL_IP=input(f"{Fore.WHITE} Enter Host/Ip: ")
    print(f"{Fore.CYAN}===================================================================================")
    print(f"{Fore.RED}")
    os.system("ping "+PING_URL_IP)

if Tool_Selecter_Number =='2':
    def send_udp_packet(target_ip, target_port, message):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message.encode(), (target_ip, target_port))
    def main():
         target_ip= "127.0.0.1"
         target_port = 80
         message = "ATTACKED BY GHOST CLAW | By Promus"
         for i in range(1000000000):
             send_udp_packet(target_ip, target_port, message)
             print(f"{Fore.RED} FLOODING NETWORK")
         print(f"{Fore.CYAN}===================================================================================")
    main()
if Tool_Selecter_Number =='3':
    Username_Osint_Username=input(f"{Fore.WHITE} Enter Username: ")
    print(f"{Fore.CYAN}===================================================================================")
    try:
         urllib.request.urlopen('https://www.pinterest.com/'+Username_Osint_Username)
         print(f"{Fore.GREEN} "+"https://www.pinterest.com/"+Username_Osint_Username)
         print(" "+'CODE : 200')
    except:
        print(f"{Fore.RED}" 'https://www.pinterest.com/'+Username_Osint_Username)
        print(" "+'CODE : 404')





    try:
         urllib.request.urlopen('https://www.facebook.com/'+Username_Osint_Username)
         print(f"{Fore.GREEN} "+"https://www.facebook.com/"+Username_Osint_Username)
         print(" "+'CODE : 200')
    except:
        print(f"{Fore.RED} "+'https://www.facebook.com/'+Username_Osint_Username)
        print(" "+'CODE : 404')




    try:
         urllib.request.urlopen('https://www.instagram.com/'+Username_Osint_Username)
         print(f"{Fore.GREEN} "+"https://www.instagram.com/"+Username_Osint_Username)
         print(" "+'CODE : 200')
    except:
        print(f"{Fore.RED} "+'https://www.instagram.com/'+Username_Osint_Username)
        print(" "+'CODE : 404')





    try:
         urllib.request.urlopen('https://www.tiktok.com/@'+Username_Osint_Username)
         print(f"{Fore.GREEN} "+"https://www.tiktok.com/@"+Username_Osint_Username)
         print(f"{Fore.GREEN} "+'CODE : 200')
    except:
        print(f"{Fore.RED}"+' https://www.tiktok.com/@'+Username_Osint_Username)
        print(f"{Fore.RED}" +' CODE : 404')
    print(f"{Fore.CYAN}===================================================================================")

if Tool_Selecter_Number =='4':
    def get_website_ip_port(url):
        parsed_uri = urllib.parse.urlparse(url)
        domain = '{uri.netloc}'.format(uri=parsed_uri)
        if parsed_uri.scheme == 'https':
            port = 443
        else:
            port = 80
        ip_addr = socket.gethostbyname(domain)
        return ip_addr, port
    url = input(f"{Fore.WHITE} Enter Url: ")
    print(f"{Fore.CYAN}===================================================================================")
    ip_addr, port = get_website_ip_port(url)
    print(f"{Fore.RED} IP: {ip_addr}")
    print(f"{Fore.RED} PORT: {port}")
    print(f"{Fore.CYAN}===================================================================================")


if Tool_Selecter_Number =='0':
    print(f"{Fore.YELLOW} 1) >For Website : example.com          >For Ip : 1.1.1.1")
    print(f"{Fore.YELLOW} 2) >You Don't Have To Do Anything It Floods Network Automaticly")
    print(f"{Fore.YELLOW} 3) >For Example : love")
    print(f"{Fore.YELLOW} 4) >For Example : https://example.com/")
    print(f"{Fore.YELLOW} ")
    print(f"{Fore.RED} ?) By Promus | t.me/xsvxoxsv666 | ")
    print(f"{Fore.CYAN}===================================================================================")
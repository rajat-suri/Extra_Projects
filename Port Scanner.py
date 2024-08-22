import argparse
import threading
import socket
from colorama import Fore
import requests
print("************************************************************************************************************************************************************")
print(Fore.CYAN)

print('''      
                        $$$$$$$\                       $$\                                                                      
                        $$  __$$\                      $$ |                                                                     
                        $$ |  $$ | $$$$$$\   $$$$$$\ $$$$$$\          $$$$$$$\  $$$$$$$\ $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\ 
                        $$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|        $$  _____|$$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
                        $$  ____/ $$ /  $$ |$$ |  \__| $$ |          \$$$$$$\  $$ /      $$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
                        $$ |      $$ |  $$ |$$ |       $$ |$$\        \____$$\ $$ |     $$  __$$ |$$ |  $$ |$$   ____|$$ |       
                        $$ |      \$$$$$$  |$$ |       \$$$$  |      $$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |\$$$$$$$\ $$ |      
                        \__|       \______/ \__|        \____/       \_______/  \_______|\_______|\__|  \__| \_______|\__|
                                                                                                |
                                                    \n")

print("************************************************************************************************************************************************************")

print("\nPorts scanning is strated")
print(Fore.MAGENTA)

def check_status(domain, ports):
    try:
        # Check Status for HTTP
        http_response = requests.head("http://" + domain, allow_redirects=True, timeout=10)
        http_status_code = http_response.status_code

        # Check HTTPS
        https_response = requests.head("https://" + domain, allow_redirects=True, timeout=10)
        https_status_code = https_response.status_code

        # Print status codes
        if http_status_code == 200:
            print(f"Domain: http://{domain}-Status Code: 200 (OK)")
        elif https_status_code in [301, 302]:
            print(f"Domain: https://{domain}-Status Code: {http_status_code} (Redirect)")
        elif http_status_code == 403:
            print(f"Domain: http://{domain}-Status Code: 403 (Forbidden)")
        else:
            print(f"Domain: http://{domain}-Status Code: {http_status_code}")
        
        # Port scanning
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)  # Set a timeout for the connection attempt
                result = sock.connect_ex((domain, port))
                if result == 0:
                    print(f"Port : {port} -- is open on -- {domain}")
                sock.close()
            except socket.error:
                print(f"Port {port} is closed on {domain}")
    except requests.RequestException as e:
        print(f"Domain: {domain} - Connection Timeout ")

parser = argparse.ArgumentParser(description="Check status codes of HTTP and HTTPS domains.")
parser.add_argument("-f", help="enter Valid filename")
parser.add_argument("-p", nargs="+", type=int, help="ports to scan", default=[80, 443])  # Default ports HTTP and HTTPS
args = parser.parse_args()

# Read the domains from the file
file = open(args.f, "r")
domains = file.readlines()
file.close()

threads = []
for domain in domains:
    domain = domain.strip()
    thread = threading.Thread(target=check_status, args=(domain, args.p))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("--------------------------------------------------------------------Thank-you------------------------------------------------------------------------------")

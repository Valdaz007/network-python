
#? The Goal of this script is to send a Ping Request
#? from the source device to another given the IP Address.
 
#? The Script will use the Modules `CSV` to get the IP address
#? from a csv file, and `OS` & `Subprocess` to access
#? the Cli/CMD to send the Ping Resquest

import subprocess
import os, csv, colorama # type: ignore
from colorama import Fore, Back, Style # type: ignore
colorama.init(autoreset=True)

def main():
    with open("cust-ip.csv", mode="r") as f:    # Get IP info from CSV file
        rd = csv.reader(f)  
        next(rd)
        for row in rd:
            ping(row[0], row[1])

def ping(name:str, ip:str):
    # Coloroma is used to style the output
    # OS to do echo outputs &
    # Subprocess to run the ping command

    os.system(f"echo {Fore.YELLOW}*")
    os.system(f"echo *")
    os.system(f"echo * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    os.system(f"echo {Fore.MAGENTA}{name}: {Fore.WHITE}{ip}{Fore.CYAN}")
    subprocess.run(f'ping {ip}')

if __name__ == "__main__":
    main()
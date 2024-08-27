import subprocess
import os, csv, colorama # type: ignore
from colorama import Fore, Back, Style # type: ignore
colorama.init(autoreset=True)

def main():
    with open("cust-ip.csv", mode="r") as f:
        rd = csv.reader(f)

        next(rd)
        for row in rd:
            ping(row[0], row[1])

def ping(name:str, ip:str):
    os.system(f"echo {Fore.YELLOW}*")
    os.system(f"echo *")
    os.system(f"echo * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    os.system(f"echo {Fore.MAGENTA}{name}: {Fore.WHITE}{ip}{Fore.CYAN}")
    subprocess.run(f'ping {ip}')

if __name__ == "__main__":
    main()
import os,csv, colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def main():
    with open("cust-ip.csv", "r") as f:
        rd = csv.reader(f)

        next(rd)
        for row in rd:
            ping(row[0], row[1])

def ping(name:str, ip:str):
    os.system("echo ''")
    os.system("echo ''")
    os.system(f"echo {Fore.RED}{name}{Fore.GREEN}")
    os.system(f"ping {ip}")

if __name__ == "__main__":
    main()
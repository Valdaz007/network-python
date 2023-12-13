import os,csv

def main():
    with open("cust-ip.csv", "r") as f:
        rd = csv.reader(f)

        next(rd)
        for row in rd:
            ping(row[0], row[1])

def ping(name:str, ip: str):
    os.system(f"echo 'Pinging {name}'")
    os.system(f"ping {ip}")

if __name__ == "__main__":
    main()
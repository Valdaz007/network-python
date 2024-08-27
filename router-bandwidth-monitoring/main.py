from netmiko import ConnectHandler  # type: ignore
import variables # Sensitive Variable Files
# from pprint import pprint as prnt

def main():
    rates = showBandwidth()
    print(rates)
    print(f'RX: {convertTo(int(rates['rx']))} mpbs')
    print(f'TX: {convertTo(int(rates['tx']))} mpbs')

def showBandwidth() -> dict:
    rtr = {
        'ip': variables.ip,
        'device_type': 'cisco_ios',
        'username': variables.username,
        'password': variables.password,
        'secret': variables.secret,
        'port': 22
    }

    try:
        conn = ConnectHandler(**rtr)
        conn.enable()
        intf = conn.send_command('sh int g8', use_textfsm=True)
        intf = {"rx": intf[0]['input_rate'], "tx": intf[0]['output_rate']} 
        conn.disconnect()
        return intf
    except Exception as e:
        return {"error":e}

def convertTo(num:int, rate:str='mbps') -> int:
    if (rate == 'mbps'): return num/1000000
    elif (rate == 'gbps'): return num/1000000000
    elif (rate=='kbps'): return num/1000
    else: return 0


if __name__ == "__main__":
    main()
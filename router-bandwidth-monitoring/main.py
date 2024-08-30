from netmiko import ConnectHandler  # type: ignore
import schedule, time # type: ignore
import variables # Sensitive Variable Files

def main():
    schedule.every(1).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(.5)

def job():
    rates = getBandwidth()  # Get Bandwidth Rates

    print(f'RX: {convertTo(int(rates['rx']))} mpbs') # Print Rx Rate in MBPS
    print(f'TX: {convertTo(int(rates['tx']))} mpbs') # Print Tx Rate in MBPS

def getBandwidth() -> dict:
    # Function Flow: 
    # Create SSH Connection with Targeted Router
    # Send Command to Run
    # Retrieve Command Results & Disconnect SSH Connection
    # Filter Results for Input & Output Rates
    # Return Rates

    rtr = {     # Router Connection Info Dict
        'ip': variables.ip,
        'device_type': 'cisco_ios',
        'username': variables.username,
        'password': variables.password,
        'secret': variables.secret,
        'port': 22
    }

    try:
        conn = ConnectHandler(**rtr)    # Create an SSH Connection with Router
        conn.enable()                   
        intf = conn.send_command('sh int g8', use_textfsm=True) # Send Command to Router
        intf = {"rx": intf[0]['input_rate'], "tx": intf[0]['output_rate']} # Get Input & Output Rates
        conn.disconnect()   # Close SSH Connection
        return intf     # Return Rates
    
    except Exception as e:
        return {"error":e}

def convertTo(num:int, rate:str='mbps') -> int:
    # Function Flow
    # Get Rates As bits/s from Param (num) & Conversion Rate from Param (rate)
    # Check Convert Rate & Convert
    # Return New Rates

    if (rate == 'mbps'): return num/1000000
    elif (rate == 'gbps'): return num/1000000000
    elif (rate=='kbps'): return num/1000
    else: return 0

if __name__ == "__main__":
    main()
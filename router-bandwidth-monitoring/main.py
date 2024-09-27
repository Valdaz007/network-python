from netmiko import ConnectHandler # ConnectHandler to Create SSH Connection # type: ignore
import schedule, time # # type: ignore
import variables # Sensitive Variable Files

def main():
    schedule.every(.5).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

def job():
    rates = getBandwidth()  # Get Bandwidth Rates
    
    try:
        print(f'RX: {convertTo(int(rates['rx']))} mpbs | TX: {convertTo(int(rates['tx']))} mpbs') # Print Rx & Tx Rate in MBPS
    except Exception as e:
        print(e)

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
        'username': variables.username, # Router Username
        'password': variables.password, # Router Password
        'secret': variables.secret,     # Router Enable Secret
        'port': 22                      # SSH Port
    }

    try:
        conn = ConnectHandler(**rtr)    # Create an SSH Connection with Router
        conn.enable()                   
        intf = conn.send_command('sh int g8', use_textfsm=True) # Send Command to Router
        intf = {"rx": intf[0]['input_rate'], "tx": intf[0]['output_rate']} # Filter Out Input & Output Rates
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
from urllib.request import urlopen
from datetime import datetime
import time
# parameters to change SI units
default_website_to_check="https://www.google.com"
interval = 10
desired_timeout=3



def check_internet():
    try:
        urlopen(default_website_to_check, timeout=desired_timeout)
        return True
    except:
        return False
    
    
def main():
    
    f=open("logfile.txt","w")
    internet_connectivity_now=check_internet()
    previous_internet_connectivity=internet_connectivity_now
    previous_down= None if internet_connectivity_now else datetime.now()
    s=f"Script Started @{datetime.now()} internet is {'up' if internet_connectivity_now else 'down'}\n"
    f.write(s)
    print(s)
    
    while True:
        time_now=datetime.now()
        internet_connectivity_now=check_internet()
        if not internet_connectivity_now and previous_internet_connectivity:
            previous_down = time_now
            s=f"internet down @{time_now} \n"
            f.write(s)
            print(s)
        elif internet_connectivity_now and not previous_internet_connectivity:
            s=f"Internet up @{time_now}, internet was down for {time_now-previous_down} ({previous_down} --> {time_now}) \n"
            f.write(s)
            print(s)
        previous_internet_connectivity=internet_connectivity_now
        time.sleep(interval)

if __name__ == "__main__":
    main()
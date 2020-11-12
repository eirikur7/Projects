import speedtest
import time
from datetime import datetime

'''
Measures, download speed, upload speed and ping.
inputs measurements to a text document in format:
'dd/mm/yy, HR:MIN:SEC, download, upload, ping\n'
'''
'''
Markmið: á að fá gildi fyrir dwnl upl og ping. 
hverjar 10 min eða eh. 
geyman gildin í töflu ásamt dag í tíma þegar gildi voru tekin.
'''
'''
1. reikna gildi og setja í list
2. geta reiknað gildi hverjar 10 min
3. setja inn dagsetningu
'''

### Global ###
MINUTES = 10    # Interval of measurements

def speedtester():
    '''
    Gets data for internet speed. returns data as string
    '''
    st = speedtest.Speedtest()
    st.get_best_server()

    # measure download and upload speed in bits per second
    dwnl = st.download()
    upl = st.upload()

    # Convert download and upload speed to Mbits
    dwnl = round(dwnl / (10**6), 2)
    upl = round(upl / (10**6), 2)

    # measure ping in milliseconds
    png = st.results.ping

    # Get date and time
    now = datetime.now()
    date_string = now.strftime("%d/%m/%Y")
    time_string = now.strftime("%H:%M:%S")

    data = f'{date_string}, {time_string}, {dwnl}, {upl}, {png}\n'
    return data

def add_data_to_file(data_string):
    '''
    Opens file, adds data, closes file
    '''
    File_Object = open('Data_File.txt','a')
    File_Object.write(data_string)
    File_Object.close()

def min_to_sec(min):
    return min*60

#### Main Code ####
def main():
    sec = min_to_sec(MINUTES)

    for i in range(5):     
        # Intervals
        time.sleep(10)
        
        # Calculations
        data = speedtester()
        add_data_to_file(data)

main()
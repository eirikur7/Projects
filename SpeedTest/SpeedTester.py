from speedtest import Speedtest
from time import sleep
from datetime import datetime


'''
Measures, download speed, upload speed and ping.
inputs measurements to a text document in format:
'dd/mm/yy, HR:MIN:SEC, download, upload, ping\n'
'''
'''
Used a raspberry pi to do this. 
I wanted to know wich one of my internet providers was 
better and more consistant.
I connected the pi to my router and ran the program remotely
using SSH(secure shell) and github. It gathered the data in txt format then
i switched the ethernet on the pi and ran i again for a couple of 
days.
'''


### Global ###
MINUTES = 10  # Interval of measurements
TEST_SPLIT = '\n<NEW TEST>\n'
FILENAME =  'New_internet.txt' #input('Enter filename: ') + '.txt'
ROUND_DATA = 2

def speedtester():
    '''
    Gets data for internet speed. returns data as string
    '''
    st = Speedtest()
    st.get_best_server()
    # measure download and upload speed in bits per second
    dwnl = st.download()
    upl = st.upload()

    # Convert download and upload speed to Mbits
    dwnl = round(dwnl / (10**6), ROUND_DATA)
    upl = round(upl / (10**6), ROUND_DATA)

    # measure ping in milliseconds
    png = st.results.ping

    # Get date and time
    now = datetime.now()
    date_string = now.strftime("%d/%m/%Y")
    time_string = now.strftime("%H:%M:%S")

    data = '{:>15} {:>15} {:>15} {:>15} {:>15}\n'.format(date_string, time_string, dwnl, upl, png)
    return data

def add_data_to_file(data_string):
    '''
    Opens file, adds data, closes file
    '''
    File_Object = open(FILENAME,'a')
    File_Object.write(data_string)
    File_Object.close()

def min_to_sec(min):
    return min*60

#### Main Code ####
def main():
    sec = min_to_sec(MINUTES)
    #add_data_to_file(TEST_SPLIT)
    while True:
        # Intervals
        sleep(sec)
        
        # Calculations
        data = speedtester()
        add_data_to_file(data)

main()
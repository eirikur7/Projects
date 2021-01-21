from speedtest import Speedtest
from time import sleep
from datetime import datetime
import matplotlib.pylab as plt
import matplotlib.dates as pltdates
import os
import numpy as np

'''
Measures, download speed, upload speed and ping.
inputs measurements to a text document in format:
'dd/mm/yy, HR:MIN:SEC, download, upload, ping\n'
'''



class Speedtester:
    ROUND_DATA = 3

    def __init__(self, auto=False, interval=5, size_data=None, filename='Data.txt'):
        self._dwnl = []
        self._upl = []
        self._ping = []
        self._date = []
        self._time = []

        self._row_format = '{:>15}'*5 + '\n'
        self._counter = 0

        if auto:
            self._auto_measurement(interval, size_data, filename)

    def _auto_measurement(self, interval, size_data, filename):
        '''Makes everything autmatic, measures at given interval,
        appends data to txt document and saves a plot of data'''
        while self._counter != size_data:
            self.measure(date=True, time=True, dwnl=True, upl=True, png=True)
            self.data_to_file(filename)

            # interval
            sleep(interval * 60)

        self._make_plot(filename=filename)
        return

    def _make_plot(self, filename=None):
        if filename == None:
            filename = 'Plot'

        time = []
        for timestamp in self._time:
            time.append(datetime.strptime(timestamp, "%H:%M:%S"))
        
    
        plt.plot(self._time, self._dwnl, self._time, self._upl)

        plt.title(f'Download and upload speed vs time')
        plt.legend(['Download', 'Upload'])
        plt.text(100, 0, self._date[0])
        plt.xlabel('Time [sec]')
        plt.ylabel('speed [Mbits/sec]')
        plt.savefig(filename+'.png')
            

    def measure(self, date=False, time=False, dwnl=False, upl=False, png=False):
        '''Returns following data, if true.

        date -> dd/mm/yy
        time -> HR:MIN:SEC
        dwnl -> download speed in Mbits
        upl  -> upload speed in Mbits
        png  -> ping in milliseconds
        '''
        now = datetime.now()
        st = Speedtest()
        st.get_best_server()

        if date:
            self._date.append(now.strftime("%d/%m/%Y"))
        if time:
            self._time.append(now.strftime("%H:%M:%S"))
        if dwnl:
            dwnl = st.download()
            self._dwnl.append(round(dwnl / (10**6), Speedtester.ROUND_DATA))
        if upl:
            upl = st.upload()
            self._upl.append(round(upl / (10**6), Speedtester.ROUND_DATA))
        if png:
            self._ping.append(st.results.ping)

        self._counter += 1
        return 

    def data_to_file(self, filename=None):
        '''Makes a txt file and appends each entry'''
        if filename == None:
            filename = os.path.dirname(os.path.abspath(__file__)) + '\\Data.txt'

        if self._counter == 1:
            file_stream = open(filename+'.txt', 'a')
            string = self._row_format.format('dd/mm/yy', 'HR:MIN:SEC', 'dwnl[Mbits]', 'upl[Mbits]', 'ping[ms]')
            file_stream.write(string)
            file_stream.close()

        entry = self._row_format.format(self._date[-1], self._time[-1], self._dwnl[-1], self._upl[-1], self._ping[-1])

        file_stream = open(filename+'.txt', 'a')
        file_stream.write(entry)
        file_stream.close()

    def set_rounding(self, round_to):
        '''Able to change rounding of data'''
        Speedtester.ROUND_DATA = round_to

    def add_data(self, data_stream):
        '''Add existing data of the same format.
        input must be file_object'''
        for line in data_stream:
            line = line.split()
            self._date.append(line[0])
            self._time.append(line[1])
            self._dwnl.append(float(line[2]))
            self._upl.append(float(line[3]))
            self._ping.append(float(line[4]))







#### Main Code ####
if __name__ == '__main__':
    # test = Speedtester()
    # test._counter = 1
    # path = os.path.dirname(os.path.abspath(__file__))
    # data = open(path+'\\Test_data.txt','r')
    # test.add_data(data)
    # test.data_to_file()
    # test._make_plot()



    test = Speedtester(auto=True, interval=0, filename='SpeedTest_Vodafone_2')

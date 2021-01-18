from speedtest import Speedtest
from time import sleep
from datetime import datetime
import matplotlib.pylab as plt
import os


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
i switched the ethernet on the pi and ran it again for a couple of 
days.
'''

class Speedtester(Speedtest):
    ROUND_DATA = 3

    def __init__(self, auto=False, interval=5, size_data=None, path='', filename='Data.txt'):
        self._dwnl = []
        self._upl = []
        self._ping = []
        self._date = []
        self._time = []

        self._row_format = '{:>15}'*5 + '\n'
        self._counter = 0

        if auto:
            self._auto_measurement(interval, size_data, path, filename)

    def _auto_measurement(self, interval, size_data, path, filename):
        '''Makes everything autmatic, measures and given interval,
        appends data to txt document and saves a plot of data'''

        self.measure(date=True, time=True, dwnl=True, upl=True, png=True)
        self.data_in_txt(path, filename)

        # interval
        sleep(interval * 60)

        if size_data == self.counter:
            self._make_plot(path)
            return

    def _make_plot(self, path):
        plt.plot(self.time, self.dwnl, self.time, self.upl)
        plt.title('Download and upload speed vs time')
        plt.legend(['Download', 'Upload'])
        plt.xlabel('Time')
        plt.ylabel('speed in Mbits/sec')

        plt.savefig(path+'Data_plot.png', dpi=300, bbox_inches='tight')

    def measure(self, date=False, time=False, dwnl=False, upl=False, png=False):
        '''Returns following data, if true.

        date -> dd/mm/yy
        time -> HR:MIN:SEC
        dwnl -> download speed in Mbits
        upl  -> upload speed in Mbits
        png  -> ping in milliseconds
        '''
        super.get_best_server()
        now = datetime.now()

        if date:
            self._date.append(now.strftime("%d/%m/%Y"))
        if time:
            self._time.append(now.strftime("%H:%M:%S"))
        if dwnl:
            dwnl = super.download()
            self._dwnl.append(round(dwnl / (10**6), Speedtester.ROUND_DATA))
        if upl:
            upl = super.upload()
            self._upl.append(round(upl / (10**6), Speedtester.ROUND_DATA))
        if png:
            self._ping.append(super.results.ping)

        self.counter += 1
        return 

    def data_in_txt(self,path='', filename='Data.txt'):
        '''Makes a txt file and appends each entry'''

        if self.counter == 1:
            file_stream = open(path+filename, 'a')
            string = self._row_format.format('dd/mm/yy', 'HR:MIN:SEC', 'downl[Mbits]', 'upl[Mbits]', 'ping[ms]')
            file_stream.write(string)
            file_stream.close()

        entry = self._row_format.format(self.date[-1], self.time[-1], self.dwnl[-1], self.upl[-1], self.ping[-1])

        file_stream = open(path+filename, 'a')
        file_stream.write(entry)
        file_stream.close()

    def set_rounding(self, round_to):
        '''Able to change rounding of data'''
        Speedtester.ROUND_DATA = round_to






#### Main Code ####
if __name__ == '__main__':
    pass
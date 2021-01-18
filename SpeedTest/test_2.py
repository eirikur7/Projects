import matplotlib.pylab as plt
import os

PATH = os.path.dirname(os.path.abspath(__file__))
TEST_SPLIT = '\n<NEW TEST>\n'
FILENAME = '\\Test_data.txt'

'dd/mm/yy, HR:MIN:SEC, download, upload, ping\n'
def get_data():
    dwnl, upl, time, hour = [], [], [], []
    file_object = open(PATH + FILENAME, 'r')
    for row in file_object:
        if row == TEST_SPLIT or 'NEW TEST' in row:
            continue

        el = row.split()
        time.append( el[1][0:5])
        hour.append( int(el[1][0:2]))
        dwnl.append( float(el[2]))
        upl.append(  float(el[3]))
    
    plt.plot(time, dwnl, time, upl)
    plt.title('Download and upload speed vs time, with 10 minute intervals.')
    plt.legend(['Download', 'Upload'])
    plt.xticks(time,hour)

    plt.savefig(PATH+'plot_speed.png', dpi=300, bbox_inches='tight')
    plt.show()
if __name__ == '__main__':
    get_data()


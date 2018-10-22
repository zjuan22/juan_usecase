import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
from matplotlib.patches import Polygon
import matplotlib

matplotlib.rc('xtick', labelsize=10)
matplotlib.rc('ytick', labelsize=10)


#file to read in
#infile = '/Users/suneetsingh/Desktop/Boxplot/bng_ul/bng_ul_latency_boxplot.csv'
#infile = 'bng_ul/bng_ul_latency_boxplot.csv'
#infile = '/home/lion/workspace/macsad_latency/eps_figures/boxplot_bng/bng_ul/bng_ul_latency_boxplot.csv'
infile = '/home/lion/workspace/macsad_latency/eps_figures/boxplot_bng/bng_ul/bng_ul_latency_dpdk.csv'


#pull data into NumPy dataframe
df = pd.read_csv(infile, sep=',', na_values='.')

#plt.labels('128', '256', '512', '1024')
plt.title('BNG_UL Use case with DPDK Pktio')
plt.xlabel('Packet Size (Bytes)')
plt.ylabel('Latency (ns)')
#plt.yaxis.grid(linestyle='--')
#plt.xaxis.set_label_coords(0.5,-0.2)


#x = np.array([64,128,156,512,1024,1280,1518,64,128,156,512,1024,1280,1518,64,128,156,512,1024,1280,1518,64,128,156,512,1024,1280,1518,64,128,156,512,1024,1280,1518,64,128,156,512,1024,1280,1518])

#x=range(len(x_axis))


#plt.legend(["64","","","","","",""])
#myplot = df.plot.bar()
#for item in myplot.get_xticklabels():
#   item.set_rotation(90)

#bp= df.boxplot(whis=[1,99], showfliers=True, showmeans=True,)
bp= df.boxplot(whis=[1,99], showfliers=True, flierprops={'markersize': 3},meanprops={'markersize': 3}, showmeans=True, widths = 0.5)

plt.xticks(rotation=90)
#df.drop(['7','8','16', '17', '25', '26', '34', '35' ], axis=1, inplace=True)
#df
#df.loc[:, ~df.columns.str.contains('^Unnamed')]
#df.drop(df.columns[[7, 8, 16, 17,25,26,34,35]], axis=1, inplace=True)
#df = pd.DataFrame(columns=['a','Unnamed: 7', 'Unnamed: 8','foo'])
#plt.legend()
#plt.xlabel('x')
#ax1 = plt.axes()
#x_axis = ax1.axes.get_xaxis()
#x_axis.set_visible(True)
#plt.xticks([0,64, 128])
plt.xticks(np.arange(44), ('', '98', '128', '256', '512','1024','1280','1518','','','98', '128', '256', '512','1024','1280','1518', '','','98', '128', '256', '512','1024','1280','1518','','','98', '128', '256', '512','1024','1280','1518','','','98', '128', '256', '512','1024','1280','1518'),fontsize=9)

#bp.grid(color='g', linestyle='--')
#bp.grid(axis='x')
plt.text(0, -600, '          1                  100                1k                 10k              100k ',fontsize=10)

plt.text(14, -1300, u'     Number of entries',fontsize=10)

#plt.tight_layout(pad=1, w_pad=0.7, h_pad=0.2)
plt.tight_layout(pad=2.5, w_pad=2.5, h_pad=2)

bp.grid(color='g', linestyle='--')
bp.grid(axis='x')
plt.axis('tight')
#plt.show()

filename="lat_bng_ul_boxplot"
#plt.savefig("vxlan.png")
plt.savefig(filename+".eps")
#plt.savefig(filename+".svg")
plt.savefig(filename+".png")




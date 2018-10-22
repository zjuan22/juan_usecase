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
#infile = '/home/lion/workspace/macsad_latency/eps_figures/boxplot_bng/bng_ul/bng_up_latency_dpdk_netmap2.csv'


#pull data into NumPy dataframe
df = pd.read_csv('bng_up_latency_dpdk_netmap2.csv', sep=',', na_values='.')

#plt.labels('128', '256', '512', '1024')
plt.title('BNG_UP Use case')
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
bp= df.boxplot(whis=[1,99], showfliers=True, flierprops={'markersize': 3},meanprops={'markersize': 3}, showmeans=True,widths = 0.5)

plt.xticks(rotation=90)
plt.xticks(np.arange(44), ('','', '98','1518','','','98','1518', '','','98','1518','','','98','1518','','','98','1518','','','98','1518','','','98','1518','','','98','1518','','','98','1518','','','98','1518'))

#bp.grid(color='g', linestyle='--')
#bp.grid(axis='x')
plt.text(0, -4200, '      8      32     128     512    1024     8      32     128    512     1024',fontsize=10)

plt.text(16, -6200, u' Burst size',fontsize=11)
plt.text(8, -7200, u' DPDK                               Netmap',fontsize=11)

#plt.tight_layout(pad=1, w_pad=0.7, h_pad=0.2)
plt.tight_layout(pad=3.5, w_pad=2.5, h_pad=2)

bp.grid(color='g', linestyle='--')
bp.grid(axis='x')
plt.axis('tight')
#plt.show()

filename="lat_bng_ul_d_n"
#plt.savefig("vxlan.png")
plt.savefig(filename+".eps")
#plt.savefig(filename+".svg")
plt.savefig(filename+".png")




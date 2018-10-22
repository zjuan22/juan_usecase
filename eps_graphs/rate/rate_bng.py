#import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

plt.rcParams['axes.spines.right'] = True 
plt.rcParams['axes.spines.bottom'] = True
plt.rcParams['axes.spines.left'] = True 
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['figure.figsize'] = 20, 4 

cores =     ["","98","","128","","256","","512","","1024","","1280","","1518","","","98","","128","","256","","512","","1024","","1280","","1518",""]


ul_100k=[1.10,2.14,4.61,9.18,9.58,9.80,9.80]
dl_100k=[2.0,3.33,6.12,9.64,9.81,9.84,9.88]

ul_10k=[1.23,2.13,4.72,9.20,9.58,9.80,9.80]
dl_10k=[2.00,3.40,6.22,9.64,9.81,9.85,9.88]

ul_100=[1.56,2.55,5.15,9.21,9.58,9.80,9.80]
dl_100=[2.00,3.71,6.56,9.65,9.81,9.85,9.88]

ul_1k=[1.32,2.31,4.90,9.21,9.58,9.80,9.80]
dl_1k=[1.98,3.46,6.31,9.65,9.81,9.85,9.88]


print ul_1k[0]



e_1k = [np.nan , np.nan ,ul_1k[0], np.nan, ul_1k[1] ,np.nan, ul_1k[2] ,np.nan, ul_1k[3] ,np.nan, ul_1k[4],np.nan, ul_1k[5],np.nan,ul_1k[6], np.nan,np.nan,dl_1k[0],np.nan,dl_1k[1],np.nan,dl_1k[2],np.nan,dl_1k[3],np.nan,dl_1k[4],np.nan,dl_1k[5],np.nan,dl_1k[6]]

e_100 = [np.nan , np.nan ,ul_100[0], np.nan,ul_100[1] ,np.nan,ul_100[2] ,np.nan,ul_100[3] ,np.nan,ul_100[4],np.nan,ul_100[5],np.nan,ul_100[6], np.nan,np.nan,dl_100[0],np.nan,dl_100[1],np.nan,dl_100[2],np.nan,dl_100[3],np.nan,dl_100[4],np.nan,dl_100[5],np.nan,dl_100[6]]
#
e_10k = [np.nan ,ul_10k[0] , np.nan,ul_10k[1],np.nan,ul_10k[2],np.nan,ul_10k[3],np.nan,ul_10k[4],np.nan,ul_10k[5],np.nan,ul_10k[6], np.nan,np.nan,dl_10k[0],np.nan,dl_10k[1],np.nan,dl_10k[2],np.nan,dl_10k[3],np.nan,dl_10k[4],np.nan,dl_10k[5],np.nan,dl_10k[6],np.nan]
#
e_100k= [np.nan ,ul_100k[0] , np.nan,ul_100k[1],np.nan,ul_100k[2],np.nan,ul_100k[3],np.nan,ul_100k[4],np.nan,ul_100k[5],np.nan,ul_100k[6], np.nan,np.nan,dl_100k[0],np.nan,dl_100k[1],np.nan,dl_100k[2],np.nan,dl_100k[3],np.nan,dl_100k[4],np.nan,dl_100k[5],np.nan,dl_100k[6],np.nan]





l2_g= [] 
l3_g= [] 
natu_g= [] 
natd_g= [] 
#netmap_p = netmap
#socket_p = socket

numb = [0,98,128,256,512,1024,1280,1528,0,0,98,128,256,512,1024,1280,1528]

#for i in range(0,len(cores)):
#	if l1[i] != np.nan or l2[i] != np.NaN:
#                print l2[i] 
#		l2_g.append(int(l2[i]/1000))
#		l3_g.append(int(l3[i]/1000))
#		#l3_g[i]=l3[i]/1000 
#	else: 
#		np.nan
#
#for i in range(0,len(cores)):
#	if nat_ul[i] != np.nan: 
#		natu_g.append(nat_ul[i]/1000)
#		natd_g.append(nat_dl[i]/1000) 
#	else:
#		np.nan

 
ind = np.arange(len(cores))

verde="#B2E835"
tomate="#E88411"
azul="#1C179F"
cafe="#7E1410"

width = 0.4
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar([p + width for p in ind+0.05],e_100 , width, color= verde, edgecolor="black",hatch="", lw=0.5, zorder = 0)
ax.bar([p + width for p in ind-0.37],e_1k , width, color= azul, edgecolor="black",hatch="//", lw=0.5, zorder = 0)
ax.bar([p + width for p in ind+0.2], e_10k, width, color=tomate, edgecolor="black",hatch="..", lw=0.5, zorder = 0)
ax.bar([p + width for p in ind-0.2], e_100k, width, color= cafe, edgecolor="black",hatch="OO", lw=0.5, zorder = 0)

ax.set_xticks(ind+6*(width/2))
xticks = ax.xaxis.get_major_ticks()

xticks[0].set_visible(False)
xticks[2].set_visible(False)
xticks[4].set_visible(False)
xticks[6].set_visible(False)
xticks[8].set_visible(False)
#xticks[9].set_visible(False)
xticks[10].set_visible(False)
#xticks[11].set_visible(False)
xticks[12].set_visible(False)
#xticks[13].set_visible(False)
xticks[14].set_visible(False)
xticks[15].set_visible(False)
#xticks[16].set_visible(False)
xticks[17].set_visible(False)
xticks[19].set_visible(False)
xticks[21].set_visible(False)
xticks[23].set_visible(False)
xticks[25].set_visible(False)
xticks[27].set_visible(False)
#xticks[30].set_visible(False)


font_size=16
ax.set_xticklabels(cores, fontsize=font_size)

#ax.set_ylabel('Average latency ($\mu$s)',fontsize=font_size)
ax.set_ylabel('Througput (Gbps)',fontsize=font_size)
#ax.yaxis.set_label_coords(-0.08,0.9)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
#ax.tick_params(axis='y',length=21)
ax.xaxis.set_ticks_position('bottom')
ax.set_xlabel("Packet size (Bytes)", fontsize=font_size)
ax.xaxis.set_label_coords(0.5,-0.2)
ax.yaxis.grid(linestyle='--')


pos_y= -2
ax.text(8, pos_y, u'BNG_UL',fontsize=font_size)
ax.text(23.5, pos_y, u'BNG_DL',fontsize=font_size)
#ax.text(5.4,pos_y, u'DPDK',fontsize=font_size)
ax.set_ylim([0,10])

leg = plt.legend(['100','1k','10k', '100k'], loc='upper left', fontsize=font_size)
leg.get_frame().set_linewidth(0.0)
plt.tight_layout(pad=0.3, w_pad=0.5, h_pad=1)

filename="rate_diff_table_e_bng"
#plt.savefig("vxlan.png")
plt.savefig(filename+".eps")
plt.savefig(filename+".svg")
plt.savefig(filename+".png")

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

cores =     ["","128","","256","","512","","1024","","1280","","1518",""]


osnt_bu=[2.55 ,	5.15 ,	9.21 ,	9.58 ,	9.80 ,	9.80]
nfpa_bu=[3.72 ,	6.4  ,   9.8 ,   10  ,   10  ,   10]


osnt_bd=[3.71 ,	6.56 ,	9.65 ,	9.81 ,	9.85 ,	9.88]
nfpa_bd=[3.6  ,  6.8 ,   9.8 ,   10  ,   10  ,   10]

e_1k = [np.nan , np.nan ,osnt_bd[0], np.nan, osnt_bd[1] ,np.nan, osnt_bd[2] ,np.nan, osnt_bd[3] ,np.nan, osnt_bd[4],np.nan, osnt_bd[5]]

e_100 = [np.nan , np.nan ,nfpa_bd[0], np.nan,nfpa_bd[1] ,np.nan,nfpa_bd[2] ,np.nan,nfpa_bd[3] ,np.nan,nfpa_bd[4],np.nan,nfpa_bd[5]]

e_10k = [np.nan ,osnt_bu[0] , np.nan,osnt_bu[1],np.nan,osnt_bu[2],np.nan,osnt_bu[3],np.nan,osnt_bu[4],np.nan,osnt_bu[5],np.nan]
e_100k = [np.nan ,nfpa_bu[0] , np.nan,nfpa_bu[1],np.nan,nfpa_bu[2],np.nan,nfpa_bu[3],np.nan,nfpa_bu[4],np.nan,nfpa_bu[5],np.nan]


le1= len(cores)
le2= len(e_1k)
le3= len(e_100)
print (le1)
print (le2)
print (le3)



l2_g= [] 
l3_g= [] 
natu_g= [] 
natd_g= [] 
#netmap_p = netmap
#socket_p = socket

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
verde_o="#66cc00"
tomate="#E88411"
azul="#1C179F"
azul_claro="#99ccff"
cafe="#7E1410"


width = 0.4
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar([p + width for p in ind+0.05],e_100 , width, color= verde, edgecolor="black",hatch="", lw=0.5, zorder = 0)
ax.bar([p + width for p in ind+0.05],e_1k , width, color= azul, edgecolor="black",hatch="//", lw=0.5, zorder = 0)
#ax.bar([p + width for p in ind-0.37],e_1k , width, color= azul, edgecolor="black",hatch="//", lw=0.5, zorder = 0)
ax.bar([p + width for p in ind+0.4], e_100k, width, color= verde_o, edgecolor="black",hatch="OO", lw=0.5, zorder = 0)
ax.bar([p + width for p in ind+0.4], e_10k, width, color=azul_claro, edgecolor="black",hatch="..", lw=0.5, zorder = 0)
#ax.bar([p + width for p in ind-0.2], e_100k, width, color= cafe, edgecolor="black",hatch="OO", lw=0.5, zorder = 0)

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
#xticks[14].set_visible(False)
#xticks[15].set_visible(False)
##xticks[16].set_visible(False)
#xticks[17].set_visible(False)
#xticks[19].set_visible(False)
#xticks[21].set_visible(False)
#xticks[23].set_visible(False)
#xticks[25].set_visible(False)
#xticks[27].set_visible(False)
##xticks[30].set_visible(False)


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
#ax.text(8, pos_y, u'BNG_UL',fontsize=font_size)
#ax.text(23.5, pos_y, u'BNG_DL',fontsize=font_size)
#ax.text(5.4,pos_y, u'DPDK',fontsize=font_size)
ax.set_ylim([0,10])

leg=plt.legend(['Batch size 8-DPDK ','Batch size 64-DPDK','Batch size 256-DPDK','Batch size 512-DPDK', 'Batch size 1024-DPDK','Batch size 8-Netmap','Batch size 64-Netmap','Batch size 256-Netmap','Batch size 512-Netmap', 'Batch size 1024-Netmap'], fontsize= 9, loc='upper center', bbox_to_anchor=(0.5, -0.3), ncol=3)

#leg = plt.legend(['bng_up nfpa','bng_up osnt','bng_up nfpa', 'bng_up osnt'], loc='upper left', fontsize=font_size)
leg = plt.legend(['BNG DL nfpa','BNG DL osnt','BNG UL nfpa', 'BNG UL osnt'], loc='upper left', fontsize=font_size,bbox_to_anchor=(0, 1), ncol=2) 
leg.get_frame().set_linewidth(0.0)
plt.tight_layout(pad=0.3, w_pad=0.5, h_pad=1)

filename="rate_bng_onst_dpdk"
#plt.savefig("vxlan.png")
plt.savefig(filename+".eps")
plt.savefig(filename+".png")

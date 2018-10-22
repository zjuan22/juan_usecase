#import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

plt.rcParams['axes.spines.right'] = True 
plt.rcParams['axes.spines.bottom'] = True
plt.rcParams['axes.spines.left'] = True 
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['figure.figsize'] = 6.5, 3.5 


markers = ["*","o","^",".",">"]

x_values= ["98", "128","256","512","1024","1280","1518"]


#bng_8_dpdk= [1.5, 2.5, 5.02, 9.18, 9.58, 9.86, 9.86]
#bng_16_dpdk= [1.53, 2.51, 5.03, 9.18, 9.58, 9.86, 9.86]
#bng_32_dpdk= [1.56, 2.55, 5.15, 9.18, 9.58, 9.86, 9.86]
#bng_64_dpdk= [1.56, 2.53, 5.15, 9.19, 9.58, 9.86, 9.86]
#

# this data for bng dl with 1k entries
bng_8_dpdk= [1.99,3.4 ,6.24,9.64,9.81,9.85,9.88]
bng_16_dpdk= [1.99,3.45,6.34,9.64,9.81,9.85,9.88]
bng_32_dpdk= [1.98,3.46,6.31,9.65,9.81,9.85,9.88]
bng_64_dpdk= [2,3.46,6.32,9.65,9.81,9.85,9.88]
bng_128_dpdk= [2.01,3.48,6.31,9.64,9.81,9.85,9.88]
bng_256_dpdk= [1.98,3.43,6.30,9.64,9.81,9.85,9.85]
bng_512_dpdk= [1.99,3.45,6.31,9.64,9.81,9.85,9.88]
bng_1024_dpdk= [2.00,3.48,6.36,9.64,9.81,9.85,9.88]



bng_8_netmap =  [ 0.346,0.579,1.065,2    ,3.8  ,3.95,4.62] 
bng_16_netmap = [ 0.54 ,0.9  ,1.63 ,3.04 ,5.71 ,6.03,7.28]
bng_32_netmap = [ 0.75 ,1.24 ,2.24 ,4.08 ,7.25 ,8.16,9.67]
bng_64_netmap = [ 0.91 ,1.51 ,2.71 ,4.86 ,8.51 ,9.53,9.77]
bng_128_netmap= [ 1.03 ,1.67 ,2.98 ,5.31 ,9.4  ,9.66,9.77]
bng_256_netmap= [ 1.09 ,1.79 ,3.22 ,5.61 ,9.77 ,9.68,9.77]
bng_512_netmap= [ 1.04 ,1.74 ,3.04 ,5.16 ,8.38 ,9.68,9.77]
bng_1024_netmap=[ 1.03 ,1.73 ,3.03 ,4.85 ,7.21 ,9.68,9.77]









ind = np.arange(len(x_values))

width = 0.3
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.set_ylim([0, 10])


linestyles = ['-', '--', '-.', ':']
dashList = [(4,2,20,2),(2,2),(5,1),(4,3,2,2),(8,4,3,1)] 
verde_oscuro="#006633"
azul_cielo="#2248E1"

fucsia="#DA22E1"
cafe="#A91524"

azul_mar="#161673"
azul_claro="#1AE2E2"

tomate="#E88411"
verde_fosfo="#B2E835"

ax.yaxis.grid(color='gray' )

#ax.plot(ind, l2_32_netmap,  marker=markers[0],  color="green",  dashes=dashList[0],markerfacecolor="green",markeredgecolor="green", lw=2, markersize=9 )
#ax.plot(ind, l2_128_netmap, color="green",  dashes=dashList[1], lw=2, markerfacecolor="green",markeredgecolor="green",  marker=markers[1] )
#ax.plot(ind, l2_256_netmap, color="green",  dashes=dashList[2], lw=2, markerfacecolor="green",markeredgecolor="green",  marker=markers[2] )

ax.plot(ind, bng_8_dpdk,  color="blue",   dashes=dashList[1], lw=1, markerfacecolor="blue",markeredgecolor="blue",  marker=markers[1] )
ax.plot(ind, bng_32_dpdk,  color="blue",   dashes=dashList[2], lw=1, markerfacecolor="blue",markeredgecolor="blue",  marker=markers[2] )
ax.plot(ind, bng_256_dpdk,  color="blue",   dashes=dashList[3], lw=1, markerfacecolor="blue",markeredgecolor="blue",  marker=markers[3] )
ax.plot(ind, bng_512_dpdk,  color="blue",   dashes=dashList[0], lw=1, markerfacecolor="blue",markeredgecolor="blue",  marker=markers[0] )
ax.plot(ind, bng_1024_dpdk,  color="blue",   dashes=dashList[4], lw=1, markerfacecolor="blue",markeredgecolor="blue",  marker=markers[4] )


ax.plot(ind, bng_8_netmap,  color="green",   dashes=dashList[1], lw=1, markerfacecolor="green",markeredgecolor="green",  marker=markers[1] )
ax.plot(ind, bng_32_netmap,  color="green",   dashes=dashList[2], lw=1, markerfacecolor="green",markeredgecolor="green",  marker=markers[2] )
ax.plot(ind, bng_256_netmap,  color="green",   dashes=dashList[3], lw=1, markerfacecolor="green",markeredgecolor="green",  marker=markers[3] )
ax.plot(ind, bng_512_netmap,  color="green",   dashes=dashList[0], lw=1, markerfacecolor="green",markeredgecolor="green",  marker=markers[0] )
ax.plot(ind, bng_1024_netmap,  color="green",   dashes=dashList[4], lw=1, markerfacecolor="green",markeredgecolor="green",  marker=markers[4] )


#ax.set_xticks(ind+6*(width/2))
#xticks = ax.xaxis.get_major_ticks()
font_size=14
ax.set_xticklabels(x_values, fontsize=font_size)

ax.set_ylabel('Throughput (Gbps)',fontsize=font_size)
#ax.yaxis.set_label_coords(-0.08,0.font_size)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
#ax.tick_params(axis='y',length=6)
ax.xaxis.set_ticks_position('bottom')
ax.set_xlabel("Packet size (Bytes)", fontsize=font_size)
ax.xaxis.set_label_coords(0.5,-0.2)
ax.yaxis.grid(linestyle='--')

#leg=plt.legend(['Batch size 8','Batch size 64','Batch size 256','Batch size 512', 'Batch size 1024'], loc='upper left', fontsize= 9, loc='upper center', bbox_to_anchor=(0.5, -0.05),
leg=plt.legend(['Batch size 8-DPDK ','Batch size 64-DPDK','Batch size 256-DPDK','Batch size 512-DPDK', 'Batch size 1024-DPDK','Batch size 8-Netmap','Batch size 64-Netmap','Batch size 256-Netmap','Batch size 512-Netmap', 'Batch size 1024-Netmap'], fontsize= 9, loc='upper center', bbox_to_anchor=(0.5, -0.3), ncol=3)

leg.get_frame().set_linewidth(0.0)
for text in leg.get_texts():
    plt.setp(text, color = 'k')

plt.tight_layout(pad=3.5, w_pad=1, h_pad=2)

filename="bng_dl_netmap_dpdk"
#plt.savefig("vxlan.png")
plt.savefig(filename+".eps")
plt.savefig(filename+".png")
#plt.savefig(filename+".svg")

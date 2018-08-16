#!/usr/bin/env python

import os
import string
import sys
import random
from random import shuffle
import argparse
from random import randint

from scapy.all import *
from datetime import datetime                                                   
now = datetime.now()



#Parse the number of entries
parser = argparse.ArgumentParser(description='IPv4 PCAP generator.')
parser.add_argument('num', metavar='n', type=int,
                   help='Number of entries')
args = parser.parse_args()


pkts = []
f = 0
entries = args.num
ipdst = []
ipsrc = []
macsrc = []
macdst = []
macsrc_h = []
macdst_h = []
#pktsize = [18, 82, 210, 466, 978, 1234, 1472] #Don't update the pktsizes original
#pktsize = [0 ,46, 174,430 ,942, 1198, 1436] #Don't update the pktsizes
pktsize = [0, 54, 182, 438, 950, 1206, 1444] #Don't update the pktsizes

#The next code generates random IPv6 and MAC address
#########
k = []
for i in range(16):
    k.append(i)
shuffle(k)
r = []
i = 0
for i in range(1,254):
    r.append(i)
shuffle(r)

l = 0
macsrc_c = ""
macdst_c = ""
macsrc_hex = ""
macdst_hex = ""
ipsrc_c = ""
ipdst_c = ""
for m in range(entries):
	macsrc_c = "f0:76:1c:"
	macdst_c = "f0:76:1c:"
	macsrc_hex = "0xf0:0x76:0x1c:"
	macdst_hex = "0xf0:0x76:0x1c:"
	l = 0
	n = 0
	for i in range(6):
		if l == 2:
			n = 0
			macsrc_c = macsrc_c + ":" + format(k[0], '01x')
			macdst_c = macdst_c + ":" + format(k[1], '01x')
			if n == 0:
				macsrc_hex = macsrc_hex + ":" + format(k[0], '#01x')
				macdst_hex = macdst_hex + ":" + format(k[1], '#01x')
				n = 1
			l = 0
		else:
			macsrc_c = macsrc_c + format(k[0], '01x')
			macdst_c = macdst_c + format(k[1], '01x')
			if n == 0:
				macsrc_hex = macsrc_hex + format(k[0], '#01x')
				macdst_hex = macdst_hex + format(k[1], '#01x')
				n = 1
			else:
				macsrc_hex = macsrc_hex + format(k[0], '01x')
				macdst_hex = macdst_hex + format(k[1], '01x')
		l = l + 1
		shuffle(k)
	macdst.append(macdst_c)
	macsrc.append(macsrc_c)
	macdst_h.append(macdst_hex)
	macsrc_h.append(macsrc_hex)

tcp_dest = []
for m in range(entries):
	l = 0
	ipsrc_c = ""
	ipdst_c = ""
        
	for i in range(4):
		if l == 1:
			ipdst_c = ipdst_c + "." + str(r[0])
			ipsrc_c = ipsrc_c + "." + str(r[1])
			l = 0
		else:
			ipdst_c = ipdst_c + str(r[0])
			ipsrc_c = ipsrc_c + str(r[1])
		l = l + 1
		shuffle(r)
        tcp_dest.append(str(r[2]))
	ipdst.append(ipdst_c)
	ipsrc.append(ipsrc_c)

# print macsrc
# print macdst
# print macsrc_h
# print macdst_h
# print ipdst
# print ipsrc

data_t= str(now.hour)+""+str(now.minute)+""+str(now.second)                     
print now.minute                                                                
create_dir="pcap_bng_dl_ts_"+str(entries)+"_"+data_t 
os.system("mkdir "+ create_dir)                                                 
#IP(dst='192.168.0.'+str(p+1),src='10.0.0.'+str(p+1))/  

#########
i = 0
print "entries : "+ str(entries)
for i in range(0, 7):
    print "i = "+str(i)
    p = 0
    ip_count = 0
    for p in range(0, entries):
       if i == 0:
           ip_src0 = randint(1,250)
           ip_src1 = randint(1,250)
           ip_dst0 = randint(1,250)
           ip_dst1 = randint(1,250)
           #if (entries < 100):
           #    tcp_dst = randint(1,100)
           #else:
           #    tcp_dst = randint(1,250)
           FILE = "echo "+str(macsrc[p])+" 10.0."+str(ip_dst0)+"."+str(ip_dst1)+" " + str(ipsrc[p])+ " " +str(tcp_dest[p])+ " 1 >> "+create_dir +"/trace_trPR_bng_dl_" + str(entries) + "_"+data_t +".txt"  
           os.system(FILE)
            
       pkts.append(
       UDP(dport=1230, sport=1129)/
       UDP(dport=1230, sport=1129)/
       Ether(dst='aa:1b:eb:df:44:3d',src=macsrc[p])/
       IP(dst=ipdst[p],src='192.168.'+str(ip_src1) +'.'+str(ip_src0))/
       TCP(sport=20, dport=int(tcp_dest[p]) )/
       Raw(RandString(size=pktsize[i])))
    pname = "./" + create_dir+"/nfpa.trPR_bng_dl_%d_%s.%dbytes.pcap" % (entries,data_t, pktsize[i]+70+4) #Update the name depending of the Use-Case, use the same format
    #pnamec = "PCAP/nfpa.trPR_tcp_%d_random.%dbytes.pcap" % (entries, pktsize[i]+78+4)  #14 (eth) + 20 (ip4) + 20 (tcp) = 54
    #copy = "scp " + pnamec + " macsad@10.1.1.29:/home/macsad/nfpa/PCAP"
    wrpcap(pname,pkts)
    del pkts[:] #Don't delete this line
    #os.system(copy)

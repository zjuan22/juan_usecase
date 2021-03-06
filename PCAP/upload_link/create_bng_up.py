#!/usr/bin/env python

import os,sys,string,random
from random import shuffle
import argparse
from random import randint

from scapy.all import *
import sys
from datetime import datetime
now = datetime.now()

#rint now.year
#print now.month
#print now.day


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
pktsize = [0 ,46, 174,430 ,942, 1198, 1436] #Don't update the pktsizes

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
	ipdst.append(ipdst_c)
	ipsrc.append(ipsrc_c)

# print macsrc
# print macdst
# print macsrc_h
# print macdst_h
# print ipdst
# print ipsrc
#########


data_t= str(now.hour)+""+str(now.minute)+""+str(now.second)
print now.minute
create_dir="pcap_"+data_t 
os.system("mkdir "+ create_dir)
#IP(dst='192.168.0.'+str(p+1),src='10.0.0.'+str(p+1))/

i = 0
for i in range(0, 7):
    print "i = "+str(i)
    p = 0
    for p in range(0, entries):
        
       ip_src_outter0 = randint(1,250)
       ip_src_outter1 = randint(1,250)
       index0 = randint(1,250)
       index1 = randint(1,250)
       index2 = randint(1,250)
       index3 = randint(1,250)
       ip_src = str(index0)+'.'+str(index1)+'.'+str(index2)+'.'+str(index3)
       if p > 100000: sys.exit(1)
       pkts.append(Ether(dst='aa:1b:eb:df:44:3d',src=macsrc[p])/
       IP(dst='4.0.0.1',src='4.0.'+str(ip_src_outter1)+'.'+str(ip_src_outter0))/
       GRE()/
       IP(dst=ipdst[p] ,src=ipsrc[p])/
       TCP(sport=20, dport=80)/Raw(RandString(size=pktsize[i])))
       
       if i==0: 
          #Create trace file
          #FILE = "echo " + macsrc_h[p] + " " + '10.0.0.'+str(p+1)+ " " + '192.168.0.'+str(p+1)  +  " " +str(r[index])+" 1 >> PCAP/trace_trPR_bng_ul" + str(entries) + "_random.txt"
          FILE = "echo " + macsrc_h[p] + " " + str(ipsrc[p])+ " " + str(ipdst[p])  +  " " +str(r[index0])+" 1 >> "+create_dir+"/trace_trPR_bng_ul_" + str(entries) + "_"+data_t+".txt"
          os.system(FILE)

    pname = "./"+create_dir+"/nfpa.trPR_bng_ul_%d_%s.%dbytes.pcap" % (entries,data_t, pktsize[i]+78+4) #Update the name depending of the Use-Case, use the same format
    #pnamec = "PCAP/nfpa.trPR_gre_%d_random.%dbytes.pcap" % (entries, pktsize[i]+42+4)
    #pnamec = "PCAP/nfpa.trPR_gre_%d_random.%dbytes.pcap" % (entries, pktsize[i]+78+4)
    #copy = "scp " + pnamec + " macsad@10.1.1.29:/home/macsad/nfpa/PCAP"
    wrpcap(pname,pkts)
    #os.system(copy)
    del pkts[:] #Don't delete this line

    
copy = "scp PCAP/trace_trPR_l2_" + str(entries) + "_random.txt" + " root@10.1.1.27:/root/Fabricio/mac_ipv6_gyn/traces/"
#os.system(copy)
copy = "scp PCAP/trace_trPR_ipv4_" + str(entries) + "_random.txt" + " root@10.1.1.27:/root/Fabricio/mac_ipv6_gyn/traces/"
#os.system(copy)

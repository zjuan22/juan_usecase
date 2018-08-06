#!/usr/bin/env python

import os
import string
import csv
import sys
import getopt

from array import array

units = '0'

#pkt_n = [64, 128, 256, 512, 1024, 1280]
#pkt_n = [64, 128, 256, 512, 1024, 1280]
pkt_n = [82, 128, 256, 512, 1024, 1280] #gre case
#Getting the name of all the data files created
def get_name( data_rep, tests, pktio_n, pktio_s, pkt_n):
	file = [None] * (data_rep)
	for x in range(0, (data_rep)):
		file_n = tests + "_" + pktio_n[pktio_s] + "_" +  str(pkt_n[x]) + "_"
		#print file_n
		#Searching for the .data file name || use the tmp/test.txt to save the name
		#FILE = 'ls /home/macsad/nfpa/res/p4/kernel/xeon/virt_no/10_G/ | grep ' + file_n + " | grep data > tmp/test.txt"
		FILE = "ls /home/macsad/CBT/cbt/res/P4/kernel/intel\ xeon/virt_no/10_G/ | grep " + file_n + " | grep data > tmp/test.txt"
		print FILE
		os.system(FILE)
		#Get the name from the tmp/test.txt
		f = open('tmp/test.txt', 'r')
		texto = f.read()
		f.seek(0, 0)
		texto = f.read(len(texto)-1)
		print "tesssssto:  " +  texto
		f.close()
		#print x
		#At file[] is storage the complete .dat file name and route, starting from pkt 64
                # old CBT folder
		file[x] = "/home/macsad/CBT/cbt/res/P4/kernel/intel xeon/virt_no/10_G/" + texto
                # new nfpa 
                #file[x] = "/home/macsad/nfpa/res/p4/kernel/xeon/virt_no/10_G/" + texto

		#print t_file[x]
		print t_file[x]
	return file;

#Creating graph with the correspond pktio selected
def c_graph(info, name_g):
	#ODPS 7 pkts
	if info == '0':
		if units == '0':
			gnuplot = "gnuplot " + "graph/odp.gnu"
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + ".cvs"
			os.system(data_created)
			graph_created = "cp odps.eps res_gre/" + name_g + ".eps"
			os.system(graph_created)
                        os.system("cat res_gre/"+name_g+".cvs")
		if units == '1':
			gnuplot = "gnuplot " + "graph/odp_pps.gnu"
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + "_pps.cvs"
			os.system(data_created)
			graph_created = "cp odps_pps.eps res_gre/" + name_g + "_pps.eps"
			os.system(graph_created)
                        os.system("cat res_gre/"+name_g+"_pps.cvs")
	#DPDK 7 pkts
	if info == '1':
		if units == '0':
			gnuplot = "gnuplot " + "graph/dpdk.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + ".cvs"
			os.system(data_created)
			graph_created = "cp odpd.eps res_gre/" + name_g + ".eps"
			os.system(graph_created)
                        os.system("cat res_gre/"+name_g+".cvs")
		if units == '1':
			gnuplot = "gnuplot " + "graph/dpdk_pps.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + "_pps.cvs"
			os.system(data_created)
			graph_created = "cp odpd_pps.eps res_gre/" + name_g + "_pps.eps"
			os.system(graph_created)
                        os.system("cat res_gre/"+name_g+"_pps.cvs") 
	#NETMAP 7 pkts
	if info == '2':
		if units == '0':
			gnuplot = "gnuplot " + "graph/netmap.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + ".cvs"
			os.system(data_created)
			graph_created = "cp odpn.eps res_gre/" + name_g + ".eps"
			os.system(graph_created)
                        os.system("cat res_gre/"+name_g+".cvs")
		if units == '1':
			gnuplot = "gnuplot " + "graph/netmap_pps.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + "_pps.cvs"
			os.system(data_created)
			graph_created = "cp odpn_pps.eps res_gre/" + name_g + "_pps.eps"
			os.system(graph_created)
                        os.system("cat res_gre/"+name_g+"_pps.cvs")
	#ODPDD
	if info == '3':
		if units == '0':
			gnuplot = "gnuplot " + "graph/odpdd.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + ".cvs"
			os.system(data_created)
			graph_created = "cp odpdd.eps res_gre/" + name_g + ".eps"
			os.system(graph_created)
		if units == '1':
			gnuplot = "gnuplot " + "graph/odpdd_pps.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + "_pps.cvs"
			os.system(data_created)
			graph_created = "cp odpdd_pps.eps res_gre/" + name_g + "_pps.eps"
			os.system(graph_created)
	#odps-odpd 7 pkts
	if info == '4':
		if units == '0':
			gnuplot = "gnuplot " + "graph/odp_dpdk.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + ".cvs"
			os.system(data_created)
			graph_created = "cp odps_odpd.eps res_gre/" + name_g + ".eps"
			os.system(graph_created)
		if units == '1':
			gnuplot = "gnuplot " + "graph/odp_dpdk_pps.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + "_pps.cvs"
			os.system(data_created)
			graph_created = "cp odps_odpd_pps.eps res_gre/" + name_g + "_pps.eps"
			os.system(graph_created)
	#odps-odpn 7 pkts
	if info == '5':
		if units == '0':
			gnuplot = "gnuplot " + "graph/odp_netmap.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + ".cvs"
			os.system(data_created)
			graph_created = "cp odps_odpn.eps res_gre/" + name_g + ".eps"
			os.system(graph_created)
		if units == '1':
			gnuplot = "gnuplot " + "graph/odp_netmap_pps.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + "_pps.cvs"
			os.system(data_created)
			graph_created = "cp odps_odpn_pps.eps res_gre/" + name_g + "_pps.eps"
			os.system(graph_created)
	#odps-odpdd 7 pkts
	if info == '6':
		if units == '0':
			gnuplot = "gnuplot " + "graph/odp_odpdd.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + ".cvs"
			os.system(data_created)
			graph_created = "cp odps_odpdd.eps res_gre/" + name_g + ".eps"
			os.system(graph_created)
		if units == '1':
			gnuplot = "gnuplot " + "graph/odp_odpdd_pps.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + "_pps.cvs"
			os.system(data_created)
			graph_created = "cp odps_odpdd_pps.eps res_gre/" + name_g + "_pps.eps"
			os.system(graph_created)
	#odpd-odpn 7 pkts
	if info == '7':
		if units == '0':
			gnuplot = "gnuplot " + "graph/dpdk_netmap.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + ".cvs"
			os.system(data_created)
			graph_created = "cp odpd_odpn.eps res_gre/" + name_g + ".eps"
			os.system(graph_created)
		if units == '1':
			gnuplot = "gnuplot " + "graph/dpdk_netmap_pps.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + "_pps.cvs"
			os.system(data_created)
			graph_created = "cp odpd_odpn_pps.eps res_gre/" + name_g + "_pps.eps"
			os.system(graph_created)
	#odpd-odpdd 7 pkts
	if info == '8':
		if units == '0':
			gnuplot = "gnuplot " + "graph/dpdk_odpdd.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + ".cvs"
			os.system(data_created)
			graph_created = "cp odpd_odpdd.eps res_gre/" + name_g + ".eps"
			os.system(graph_created)
		if units == '1':
			gnuplot = "gnuplot " + "graph/dpdk_odpdd_pps.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + "_pps.cvs"
			os.system(data_created)
			graph_created = "cp odpd_odpdd_pps.eps res_gre/" + name_g + "_pps.eps"
			os.system(graph_created)
	#odpn-odpdd 7 pkts
	if info == '9':
		if units == '0':
			gnuplot = "gnuplot " + "graph/netmap_odpdd.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv rese" + name_g + ".cvs"
			os.system(data_created)
			graph_created = "cp odpn_odpdd.eps res_gre/" + name_g + ".eps"
			os.system(graph_created)
		if units == '1':
			gnuplot = "gnuplot " + "graph/netmap_odpdd_pps.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + "_pps.cvs"
			os.system(data_created)
			graph_created = "cp odpn_odpdd_pps.eps res_gre/" + name_g + "_pps.eps"
			os.system(graph_created)
	#odps-odpd-odpn 7 pkts
	if info == '10':
		if units == '0':
			gnuplot = "gnuplot " + "graph/odp_dpdk_netmap.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + ".cvs"
			os.system(data_created)
			graph_created = "cp odps_odpd_odpn.eps res_gre/" + name_g + ".eps"
			os.system(graph_created)
		if units == '1':
			gnuplot = "gnuplot " + "graph/odp_dpdk_netmap_pps.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + "_pps.cvs"
			os.system(data_created)
			graph_created = "cp odps_odpd_odpn_pps.eps res_gre/" + name_g + "_pps.eps"
			os.system(graph_created)
	#odps-odpd-odpdd 7 pkts
	if info == '11':
		if units == '0':
			gnuplot = "gnuplot " + "graph/odp_dpdk_odpdd.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + ".cvs"
			os.system(data_created)
			graph_created = "cp odps_odpd_odpdd.eps res_gre/" + name_g + ".eps"
			os.system(graph_created)
		if units == '1':
			gnuplot = "gnuplot " + "graph/odp_dpdk_odpdd_pps.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + "_pps.cvs"
			os.system(data_created)
			graph_created = "cp odps_odpd_odpdd_pps.eps res_gre/" + name_g + "_pps.eps"
			os.system(graph_created)
	#odps-odpn-odpdd
	if info == '12':
		if units == '0':
			gnuplot = "gnuplot " + "graph/odp_netmap_odpdd.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + ".cvs"
			os.system(data_created)
			graph_created = "cp odps_odpn_odpdd.eps res_gre/" + name_g + ".eps"
			os.system(graph_created)
		if units == '1':
			gnuplot = "gnuplot " + "graph/odp_netmap_odpdd_pps.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + "_pps.cvs"
			os.system(data_created)
			graph_created = "cp odps_odpn_odpdd_pps.eps res_gre/" + name_g + "_pps.eps"
			os.system(graph_created)
	#odpd-odpn-odpdd 7 pkts
	if info == '13':
		if units == '0':
			gnuplot = "gnuplot " + "graph/dpdk_netmap_odpdd.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + ".cvs"
			os.system(data_created)
			graph_created = "cp odpd_odpn_odpsdd.eps res_gre/" + name_g + ".eps"
			os.system(graph_created)
		if units == '1':
			gnuplot = "gnuplot " + "graph/dpdk_netmap_odpdd_pps.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + "_pps.cvs"
			os.system(data_created)
			graph_created = "cp odpd_odpn_odpsdd_pps.eps res_gre/" + name_g + "_pps.eps"
			os.system(graph_created)
	#odps-odpd-odpn-odpdd 7 pkts
	if info == '14':
		if units == '0':
			gnuplot = "gnuplot " + "graph/odp_dpdk_netmap_odpdd.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + ".cvs"
			os.system(data_created)
			graph_created = "cp odps_odpd_odpn_odpdd.eps res_gre/" + name_g + ".eps"
			os.system(graph_created)
		if units == '1':
			gnuplot = "gnuplot " + "graph/odp_dpdk_netmap_odpdd_pps.gnu" 
			os.system(gnuplot)
			print "Graph generated"
			#Saving data info and graph
			data_created = "cp graph/data.csv res_gre/" + name_g + "_pps.cvs"
			os.system(data_created)
			graph_created = "cp odps_odpd_odpn_odpdd_pps.eps res_gre/" + name_g + "_pps.eps"
			os.system(graph_created)
	return;

#Get the information of the "file" //pkt and avr and save into results[]
def get_info(data_rep, file):
	results = [None] * 2
	pkt = [None] * (data_rep)
	avr = [None] * (data_rep)
	for x in range(0, (data_rep)):	
		with open(str(file[x]), 'rb') as f:
			reader = csv.reader(f)
			cl=0
			for row in reader:	
				if cl == 1:
					pkt[x]=float(row[0])
					#print pkt[x]
					if units == '0':
						avr[x]=float(row[16]) #return to 15  bi 33
					if units == '1':
						avr[x]=float(row[6]) #return to 6  bi 24
					#print avr[x]
				cl=cl+1
				#print cl
	results[0]=pkt
	results[1]=avr
	return results;

#Check inputs graph.py -i <name> -o <pktio> -m <Mbps/Kpps>
def inputs(argv):
	i_name = ''
	i_pktio = ''
	i_units = ''
	info = [None] * (3)
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["name=","pktio=","units="])
	except getopt.GetoptError:
		print 'graph.py -i <name> -o <pktio> -m <units> ?'
		print """
		-o options
	odps (socket mmap)	 0
	odpd (dpdk)		 1
	odpn (netmap)		 2
	odpdd (odp-dpdk)	 3
	-- Graph Conbinations --
	odps-odpd		 4
	odps-odpn		 5
	odps-odpdd		 6
	odpd-odpn		 7
	odpd-odpdd 		 8
	odpn-odpdd 		 9
	odps-odpd-odpn 		 10
	odps-odpd-odpdd 	 11
	odps-odpn-odpdd 	 12
	odpd-odpn-odpdd 	 13
	odps-odpd-odpn-odpdd	 14

		-m options
	Mbps			 0
	Kpps			 1"""
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'graph.py -i <name> -o <pktio> -m <units>'
			print """
		-o options
	odps (socket mmap)	 0
	odpd (dpdk)		 1
	odpn (netmap)		 2
	odpdd (odp-dpdk)	 3
	-- Graph Conbinations --
	odps-odpd		 4
	odps-odpn		 5
	odps-odpdd		 6
	odpd-odpn		 7
	odpd-odpdd 		 8
	odpn-odpdd 		 9
	odps-odpd-odpn 		 10
	odps-odpd-odpdd 	 11
	odps-odpn-odpdd 	 12
	odpd-odpn-odpdd 	 13
	odps-odpd-odpn-odpdd 	 14

		-m options
	Mbps			 0
	Kpps			 1"""
			sys.exit()
		elif opt in ("-i", "--iname"):
			i_name = arg
		elif opt in ("-o", "--pktio"):
			i_pktio = arg
		elif opt in ("-m", "--units"):
			i_units = arg
	#print 'File name: ', i_name
	#print 'pktio: ', i_pktio
	#print 'units:', i_units
	return; 


#####MAIN#####

###VARIABLES
#TODO define name format
#<<name_pktio_pkt>>
#Supported pkt sizes
#pkt_n = [82]
#pkt_n = [64]
#pkt_n = [82, 128, 256, 512, 1024, 1280]
#pkt_n = [1518]
data_rep= len(pkt_n)
#data_rep= 6 

print "data rep: " + str(data_rep)
#Supported formats // more can be added
pktio_n = ["odp", "odpD", "odpN", "odpdd"]
#pktio_n = ["odps", "odpd", "odpn", "odpdd"]
t_file = [None] * (data_rep)
t_file_md = [None] * (data_rep)
t_file_mn = [None] * (data_rep)
t_file_mdd = [None] * (data_rep)
resutls = [None] * 2
pkt = [None] * (data_rep)
avr = [None] * (data_rep)
avr_d = [None] * (data_rep)
avr_n = [None] * (data_rep)
avr_dd = [None] * (data_rep)
info = [None] * (3)
odp = 0
dpdk = 0
netmap = 0
odpdd = 0

## inputs pktio
#	odps (socket mmap)	 0
#	odpd (dpdk)			 1
#	odpn (netmap)		 2
#	odpdd (odp-dpdk)	 3
#	-- Graph Conbinations --
#	odps-odpd			 4
#	odps-odpn			 5
#	odps-odpdd			 6
#	odpd-odpn			 7
#	odpd-odpdd 			 8
#	odpn-odpdd 			 9
#	odps-odpd-odpn 		 10
#	odps-odpd-odpdd 	 11
#	odps-odpn-odpdd 	 12
#	odpd-odpn-odpdd 	 13
#	odps-odpd-odpn-odpdd 14
##
#Get the inputs graph.py -i <name> -o <pktio> -m <units>
#inputs(sys.argv[1:])
print "*********" + str(sys.argv[1:])

#info[0] name // info[1] pktio (according to table) // more inputs can be added
#info[0] = sys.argv[1]
#info[1] = sys.argv[3]
#info[2] = sys.argv[5]
info[0] = sys.argv[2]
info[1] = sys.argv[4]
info[2] = sys.argv[6]
#information prints
print 'File name: ', info[0]
print 'pktio: ', info[1]
print 'units: ', info[2]
#tests name of the file saved 
tests = info[0]
units = info[2]

#source 1 enabled - 0 disabled
#pktio_s select if the data is from ODP DPDK or NETMAP
if info[1] == '0':
	odp = 1
	pktio_s = 0
if info[1] == '1':
	dpdk = 1
	pktio_s = 1
if info[1] == '2':
	netmap = 1
	pktio_s = 2
if info[1] == '3':
	odpdd = 1
	pktio_s = 3

#Getting the name of all the data files created
#File names saved at t_file if there is more than one use t_file_md, t_file_mn and t_file_mdd

#Reading the data from the t_file //pkt //avr || use avr_d and avr_n for more than one t_file
#TODO add support for more inputs, dependig of the main script
#Save info into .csv // delimiter \t
data=open('graph/data.csv', 'w+')
# ######################################Only get pkt size from the first t_file ######################

if (odp == 1) or (dpdk == 1) or (netmap == 1) or (odpdd == 1):
	t_file = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
        
	#get info
	results = get_info(data_rep, t_file)
	pkt = results[0]
	#print pkt
	avr = results[1]
	#print avr
	for x in range(0, (data_rep)):
           if units == '0': 
		data.write("%d\t%d\t%f\n" % ((x+1), pkt[x], avr[x]/1000))
		#data.write("%d\t%d\t%f\n" % ((x+1), pkt[x], avr[x]))

           else:
		data.write("%d\t%d\t%f\n" % ((x+1), pkt[x], avr[x]))
                  
#odps-odpd
elif info[1] == '4':
	pktio_s = 0
	t_file = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	pktio_s = 1
	t_file_md = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	#get info
	results = get_info(data_rep, t_file)
	pkt = results[0]
	avr = results[1]
	results = get_info(data_rep, t_file_md)
	avr_d = results[1]
	for x in range(0, (data_rep)):
		data.write("%d\t%d\t%f\t%f\n" % ((x+1), pkt[x], avr[x], avr_d[x]))

#odps-odpn
elif info[1] == '5':
	pktio_s = 0
	t_file = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	pktio_s = 2
	t_file_mn = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	#get info
	results = get_info(data_rep, t_file)
	pkt = results[0]
	avr = results[1]
	results = get_info(data_rep, t_file_mn)
	avr_n = results[1]
	for x in range(0, (data_rep)):
		data.write("%d\t%d\t%f\t%f\n" % ((x+1), pkt[x], avr[x], avr_n[x]))

#odps-odpdd
elif info[1] == '6':
	pktio_s = 0
	t_file = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	pktio_s = 3
	t_file_mdd = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	#get info
	results = get_info(data_rep, t_file)
	pkt = results[0]
	avr = results[1]
	results = get_info(data_rep, t_file_mdd)
	avr_dd = results[1]
	for x in range(0, (data_rep)):
		data.write("%d\t%d\t%f\t%f\n" % ((x+1), pkt[x], avr[x], avr_dd[x]))

#odpd-odpn
elif info[1] == '7':
	pktio_s = 1
	t_file_md = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	pktio_s = 2
	t_file_mn = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	#get info
	results = get_info(data_rep, t_file_md)
	pkt = results[0]
	avr_d = results[1]
	results = get_info(data_rep, t_file_mn)
	avr_n = results[1]
	for x in range(0, (data_rep)):
		data.write("%d\t%d\t%f\t%f\n" % ((x+1), pkt[x], avr_d[x], avr_n[x]))

#odpd-odpdd
elif info[1] == '8':
	pktio_s = 1
	t_file_md = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	pktio_s = 3
	t_file_mdd = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	#get info
	results = get_info(data_rep, t_file_md)
	pkt = results[0]
	avr_d = results[1]
	results = get_info(data_rep, t_file_mdd)
	avr_dd = results[1]
	for x in range(0, (data_rep)):
		data.write("%d\t%d\t%f\t%f\n" % ((x+1), pkt[x], avr_d[x], avr_dd[x]))

#odpn-odpdd
elif info[1] == '9':
	pktio_s = 2
	t_file_mn = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	pktio_s = 3
	t_file_mdd = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	#get info
	results = get_info(data_rep, t_file_mn)
	pkt = results[0]
	avr_n = results[1]
	results = get_info(data_rep, t_file_mdd)
	avr_dd = results[1]
	for x in range(0, (data_rep)):
		data.write("%d\t%d\t%f\t%f\n" % ((x+1), pkt[x], avr_n[x], avr_dd[x]))

#odps-odpd-odpn
elif info[1] == '10':
	pktio_s = 0
	t_file = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	pktio_s = 1
	t_file_md = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	pktio_s = 2
	t_file_mn = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	#get info
	results = get_info(data_rep, t_file)
	pkt = results[0]
	avr = results[1]
	results = get_info(data_rep, t_file_md)
	avr_d = results[1]
	results = get_info(data_rep, t_file_mn)
	avr_n = results[1]
	for x in range(0, (data_rep)):
		data.write("%d\t%d\t%f\t%f\t%f\n" % ((x+1), pkt[x], avr[x], avr_d[x], avr_n[x]))

#odps-odpd-odpdd
elif info[1] == '11':
	pktio_s = 0
	t_file = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	pktio_s = 1
	t_file_md = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	pktio_s = 3
	t_file_mdd = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	#get info
	results = get_info(data_rep, t_file)
	pkt = results[0]
	avr = results[1]
	results = get_info(data_rep, t_file_md)
	avr_d = results[1]
	results = get_info(data_rep, t_file_mdd)
	avr_dd = results[1]
	for x in range(0, (data_rep)):
		data.write("%d\t%d\t%f\t%f\t%f\n" % ((x+1), pkt[x], avr[x], avr_d[x], avr_dd[x]))

#odps-odpn-odpdd
elif info[1] == '12':
	pktio_s = 1
	t_file = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	pktio_s = 2
	t_file_mn = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	pktio_s = 3
	t_file_mdd = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	#get info
	results = get_info(data_rep, t_file)
	pkt = results[0]
	avr = results[1]
	results = get_info(data_rep, t_file_mn)
	avr_n = results[1]
	results = get_info(data_rep, t_file_mdd)
	avr_dd = results[1]
	for x in range(0, (data_rep)):
		data.write("%d\t%d\t%f\t%f\t%f\n" % ((x+1), pkt[x], avr[x], avr_n[x], avr_dd[x]))

#odpd-odpn-odpdd
elif info[1] == '13':
	pktio_s = 1
	t_file_md = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	pktio_s = 2
	t_file_mn = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	pktio_s = 3
	t_file_mdd = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	#get info
	results = get_info(data_rep, t_file_md)
	pkt = results[0]
	avr_d = results[1]
	results = get_info(data_rep, t_file_mn)
	avr_n = results[1]
	results = get_info(data_rep, t_file_mdd)
	avr_dd = results[1]
	for x in range(0, (data_rep)):
		data.write("%d\t%d\t%f\t%f\t%f\n" % ((x+1), pkt[x], avr_d[x], avr_n[x], avr_dd[x]))

#odps-odpd-odpn-odpdd
elif info[1] == '14':
	pktio_s = 1
	t_file = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	pktio_s = 2
	t_file_md = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	pktio_s = 3
	t_file_mn = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	pktio_s = 3
	t_file_mdd = get_name(data_rep, tests, pktio_n, pktio_s, pkt_n)
	#get info
	results = get_info(data_rep, t_file)
	pkt = results[0]
	avr = results[1]
	results = get_info(data_rep, t_file_md)
	avr_d = results[1]
	results = get_info(data_rep, t_file_mn)
	avr_n = results[1]
	results = get_info(data_rep, t_file_mdd)
	avr_dd = results[1]
	for x in range(0, (data_rep)):
		data.write("%d\t%d\t%f\t%f\t%f\n" % ((x+1), pkt[x], avr[x], avr_d[x], avr_n[x], avr_dd[x]))

data.close()

#generate graph with the correspond pktio (info[1]) selected as input
c_graph(info[1], info[0])


##END##


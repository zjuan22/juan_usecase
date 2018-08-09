#!/bin/bash

echo "Script started... "
# set default values for variables if they are not already defined
MAKE_CMD=${MAKE_CMD-make}

# Compile Controller
pwd=`pwd`
echo $pwd
cd ..
#cd src/hardware_dep/shared/ctrl_plane
#TS=/root/Juan/myrepo/
TS=/home/lion/workspace/myrepo
cd $TS/ctrl_plane 

#gcc -Wall -pthread -std=c99  handlers.c controller.c messages.c sock_helpers.c threadpool.c fifo.c mac_l3_controller_ipv6.c -o $pwd/mac_l3_controller_ipv6
#gcc -Wall -pthread -std=c99  handlers.c controller.c messages.c sock_helpers.c threadpool.c fifo.c mac_controller.c -o $pwd/mac_controller
gcc -Wall -pthread -std=c99  handlers.c controller.c messages.c sock_helpers.c threadpool.c fifo.c mac_bng_controller_ul.c -o $pwd/mac_bng_controller_ul
#gcc -Wall -pthread -std=c99  handlers.c controller.c messages.c sock_helpers.c threadpool.c fifo.c mac_bng_controller_dl.c -o $pwd/mac_bng_controller_dl
#gcc -Wall -pthread -std=c99  handlers.c controller.c messages.c sock_helpers.c threadpool.c fifo.c nat_controller_up.c -o $pwd/nat_controller_ul

cd $pwd/..
echo $(pwd)
#make clean
#make all
#ERROR_CODE=$?
#if [ "$ERROR_CODE" -ne 0 ]; then
#    echo Controller compilation failed with error code $ERROR_CODE
#    exit 1
#fi
#cd -

# Restart mac controller in background
killall mac_controller
killall mac_l2_l3_controller
killall mac_l3_controller
killall mac_l3_nhg_controller
killall mac_l3_controller_ipv6
killall mac_bng_controller_dl 
killall mac_bng_controller_ul 
killall nat_controller_ul

pkill -f mac_controller
pkill -f mac_l2_l3_controller
pkill -f mac_l3_controller
pkill -f mac_l3_nhg_controller
pkill -f mac_l3_controller_ipv6
pkill -f mac_bng_controller_dl
pkill -f mac_bng_controller_ul
pkill -f nat_controller_ul
 

#./old_mk/mac_bng_controller_ul $TS/PCAP/upload_link/PCAP/trace_trPR_bng_ul100_random.txt & 
./old_mk/mac_bng_controller_ul $TS/PCAP/upload_link/pcap_19290/trace_trPR_bng_ul_100_19290.txt & 

echo "Controller started... "

echo "Creating Datapath Logic from P4 source."
rm -rf build

#python src/transpiler.py examples/p4_src/l2_fwd.p4
#python src/transpiler.py examples/p4_src/l2_l3.p4
#python src/transpiler.py examples/p4_src/l3_routing_test.p4
#python src/transpiler.py examples/p4_src/l3_routing_nhg.p4
#python src/transpiler.py examples/p4_src/l3_routing_ipv6.p4
python src/transpiler.py $TS/bng_elte.p4 --p4v 16
#python src/transpiler.py $TS/nat_mac/nat_mac.p4 --p4v 16
ERROR_CODE=$?
if [ "$ERROR_CODE" -ne 0 ]; then
    echo Transpiler failed with error code $ERROR_CODE
    exit 1
fi

cd $pwd
# Compile C sources
make clean;${MAKE_CMD} -j12

rm -rf /tmp/odp*

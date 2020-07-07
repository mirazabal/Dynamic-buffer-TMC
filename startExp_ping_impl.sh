#!/bin/bash
#sleep 1
echo "the variable is equal to  $EXE_A"

cd

cd ~/Desktop/ProjectPath/

ps -A | grep $EXE_A  | awk '{print $1}' | xargs sudo kill -9

if [ ! -d "$DIRECTORY" ]; then
mkdir $DIRECTORY
fi

cd $DIRECTORY

if [ ! -d "$SCENARIO" ]; then
mkdir $SCENARIO
fi

cd $SCENARIO

if [ ! -d "$CASE" ]; then
mkdir $CASE
fi

cd $CASE

sudo ./../../../$EXE_A 0 > $A_DEST_FILE &

sleep 1


sshpass -p "pi" ssh -tt -o StrictHostKeyChecking=no pi@10.0.0.202 << HERE 
cd /home/pi/UDP/client/ 


if [ ! -d "$DIRECTORY" ]; then
mkdir $DIRECTORY
fi
cd $DIRECTORY

if [ ! -d "$SCENARIO" ]; then
mkdir $SCENARIO
fi
cd $SCENARIO

if [ ! -d "$CASE" ]; then
mkdir $CASE
fi
cd $CASE

if [ ! "$CASE" == "7th" ]; then
echo "pi" | sudo -S sysctl net.ipv4.tcp_congestion_control=cubic
fi

if [ "$CASE" == "7th" ]; then
echo "pi" | sudo -S sysctl net.ipv4.tcp_congestion_control=bbr
fi

iperf3 -c 10.0.0.138 -t 200 -M 1500  $NUM_CONN > $IPERF_DEST_FILE &
sleep 3
cd /home/pi/UDP/client

if [ ! -d "$DIRECTORY" ]; then
mkdir $DIRECTORY
fi
cd $DIRECTORY

if [ ! -d "$SCENARIO" ]; then
mkdir $SCENARIO
fi
cd $SCENARIO

if [ ! -d "$CASE" ]; then
mkdir $CASE
fi
cd $CASE

cd /home/pi/UDP/client
./a.out 10.0.0.138 10020 50 3000 > $PING_DEST_FILE &

./a.out 10.0.0.138 10021 $PING_LAT $PING_QUANTITY > $PING_DEST_FILE_2 &

#sshpass -p "pi" ssh -tt -o StrictHostKeyChecking=no pi@10.0.0.202 << HERE 
#iperf3 -c 10.0.0.138 -t 200 -M 1500  $NUM_CONN > $IPERF_DEST_FILE &
#sleep 3
#cd /home/pi/UDP/client
#./a.out 10.0.0.138 10020 $PING_LAT $PING_QUANTITY > $IPERF_DEST_FILE &

HERE
sleep 202

echo "before killing the a.out binary"
ps -A | grep $EXE_A  | awk '{print $1}' | xargs sudo kill -9

kill 0


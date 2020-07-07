# Dynamic-buffer-TMC
Hierarchical 5G Qos queues emulator used to validate the 5G-BDP and the DRQL algorithms. 

# Build Instructions

Download the code: 

1. git clone https://github.com/mirazabal/Dynamic-buffer-TMC

2. cd Dynamic-buffer-TMC

3. sudo python compile.py


At this moment check whether the everything compiled. If it didn't you are probably missing some dependencies. Download them.

We also provide a UDP server and client in case that you want to use them.

4. cd UDP/server

5. g++ -std=c++11 blocking_udp_echo_server.cpp -lboost_system

Copy the blocking_udp_echo_client.cpp file from UDP/client into the DN (e.g., in our article the raspberri py) and build it.

6. g++ -std=c++11 blocking_udp_echo_client.cpp -lboost_system -lpthread

# Use instructions

Start a new iperf3 session in the 5G QoS emulator:

4. iperf3 -s

Start the UDP servers

5. cd UDP/server

6. ./a.out 10020

Redirect the packets from the kernel space to the user space through NFQUEUE with the following command:

7. sudo iptables -A INPUT -j NFQUEUE --queue-num 0

Change the IP addresses, data paths, ssh password and scenarios as desired in the startExp_ping.sh and startExp_ping_impl.sh scripts

8. sudo ./startExp_ping.sh

If everything went fine, you should start traffic flowing into the 5G QoS queue emulator.

Copy the file bdp_1st.py and bdp_2nd.py into the generated folder.

9. Run: python bdp_1st.py for the first scenario and run: python bdp_2nd.py for the second scenario

The dataset used for the emulation can be found at: 

https://www.ucc.ie/en/misl/research/datasets/ivid_4g_lte_dataset/


import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def get_delay(str1):
    f = open(str1, 'r')

    y = []
    x = []
    firstTime = True
    firstVal = 0

    for line in f:
        if line.startswith("UDP Packet with"):
            try:

                s = line.split()[30];
                if firstTime == True:
                 firstTime = False
                 firstVal = float(s)
                n1 = float(s) - firstVal   
                x.append(n1)

                s = line.split()[26];
                n2 = float(s) 

                if n1 > 2500000 and n1 < 192500000:
                    y.append(n2/1000)
            except Exception:
               pass

    print 'Mean value for ' + str1 + ' ' + str(np.mean(y))
    return (np.mean(y), np.std(y))

def get_values(str1):
    f = open(str1, 'r')
    y = []
    x = []
    firstTime = True
    firstVal = 0

    for line in f:
        if line.startswith("UDP Packet with"):
            s = line.split()[6]
            if s == 'inserted':
                s = line.split()[18]
                if firstTime == True:
                     firstTime = False
                firstVal = float(s)
                n = float(s) - firstVal   
                x.append(n)

                s = line.split()[14];
                n1 = float(s) 

                if n > 2500000 and n < 192500000:
                    y.append(n1)

    
    print 'Mean value = ' + str(np.mean(y))
    return (np.mean(y), np.std(y) )

def generate_ping_mean(str1):
    val2 = get_delay(str1 + '/a_20.txt') 
    val3 = get_delay(str1 + '/a_30.txt') 
    val4 = get_delay(str1 + '/a_40.txt') 
    val5 = get_delay(str1 + '/a_50.txt') 
    val6 = get_delay(str1 + '/a_60.txt') 
    val7 = get_delay(str1 + '/a_70.txt') 

    return  (val2[0],val3[0],val4[0],val5[0],val6[0],val7[0]) 

def get_MAC_utilization(str1):
    counter = 0
    total_num_used_res = 0
    total_num_res = 0
    print 'value of str1 = ' + str1
    f = open(str1, 'r')
    y = []
    x = []
    firstTime = True
    firstVal = 0
    for line in f:
        if line.startswith('Packets deque at MAC'):
            try:
                s = line.split()[17];
                if firstTime == True:
                    firstTime = False
                    firstVal = float(s)
                n1 = float(s) - firstVal  
                x.append(n1)

                s = line.split()[6];
                n2 = float(s) 
                if n1 > 2500000 and n1 < 192500000:
                    y.append(n2)
                    counter += 1
                    total_num_used_res += n2
                    total_num_res += int(line.split()[13])
            except Exception:
                pass

    print 'Total number of resources = ' + str(total_num_res) + 'total number of resources used ' +  str( total_num_used_res ) + ' in this times = '  + str(counter) + 'in percentage = ' + str( total_num_used_res / total_num_res )
    return  total_num_used_res/ total_num_res 


def generate_utilization_mean(str1):

    RTT_min = 10
    val2 = get_MAC_utilization(str1 + '/a_20.txt') 
    val3 = get_MAC_utilization(str1 + '/a_30.txt') 
    val4 = get_MAC_utilization(str1 + '/a_40.txt') 
    val5 = get_MAC_utilization(str1 + '/a_50.txt') 
    val6 = get_MAC_utilization(str1 + '/a_60.txt') 
    val7 = get_MAC_utilization(str1 + '/a_70.txt') 

    return  (val2,val3,val4,val5,val6,val7) 


print 'Vanilla case' 
y1 = generate_ping_mean('1st') 

print 'Codel case' 
y5 = generate_ping_mean('3rd')

print 'DRQL' 
y10 = generate_ping_mean('6th')

print 'BBR' 
y11 = generate_ping_mean('7th')

#y12 = generate_ping_mean('8th')
#y13 = generate_ping_mean('9th')

print 'DynRLC' 
y14 = generate_ping_mean('10th')



print '5G-BDP' 
y15 = generate_ping_mean('11th')

print '5G-BDP_ASYNC' 
y16 = generate_ping_mean('12th')


print 'Vanilla case' 
x1 = generate_utilization_mean('1st')
print 'Codel case' 
x5 = generate_utilization_mean('3rd')

print 'DRQL' 
x10 = generate_utilization_mean('6th')

print 'BBR' 
x11 = generate_utilization_mean('7th')

print 'DynRLC' 
x14 = generate_utilization_mean('10th')
print '5G-BDP' 
x15 = generate_utilization_mean('11th')
#print '5G-BDP_ASYNC' 
#x16 = generate_utilization_mean('12th')


(fig, ax) = plt.subplots(1,6)


for x in range(0, 6):
    ax[x].plot(x1[x], y1[x], 'd-' , linewidth = 3.0 , markersize=15, color='cyan')
    ax[x].plot(x5[x], y5[x], '>-' , linewidth = 3.0 , markersize=15, color='blue')
    ax[x].plot(x10[x], y10[x], 'D-' , linewidth = 3.0 , markersize=15, color='red')
    ax[x].plot(x11[x], y11[x], 's-' , linewidth = 3.0 , markersize=15, color='green')
   # ax[x].plot(x12[x], y12[x], 'd-' , linewidth = 3.0 , markersize=15, color='blue')
   # ax[x].plot(x13[x], y13[x], 'd-' , linewidth = 3.0 , markersize=15, color='orange')
    ax[x].plot(x14[x], y14[x], 'p-' , linewidth = 3.0 , markersize=15, color='purple')
    ax[x].plot(x15[x], y15[x], '*-' , linewidth = 3.0 , markersize=15, color='orange')
#    ax[x].plot(x16[x], y16[x], 'h-' , linewidth = 3.0 , markersize=15, color='pink')

# , '5G-BDP_ASYNC'
ax[0].legend(( 'Vanilla','CoDel', 'DRQL', 'BBR', 'DynRLC', '5G-BDP' ), loc='lower left', bbox_to_anchor= (0.0, 1.01), ncol=6, borderaxespad=0, frameon=False, fontsize=22)

ax[0].set_xlabel('Av. Interval 20 ms', fontsize=18) 
ax[1].set_xlabel('Av. Interval 30 ms', fontsize=18) 
ax[2].set_xlabel('Av. Interval 40 ms', fontsize=18) 
ax[3].set_xlabel('Av. Interval 50 ms', fontsize=18) 
ax[4].set_xlabel('Av. Interval 60 ms', fontsize=18) 
ax[5].set_xlabel('Av. Interval 70 ms', fontsize=18) 

plt.suptitle('Normalized Bandwidth Utilization', y=0.05 , fontsize=28)

ax[0].set_ylabel('Delay [ms]', fontsize=28)

ymajor_ticks = np.arange(5,95,5)
xmajor_ticks = np.arange(0.90,1.01,0.02)

for x in range (0,6):
    ax[x].set_ylim(5,95)
    ax[x].set_yticks(ymajor_ticks)

    ax[x].tick_params(axis='both', which='major', labelsize=11)
    ax[x].set_xticks(xmajor_ticks)
    ax[x].set_xlim(0.90,1.0)
    ax[x].grid()

plt.rc('axes', titlesize=18)
plt.rc('xtick',  labelsize=18)
plt.rc('ytick',  labelsize=18)
plt.show()


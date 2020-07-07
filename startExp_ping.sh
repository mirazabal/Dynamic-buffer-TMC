#!/bin/bash

_A_DEST_FILE="a_"
_PING_DEST_FILE="ping_"
_IPERF_DEST_FILE="iperf_"
_FILE_END=".txt"
EXE_A="a.out"
CASE="1st"
DIRECTORY="JOURNAL_PING_DYN_FINAL_PEDESTRIAN_NEW"
#SCENARIO="2nd_scenario"
PING_LAT="10"	
PING_QUANTITY="3000"

array_exe_sce_0=('a11.out' 'a17.out' 'a110.out' 'a111.out' 'a112.out' 'a113.out' 'a114.out' 'a115.out' 'a116.out' 'a117.out')
#array_exe_sce_0=( 'a21.out' 'a23.out' 'a26.out' 'a27.out' 'a28.out' 'a29.out' 'a210.out' 'a211.out' 'a212.out')

array_cases=('1st' '7th' '10th' '11th' '12th' '13th' '14th' '15th' '16th' '17th')
#array_cases=('1st' '3rd' '6th' '7th' '8th' '9th' '10th' '11th' '12th' )

array_scenarios=('1st_scenario')
#array_scenarios=('2nd_scenario')

array_ms=( '20' '30' '40' '50' '60' '70' )
array_quantity=( '7500' '5000' '3750' '3000' '2500' '2150' )

idx_sce=0
while [ $idx_sce -le 1 ];
do
  SCENARIO=${array_scenarios[$idx_sce]}

  idx_cases=0
  while [ $idx_cases -le 9 ];
  do

    if [ $idx_sce == 0 ]; then    
      EXE_A=${array_exe_sce_0[$idx_cases]}
    fi

    if [ $idx_sce == 1 ]; then    
      EXE_A=${array_exe_sce_1[$idx_cases]}
    fi

    CASE=${array_cases[$idx_cases]}
    echo "the value of the exe is equal to ${array_exe_sce[$idx_cases]}"

    idx_ping=0
    while [ $idx_ping -le 5 ];
    do
      A_DEST_FILE="$_A_DEST_FILE${array_ms[$idx_ping]}.txt"
      PING_DEST_FILE="$_PING_DEST_FILE${array_ms[$idx_ping]}.txt"
      PING_DEST_FILE_2="$_PING_DEST_FILE${array_ms[$idx_ping]}.txt_2"
      IPERF_DEST_FILE="$_IPERF_DEST_FILE${array_ms[$idx_ping]}.txt"

      PING_LAT=${array_ms[$idx_ping]}
      PING_LAT_FILE ="${array_ms[$idx_ping]}.txt"

      PING_QUANTITY=${array_quantity[$idx_ping]}


      export EXE_A
      export A_DEST_FILE
      export PING_DEST_FILE
      export PING_DEST_FILE_2
      export PING_DEST_FILE_3
      export PING_DEST_FILE_4

      export IPERF_DEST_FILE
      export PING_LAT
      export PING_LAT_FILE
      export PING_QUANTITY
      export CASE
      export DIRECTORY
      export SCENARIO
      ./startExp_ping_impl.sh & 
      pid[0]=$!
      sleep 210
      ps -A | grep $EXE_A  | awk '{print $1}' | xargs sudo kill -9
      trap INT "kill $(pid[0]);"

      idx_ping=$(( $idx_ping + 1 )) 
    done

    echo "into new case"
    ps -A | grep $EXE_A  | awk '{print $1}' | xargs sudo kill -9
    idx_cases=$(( $idx_cases + 1 )) 

  done
  idx_sce=$(( $idx_sce + 1 )) 
done

kill 0


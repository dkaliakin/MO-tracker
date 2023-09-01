#!/bin/bash

###################
# This shell script 
# 1) runs python MO-tracker 
# 2) removes RasOrb file of N-2 step to safe disk space
####################

### Find step number from md.energies
iter=$(wc -l $InpDir/$Project.md.energies | awk '{print $1}')
iter=$((iter-1))

### Create MO track list
if [ $iter -eq 1 ]
then
   echo "step-1 single MO file" > $InpDir/MO-track-list.txt
fi

### Run python MO-tracker
if [ $iter -gt 1 ]
then
   comp1=$((iter-1))
   comp2=$iter
   result=$(python3 $InpDir/Track-MO.py $InpDir/$Project-iter-${comp1}.RasOrb $InpDir/$Project-iter-${comp2}.RasOrb)
   echo "step-$iter $result" >> $InpDir/MO-track-list.txt
fi

### Remove the RasOrb file of N-2 step ###
if [ $iter -gt 2 ]
then
   burn=$((iter-2))
   rm $InpDir/$Project-iter-${burn}.RasOrb
fi

#!/bin/bash

#####################
# This shell script removes previous
# MO track data, iter-A.RasOrb, and md.energies
# to avoid MO track errors
#####################

if [ -d "$InpDir" ]; then
    if [ -e "$InpDir/${Project}.RasOrb" ]; then
        rm $InpDir/*.RasOrb*
    fi
    
    if [ -e "$InpDir/MO-track-list.txt" ]; then
        rm $InpDir/MO-track-list.txt
    fi
    
    if [ -e "$InpDir/${Project}.md.energies" ]; then
        rm $InpDir/${Project}.md.energies
    fi
else
    echo "Input directory '$InpDir' not found."
fi

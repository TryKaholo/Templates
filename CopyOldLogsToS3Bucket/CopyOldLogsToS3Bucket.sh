#!/bin/bash

#We extract the number of log files
n=$(ls $path | wc -l)
#If the number of files is greater than 7 the if is executed
if [ $n -gt 7 ];
then
	#We subtract the number of files we have from the maximum number of files we must have on the server
        j=$(($n - 7))
	#The for is executed the number of extra times that we got in the previous calculation
        for ((i=1; i<=$j; i++))
        do
		#With this command we find the oldest file and save it in a variable
                old=$(ls -lt $path | tail -1 | awk '{ print $9 }')
		#We call the variable and upload it to an s3 bucket
                aws s3 mv $path/$old s3://$bucket/
        done
fi

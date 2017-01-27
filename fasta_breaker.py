#!/usr/bin/env python

import os
import sys

fasta_in = sys.argv[1]
print fasta_in
fasta = open(fasta_in, 'r')
x = 1
y= 1
output = open(fasta_in +"_"+ str(y), "w")
for line in fasta:
	if line.startswith(">") and x<1000:
		output.write(line)
		x += 1
		y += 1
	elif x < 1000:
		output.write(line)
	elif line.startswith(">") and x == 1000:
		x = 1
		y +=1
		output.close()
		output = open(fasta_in+"_"+str(y),"w")
		output.write(line)

output.close()


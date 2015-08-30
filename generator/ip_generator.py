#!/usr/bin/python
import csv

with open('ips.txt', 'wb') as outf:
	fieldnames = ['uri']
	csvwriter = csv.DictWriter(outf, fieldnames)

	for i in range(0,255):
		for j in range(0,255):
			row = {}
			csvwriter.writerow(dict(row, uri="86.192."+str(i)+"."+str(j)))
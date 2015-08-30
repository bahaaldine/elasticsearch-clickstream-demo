#!/usr/bin/python
import csv
import random

with open('ip_mappings.csv', 'wb') as outf:
	fieldnames = ['ip'] + ['label']
	csvwriter = csv.DictWriter(outf, fieldnames)

	for i in range(0,255):
		for j in range(0,255):
			row = {}
			csvwriter.writerow(dict(row, ip="86.192."+str(i)+"."+str(j), label=random.randint(1,5)))
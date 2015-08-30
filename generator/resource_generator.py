#!/usr/bin/python
import csv

productCount = 200000

with open('resources.txt', 'wb') as outf:
	fieldnames = ['uri']
	csvwriter = csv.DictWriter(outf, fieldnames)

	while productCount > 0:
		row = {}
		csvwriter.writerow(dict(row, uri="/products/product%d" % productCount))
		productCount -= 1
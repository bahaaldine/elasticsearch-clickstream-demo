#!/usr/bin/python
import csv
import random

productCount = 200000
productCategories = ["Devices accessories","High-Tech accessories","IT accessories","pet","car","baby","home working","kitchen","video games","cycling","blu-ray and dvd","office supply","household applicance","High-tech","IT","Audio and musique","Gardening","Toys and games","Books","Software","Lighting","House","Music","Tires","Sport and leisure","Videos","Cosmetics","Jewellery","Shoes","Watches","Heatlh","Clothes"]

with open('mappings.csv', 'wb') as outf:
	fieldnames = ['uri'] + ['category']
	csvwriter = csv.DictWriter(outf, fieldnames)

	while productCount > 0:
		row = {}
		csvwriter.writerow(dict(row, uri="/products/product%d" % productCount, category=random.choice(productCategories)))
		productCount -= 1
import os
from datetime import datetime
import csv
import re
from functools import reduce
import operator
class param:
	def __init__(self, line, time):
		self.current=line[2]
		self.min=line[4]
		self.max=line[5]
		if self.min=="":
			self.minmax=""
		else:
			self.minmax="[{} {}]".format(self.min, self.max)
		self.time=time
	def __str__(self):
		return "current={},minmmax={},time={}".format(self.current, self.minmax, self.time)

def is_num(test):
	p=re.compile("[\d.]+(e-\d+|[nmu])?")
	if p.match(test):
		return True
	return False

def parse_names(names, single=True):
	if single:
		chunks=[names.split("\t")]
	else:
		chunks=[x.split('\t') for x in names[1:]]
	names_list=list()
	for item in chunks:
		if item[1] != "" and not is_num(item[1]):
			names_list.append(item[1])
		else:
			if item[0].find(":") != -1:
				partial=item[0].split(":")[2]
				if "." in partial:
					partial=partial.split(".")[1]
			else:
				partial=item[0]
			names_list.append(partial)
			#start=item[0].find(".")
			#end=item[0].find(":", start=start)
			#names_list.append(item[0][start+1:end])
	return names_list

def get_results():
	p=re.compile("^optimization_output_rev\d*\.txt")
	directory=os.listdir()
	files=[]
	for f in directory:
		if p.match(f):
			files.append(f)
	f=sorted(files,key=lambda x:int(re.findall("\d+",x)[0]))
	return f

fnames=get_results()
params=dict()
param_names=list()
dates=list()
for fname,i in zip(fnames,range(1,12)):
	#Read file
	with open(fname) as f:
		lines=f.readlines()
	# record the date of creation for the file
	ts=os.path.getctime(fname)
	time=datetime.utcfromtimestamp(ts).strftime('%m.%d.%Y')
	dates.append(time)

	# get the number of rows
	# some files are formatted as "var,alias,curr,nom,min,max"
	# some files are formatted aas "var,curr"
	chunk=lines[0].split("\t")
	if len(chunk)==2:
			flag_missing_vals=True
	else:
			flag_missing_vals=False
	
	# Get the names of all the parameters
	names=parse_names(lines, False)
	# if there's a known variable not in this file,
	# leave the spot blank
	for n in param_names:
		if n not in names:
			params[n].append(param(["","","","","",""],""))
	# if there's a variable that hasn't existed until this file,
	# save it, but also save the number of blanks before it
	for n in names:
		if n not in param_names:
			param_names.append(n)
			params[n]=[]
			for j in range(i-1):
				params[n].append(param(["","","","","",""],""))
	# process the lines
	for line in lines[1:]:
		
		chunk=line.rstrip('\n').split("\t")
		name=parse_names(line)[0]
		if flag_missing_vals==True:
			chunk=[name,"",chunk[1],"","","",""]
		params[name].append(param(chunk, time))
paramlist=[[x, params[x]] for x in params]
	
def print_vals(f,l):
	if not l:
		f.write("\n")
		return
	f.write(",{}".format(l[0].current))
	#print(l[0])
	print_vals(f, l[1:])
def print_minmax(f,l):
	if not l:
		f.write("\n")
		return
	f.write(",{}".format(l[0].minmax))
	print_minmax(f, l[1:])
def print_time(f,l):
	if not l:
		f.write("\n")
		return
	f.write(",{}".format(l[0]))
	print_time(f, l[1:])
def print_param(f, l):
	f.write("{}".format(l[0]))
	#print(l[0])
	print_vals(f,l[1])
	print_minmax(f, l[1])
def print_output(f,l):
	if not l:
		return
	print_param(f, l[0])
	print_output(f,l[1:])

f=open("optimization_outputs.csv","w")
print_time(f, dates)
print_output(f, paramlist)
f.write("\n")

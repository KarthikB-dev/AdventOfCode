import re
cmem=""
oval = 0
with open("input", "r+") as fin:
	for line in fin:
		cmem += line
muls=re.findall("mul\(\d+,\d+\)", cmem)
for mul in muls:
	# Multiply the values after the first parentheses
	# to the comma 
	lnum = re.findall("\d+,", mul)[0]
	lnum = lnum[:-1]
	lnum = int(lnum)
	# times what is after the comma to the second parentheses
	rnum = re.findall("\d+\)", mul)[0]
	rnum = rnum[:-1]
	rnum = int(rnum)
	# Add their product to oval
	oval += lnum * rnum	

print(f"Final output: {oval}")
	

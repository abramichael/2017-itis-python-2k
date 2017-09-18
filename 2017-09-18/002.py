import os

s = 0
for f in os.listdir("."):
	if f == __file__:
		continue

	if (f[0] in "aeiou"):
		fn = open(f)
		a = float(fn.read())
		s += a
print s
# Project Euler problem 1

# what is the sum of all the multiples of 3 or 5 under 1000?
# Thoughts: sum of 3s + sum of 5s - sums of 15s
# math way plug in formula vs. programming way
# do math way first: n(a1 +an)/2

#Calculating sum of 3s now
n1_3 = 3
nn_3 = 999
n_3 = 999 / 3
sn_3 = n_3 * (n1_3 + nn_3) / 2 

#Calculating sum of 5s now
n1_5 = 5
nn_5 = 995
n_5 = 995 / 5
sn_5 = n_5 * (n1_5 + nn_5) / 2

n1_15 = 15
nn_15 = 990
n_15 = 990 / 15
sn_15 = n_15 * (n1_15 + nn_15) / 2

#Calculating total sum now subtracting the double counted
answer = sn_5 + sn_3 - sn_15

print "The formula way says it is: %d" % answer

#starting the "dumb" way, the programming way
#concept is identify all the numbers in this list and add them up together
#for x in range 1 to 1000 inclusive, if remainder of x/3 or x/5 is 0, then add x to sum

answer2 = 0
for x in range(1,1000):
	if x % 3 == 0 or x % 5 == 0:
		answer2 += x

print "The programming answer is: %d" % answer2
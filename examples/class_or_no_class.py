#!/usr/bin/env python

# Example fasta file
#
# >seq1
# atgc
# >seq2
# tggcg
# >seq3
# cgcctta

# 1. Store the sequence information in a list of lists.
sequences = [["seq1", "atgc"], ["seq2", "tggcg"], ["seq3", "cgcctta"]]

##############################################

# 2. print names of sequences
for seq in sequences:
	print(seq[0])

# 3. print names and lengths of sequences
for seq in sequences:
	print(seq[0] + " " + str(len(seq[1])))

# 4. Calculate G+C content of sequences
for seq in sequences:
	gc = 0
	for base in seq[1]:
		if base == "g" or base == "c":
			gc += 1
	print(gc)

##############################################





# 1. Define a new object type called "Sequence".

class Sequence(object):
    def __init__(self, name, seq):
        self.name = name
        self.seq = seq

    def getName(self):
        return self.name

    def getLen(self):
        return str(len(self.seq))

    def getGC(self):
        gc = 0
        for base in self.seq:
            if base == "g" or base == "c":
                gc += 1
        return gc






# 3. Store the sequence data as a list of "Sequence" objects.

seq_objects = []

for seq in sequences:
	seq_objects.append(Sequence(seq[0], seq[1]))

#############################################

# 4. print names of sequences
for seq in seq_objects:
	print(seq.getName())

# 3. print names and lengths of sequences
for seq in seq_objects:
	print(seq.getName() + " " + seq.getLen())

# 4. Calculate G+C content of sequences
for seq in seq_objects:
	print(seq.getGC())

#############################################












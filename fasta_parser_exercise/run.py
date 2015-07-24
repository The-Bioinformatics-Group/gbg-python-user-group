#!/usr/bin/env python

"""
An exercise designed to practice writing classes in python.

This script will use the class that the user writes himself in an other file
and will test that it provides a certain functionality and behavior.

The class will be called FastaParser and will parse fasta type files.

Written by Lucas Sinclair.
Kopimi.
"""

# Step 1: Importing code from other files.
# Once the class exists in a file called "fasta_parser.py", it
# should be possible to import it and the following line should
# work:
from fasta_parser import FastaParser

# Step 2: One should be able to make new instances from this class
# In fact, one should be able to make as many new objects as one wants
# Here we will just make two in this example.
# The class initialization should take one argument: the path of the fasta
# file to parse. Two files are provided in this exercise.
contigs = FastaParser("all_contigs.fasta")
genes = FastaParser("predicted_genes.fasta")

# Step 3: What if we give a path, but there is no file there ?
# Then your class should complain ! It must throw an exception
# of type IOError. To check this we will use a function from
# the pytest module. It's like assert but for Exceptions.
# If you don't have pytest just install it.
import pytest
with pytest.raises(IOError): not_found = FastaParser('/file_does_not_exist.fasta')

# Step 4: What if we don't give a file path at all when making
# a new instance ? Then your class should complain also !
# It must throw an exception of type TypeError.
with pytest.raises(TypeError): missing = FastaParser()

# Step 5: OK we are ready to start reading data from the file.
# The first thing the class should do is report how many sequences
# there are in the fasta file
assert contigs.count == 5

# Step 6: We also want this to be reported as the length property
# itself of the object, so as to make something pythonic.
assert len(genes) == 8

# Step 7: Now we need to access the sequences in the file. Let's say
# we want to use a simple indexing syntax that is natural for python
# For instance asking for the second sequence would be as easy as genes[1]
assert genes[1] == "CGAGACTTATTCCTGAGATACTGTCCTTTCTCA"

# Step 8: What if we ask for a sequence number that is too high ?
# Then your class should complain !
# It must throw an exception of type IndexError.
with pytest.raises(IndexError): print contigs[93558]

# Step 9: What if the user doesn't ask for a certain sequence
# by using a number, but by using it's ID ? This should work too.
# Check that we complain when we should complain by raising the
# right exception.
assert contigs['contig_C'] == "GACTACCAGGGTATCTAATCCCGTTTGCTCCCTTGGCTTTCGTGC"
with pytest.raises(KeyError): print contigs['lorem_ipsum']

# Step 10: We can do all sorts of things with a fasta file.
# Maybe the user wants to get all sequences that are shorter
# than a given length. Write a method called 'extract_length'
# that takes only one argument: the length above which we will
# filter sequences. Return the new sequences in a list.
assert len(genes.extract_length(30)) == 3
assert contigs.extract_length(2) == []

# Step 11: Write a method "length_dist" that takes one argument:
# the path at which a PDF file containing a graph of the length
# distribution of the sequences should be created. Use any plotting
# library such as matplotlib or ggplot etc.
genes.length_dist("~/test/genes_lengths.pdf")

# Step 12: Write a method "align" that takes one argument:
# the path at which an aligned version of the fasta file
# will be created by calling the `muscle` executable or some other
# fast aligner.
contigs.align("~/test/alignement.fasta")

# Step 13: Write a method "subsample" that takes one argument:
# the number of sequences down to which the file should be
# rarefied. Check that that number is equal or lower than
# the number of sequences already in the file. Return the
# result as a list.
genes.subsample(3)

# Step 14: Document your code. Each method should have a docstring
# that would enable someone to quickly understand your code

# Step 15: Add style to your code. Google the term "PEP8" and make
# your code conform to it.
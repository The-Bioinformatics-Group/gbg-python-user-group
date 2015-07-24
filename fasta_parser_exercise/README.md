The goal of this exercise is to write a class that handles parsing fasta files in Python.

Obviously this functionality exists in Biopython. A requirement for this exercise is to never `import Bio`.

You should run the file called `run.py`. But that script will only run until the end if the file `fasta_parser.py` contains all the right code. The goal is to write the code that `fasta_parser.py` should contain in order for `run.py` to run until the end. At first `run.py` will raise an Exception on the first instruction because `fasta_parser.py` is empty.

Hint:
The first thing you should do to get started is to run this command on your bash prompt.

    $ echo "class FastaParser(object):" > fasta_parser.py
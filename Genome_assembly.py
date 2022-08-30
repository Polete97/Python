if __name__ == "__main__":
import Bio
print(Bio.__version__)
from Bio.Seq import Seq
my_seq = Seq("GATACATAGCTA")
print(my_seq)
print(my_seq.complement())
print(my_seq.reverse_complement())
print(my_seq.translate())
from Bio import SeqIO
#seq_file = SeqIO.parse("PATH_TO_YOUR_FILE", "fasta")

from Bio.Blast import NCBIWWW
results_handle = NCBIWWW.qblast("blastn", "nt", my_seq, format_type="text")

for line in results_handle:
    print(line)


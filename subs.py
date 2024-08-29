import argparse

parser = argparse.ArgumentParser()
parser.add_argument("dna_file", type=str, help="The path of the DNA string file to read.")
args = parser.parse_args()

lines = open(args.dna_file, "r").readlines()
dna = lines[0].strip() #s
motif = lines[1].strip() #t (substring)

position = []

for i in range(len(dna)):
    j = 0
    is_substring = False
    while j < len(motif) and i + len(motif) < len(dna):
        if dna[i + j] == motif[j]:
            is_substring = True
            j += 1
        else:
            is_substring = False
            break
    
    if is_substring:
        position.append(i + 1)

        
print(*position)



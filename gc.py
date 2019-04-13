#Calculates GC Content made by Mehmet Ali GUL

gene = open("BRCA1_BAP1.txt", "r")

#Set the values to 0
g = 0;
a = 0;
c = 0;
t = 0;

#Skip the first line of header
gene.readline()

for line in gene:
    line = line.lower()
    for char in line:
        if char == "g":
            g+=1
        if char == "a":
            a+=1
        if char == "c":
            c+=1
        if char == "t":
            t+=1

#Print the number of each nucleotide bases
print("number of guanine's: " + str(g))
print("number of adenine's: " + str(a))
print("number of cytosine's: " + str(c))
print("number of thymine's: " + str(t))

#0. = convert to floating point
gc = (g+c+0.) / (a+t+c+g+0.)

print("gc content: " + str(gc))

import os
print ("\x1b[6;30;42m:::: COPYPASTA TOOL  ::::\x1b[0m")
print ("\x1b[6;30;42m:::: By @Ridzwanirawan ::::\x1b[0m")
fin = open("wangy.txt", "rt")
fout = open("out.txt", "wt")
wangy = raw_input("Input Nama : ")
for line in fin:
	fout.write(line.replace('KEQING', wangy ))
fin.close()
fout.close()
print "Hasilnya\n\n"
print "\n\nATAU BUKA DI APLIKASI PENAMPIL TEKS"
os.system("xdg-open out.txt")

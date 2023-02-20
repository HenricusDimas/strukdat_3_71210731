import collections
kata = input("Masukkan kalimat yang akan di hitung : "  )
li=kata.split(' ')
ambil=collections.Counter(li).most_common()
wrd = set(kata.split(' '))

for i in ambil:
    print("%s\t: %d"%(i[0],i[1]))
  
word = kata.split()

print ("Jumlah Kata :" , len(word))
print ("Jumlah Kata Unik :" , len(wrd))



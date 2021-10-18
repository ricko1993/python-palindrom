# input kata
kata = input('Masukan Kata : ')

# operasi untuk membalikan kata yang diinput
membalik_kata = kata[::-1]

# operasi perbandingan
if kata == membalik_kata:
    print('palindrom')
else:
    print('bukan palindrom')

import os
from io import BytesIO
import pickle
try :
    os.mkdir('/home/wahyu/PycharmProjects/JPSS/Wahyu')
except :
    #open data
    openfile = open('/home/wahyu/PycharmProjects/JPSS/abstrak.txt','r')
    readfile = openfile.seek(80)
    readfile = openfile.read()
   # print(readfile)

    #membuat file txt baru
    createfile = open('/home/wahyu/PycharmProjects/JPSS/Wahyu/potongan_abstrak.txt','w')
    createfile.write(readfile)

    #enkripsi data
    readfile = BytesIO()
    writing = open('/home/wahyu/PycharmProjects/JPSS/Wahyu/potongan_abstrak.ser','wb')
    encrip = pickle.dump(readfile,writing)

    openfile.close()
    createfile.close()
    writing.close()
    #cek isi data enkripsi
    cek = open('/home/wahyu/PycharmProjects/JPSS/Wahyu/potongan_abstrak.ser','rb')
    lihat = pickle.load(cek)
    print(lihat)
    cek.close()

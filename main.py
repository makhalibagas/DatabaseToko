import barang,pembeli
print ('KELOMPOK 11 MEMBUAT DATABASE MENGGUNAKAN PYTHON')
print('1. Tambah Data Toko')
print('2. Ubah Data Toko ')
print('3. Hapus Data Toko')
print('4. Tampilkan semua data')
menu2=int(input('[Data]Pilih terserah : '))
if(menu2==1):
    print('1. Tabel Barang')
    print('2. Tabel Pembeli')
    menutabel = int(input('Pilih Tabe Apa?'))
    if(menutabel==1):
        print = ('ANDA MEMILIH TABEL BARANG')
        namabarang=input('Nama Barang : ')
        jumlahbarang=input('Jumlah Barang : ')
        barangterjual=input('Barang terjual : ')
        data=[namabarang,jumlahbarang,barangterjual]
        barang.add(data)
    elif(menutabel==2):
        print = ('ANDA MEMILIH TABEL PEMBELI')
        nama = input('Nama Pembeli : ')
        alamat = input ('Alamat Pembeli : ')
        pendidikan = input('Pendidikan Pembeli : ')
        data = [nama,alamat,pendidikan]
        pembeli.addPembeli(data)
    else:
        print('Menu tidak tersedia')
elif(menu2==2):
    print('1. Ubah Tabel Barang')
    print('2. Ubah Tabel Pembeli')
    menutabel = int(input('Pilih Tabe Apa? '))
    if(menutabel==1):
        print = ('ANDA MENGUBAH TABEL BARANG')
        idbarang_barang = input('id barang : ')
        namabarang=input('Nama Barang : ')
        jumlahbarang=input('Jumlah Barang : ')
        barangterjual=input('Barang terjual : ')
        data=[namabarang,jumlahbarang,barangterjual,idbarang_barang]
        barang.edit(data)
    elif(menutabel==2):
        print = ('ANDA MENGUBAH TABEL PEMBELI')
        id_pembeli = input('id Pembeli : ')
        nama = input('Nama Pembeli : ')
        alamat = input ('Alamat Pembeli : ')
        pendidikan = input('Pendidikan Pembeli : ')
        data = [nama,alamat,pendidikan,id_pembeli]
        pembeli.editPembeli(data)
    else:
        print('Menu tidak tersedia')
elif(menu2==3):
    print('1. Hapus Tabel Barang')
    print('2. Hapus Tabel Pembeli')
    menuhapus = int(input('Pilih Hapus yang mana?'))
    if(menuhapus==1):
        idbarang_barang=input('Id Barang : ')
        data=[idbarang_barang]
        barang.search(data)
        barang.delete(data)
    elif(menuhapus==2):
        id_pembeli=input('Id Pembeli : ')
        data = [id_pembeli]
        pembeli.searchPembeli(data)
        pembeli.deletePembeli(data)
elif(menu2==4):
    print('INI TABEL BARANG')
    barang.show()
    print('................................................................')
    print('INI TABEL PEMBELI')
    pembeli.showPembeli()
    print('................................................................')
else:
    print('Menu tidak tersedia')


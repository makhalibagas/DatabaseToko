import member
print ('KELOMPOK 11 MEMBUAT DATABASE MENGGUNAKAN PYTHON')
print('1. Tambah Member Perpus')
print('2. Ubah Member Perpus ')
print('3. Hapus Member Perpus')
print('4. Tampilkan Member Perpus')
menu2=int(input('[Member]Pilih terserah : '))
if(menu2==1):
    nama=input('Nama : ')
    alamat=input('Alamat : ')
    data=[nama,alamat]
    member.add(data)
elif(menu2==2):
    id_member=input('No.Member : ')
    nama=input('Nama : ')
    alamat=input('Alamat : ')
    data=[nama,alamat,id_member]
    member.edit(data)
elif(menu2==3):
    id_member=input('No.Member : ')
    data=[id_member]
    member.search(data)
    confirm=input('Yakin menghapus member ini?[Y/N]:')
    if(confirm=='Y'):
        member.delete(data)
    else:
        print('Tidak jadi menghapus data member!')
elif(menu2==4):
    member.show()
else:
    print('Menu tidak tersedia')



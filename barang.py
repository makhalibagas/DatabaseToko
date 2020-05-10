import mysql.connector
import connect
db=connect.koneksi()

#menambahkan data baru ke dalam tabel member
def add(data):
    cursor=db.cursor()
    sql="""INSERT INTO barang(namabarang,jumlahbarang,barangterjual)VALUES(%s,%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{} Data berhasil ditambahkan!'.format(cursor.rowcount))

#menampilkan seluruh data(record) dari tabel member
def show():
    cursor=db.cursor()
    sql="""SELECT*FROM barang"""
    cursor.execute(sql)
    results=cursor.fetchall()
    print("_________________________________________________________")
    print("|ID|NAMA BARANG|JUMLAH BARANG|BARANG TERJUAL|\tSISA BARANG")
    print("_________________________________________________________")
    for data in results:
        print("|",data[0],"|",data[1],"|\t",data[2],"|\t",data[3],"|\t",data[2]-data[3],"|")
        print("_________________________________________________________")

#mengubah data per record berdasarkan id pada tabel member
def edit(data):
    cursor=db.cursor()
    sql="""UPDATE barang SET namabarang=%s,jumlahbarang=%s,barangterjual=%s WHERE idbarang=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{} Data member berhasil diubah!'.format(cursor.rowcount))
#menghapus data(record) dari taabel member
def delete(data):
    cursor=db.cursor()
    sql="""DELETE FROM barang WHERE idbarang=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{} Data berhasil dihapus!'.format(cursor.rowcount))

#mencari data(record) dari tabel member
def search(idbarang_barang):
    cursor=db.cursor()
    sql="""SELECT*FROM barang WHERE idbarang=%s"""
    cursor.execute(sql,idbarang_barang)
    results=cursor.fetchall()
    print("_________________________________________________________")
    print("|ID|NAMA BARANG|\tJUMLAH BARANG\t|\tBARANG TERJUAL\t|\tSISA BARANG")
    print("_________________________________________________________")
    for data in results:
        print("|",data[0],"|",data[1],"|\t\t\t",data[2],"|\t\t\t",data[3],"|\t\t\t",data[2]-data[3],"|")
        print("_________________________________________________________")

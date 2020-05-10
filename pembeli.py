import mysql.connector
import connect
db=connect.koneksi()

#menambahkan data baru ke dalam tabel member
def addPembeli(data):
    cursor=db.cursor()
    sql="""INSERT INTO pembeli(nama,alamat,pendidikan)VALUES(%s,%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{} Data berhasil ditambahkan!'.format(cursor.rowcount))

#menampilkan seluruh data(record) dari tabel member
def showPembeli():
    cursor=db.cursor()
    sql="""SELECT*FROM pembeli"""
    cursor.execute(sql)
    results=cursor.fetchall()
    print("_________________________________________________________")
    print("|ID|NAMA|\tALAMAT\t|\tPENDIDIKAN|")
    print("_________________________________________________________")
    for data in results:
        print("|",data[0],"|",data[1],"|\t",data[2],"|\t",data[3],"|")
        print("_________________________________________________________")

#mengubah data per record berdasarkan id pada tabel member
def editPembeli(data):
    cursor=db.cursor()
    sql="""UPDATE pembeli SET nama=%s,alamat=%s,pendidikan=%s WHERE id=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{} Data member berhasil diubah!'.format(cursor.rowcount))

#menghapus data(record) dari taabel member
def deletePembeli(data):
    cursor=db.cursor()
    sql="""DELETE FROM pembeli WHERE id =%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{} Data berhasil dihapus!'.format(cursor.rowcount))

#mencari data(record) dari tabel member
def searchPembeli(id_pembeli):
    cursor=db.cursor()
    sql="""SELECT*FROM pembeli WHERE id=%s"""
    cursor.execute(sql,id_pembeli)
    results=cursor.fetchall()
    print("_________________________________________________________")
    print("|ID|NAMA|\tALAMAT\t|\tPENDIDIKAN|")
    print("_________________________________________________________")
    for data in results:
        print("|",data[0],"|",data[1],"|\t\t\t",data[2],"|\t\t\t",data[3],"|")
        print("_________________________________________________________")

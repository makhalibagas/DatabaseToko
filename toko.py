import mysql.connector
import connect
db=connect.koneksi()

#menambahkan data baru ke dalam tabel member
def add(datatoko):
    cursor=db.cursor()
    sql="""INSERT INTO member(nama,alamat)VALUES(%s,%s)"""
    cursor.execute(sql,datatoko)
    db.commit()
    print('{} Data toko berhasil ditambahkan!'.format(cursor.rowcount))

#menampilkan seluruh data(record) dari tabel member
def show():
    cursor=db.cursor()
    sql="""SELECT*FROM member"""
    cursor.execute(sql)
    results=cursor.fetchall()
    print("**********************************************************************************************")
    print("|ID|\t\t\tNAMA\t\t\t|\t\t\tALAMAT\t\t\t|\t\t\t")
    print("**********************************************************************************************")
    for data in results:
        print("",data[0],"|",data[1],"|",data[2],"|")
        print("*******************************************************************************************")

#mengubah data per record berdasarkan id pada tabel member
def edit(data):
    cursor=db.cursor()
    sql="""UPDATE member SET nama=%s,alamat=%s WHERE id=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{} Data member berhasil diubah!'.format(cursor.rowcount))

#menghapus data(record) dari taabel member
def delete(data):
    cursor=db.cursor()
    sql="""DELETE FROM member WHERE id=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{} Data member berhasil dihapus!'.format(cursor.rowcount))

#mencari data(record) dari tabel member
def search(id_member):
    cursor=db.cursor()
    sql="""SELECT*FROM member WHERE id=%s"""
    cursor.execute(sql,id_member)
    results=cursor.fetchall()
    print("*******************************************************************************************")
    print("|ID|\t\t\tNAMA\t\t\t|\t\t\tALAMAT\t\t\t|\t\t\t")
    print("*******************************************************************************************")
    for data in results:
        print("",data[0],"|",data[1],"|",data[2],"|")
        print("*******************************************************************************************")

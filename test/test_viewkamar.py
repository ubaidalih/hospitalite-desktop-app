import psycopg2 as pg
import os, sys
sys.path.append(os.path.join(sys.path[0], "../src/backend"))
from room import viewKamar

def viewKamar(infoKamar):
    conn = pg.connect(
        user = "vyojenvrexevcy",
        password = "78260dce308329a44a00d836c4cda566c328fdcb753a1c3996b5c1bb3d35ede2",
        host = "ec2-3-230-122-20.compute-1.amazonaws.com",
        port = "5432",
        database = "d1lsdor9ucq2mi"
    )
    com = conn.cursor()
    s1 = "SELECT DISTINCT k.id, kelas, harga FROM kamar k LEFT JOIN booking_kamar bk ON k.id = bk.id_kamar "
    s2 = "WHERE "
    s3 = "k.kelas = " + str(infoKamar[0])
    s4 = " AND "
    s5 = "(tanggal_kedatangan < '" + infoKamar[1] + "' OR " + "tanggal_kedatangan > '" + infoKamar[2] + "') AND "
    s6 = "(tanggal_pulang < '" + infoKamar[1] + "' OR " + "tanggal_pulang > '" + infoKamar[2] + "') AND "
    s7 = "(tanggal_kedatangan > '" + infoKamar[1] + "' OR tanggal_pulang < '" + infoKamar[2] + "')"
    s8 = " OR (waktu_booking IS NULL "
    s9 = "AND k.kelas = " + str(infoKamar[0])
    s10 = " )"
    
    if infoKamar[0] == "" and infoKamar[1] == "" and infoKamar[2] == "":
        com.execute(s1)
    elif infoKamar[0] == "":
        com.execute(s1 + s2 + s5 + s6 + s7 + s8 + s10)
    elif infoKamar[1] == "" and infoKamar[2] == "":
        com.execute(s1 + s2 + s3)
    else :
        com.execute(s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10)
    listKamar = com.fetchall()
    conn.close()
    return listKamar

def test_without_filter():
    infoKamar = ["", "", ""]
    listKamar = viewKamar(infoKamar)
    assert len(listKamar) == 49

def test_type_only():
    infoKamar = [1, "", ""]
    listKamar = viewKamar(infoKamar)
    assert len(listKamar) == 15

def test_date_only():
    infoKamar = ["", "2022-03-15", "2022-03-20"]
    listKamar = viewKamar(infoKamar)
    assert len(listKamar) == 45

def test_type_and_date():
    infoKamar = [1, "2022-03-15", "2022-03-20"]
    listKamar = viewKamar(infoKamar)
    assert len(listKamar) == 12

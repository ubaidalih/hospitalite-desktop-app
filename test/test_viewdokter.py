import psycopg2 as pg
import os, sys
sys.path.append(os.path.join(sys.path[0], "../src/backend"))
from appointment import viewDokter

def test_viewDokter_nofilter():
    conn = pg.connect(
        user = "vyojenvrexevcy",
        password = "78260dce308329a44a00d836c4cda566c328fdcb753a1c3996b5c1bb3d35ede2",
        host = "ec2-3-230-122-20.compute-1.amazonaws.com",
        port = "5432",
        database = "d1lsdor9ucq2mi"
    )
    com = conn.cursor()
    com.execute("SELECT id FROM dokter")
    amount = len(com.fetchall())
    conn.close()
    assert len(viewDokter(["", "", "", ""])) == amount

def test_viewDokter_nama():
    assert len(viewDokter(["Rebecca Knapp", "", "", ""])) == 1

def test_viewDokter_tanggal_waktu():
    conn = pg.connect(
        user = "vyojenvrexevcy",
        password = "78260dce308329a44a00d836c4cda566c328fdcb753a1c3996b5c1bb3d35ede2",
        host = "ec2-3-230-122-20.compute-1.amazonaws.com",
        port = "5432",
        database = "d1lsdor9ucq2mi"
    )
    com = conn.cursor()
    com.execute("SELECT DISTINCT id_dokter FROM booking_konsultasi WHERE tanggal_konsultasi = '2022-04-17' AND waktu_mulai = 16")
    amount = len(com.fetchall())
    com.execute("SELECT id FROM dokter")
    amount_doc = len(com.fetchall())
    conn.close()
    assert len(viewDokter(["", "", "2022-04-17", 16])) == (amount_doc - amount)

def test_viewDokter_nama_tanggal_waktu():
    conn = pg.connect(
        user = "vyojenvrexevcy",
        password = "78260dce308329a44a00d836c4cda566c328fdcb753a1c3996b5c1bb3d35ede2",
        host = "ec2-3-230-122-20.compute-1.amazonaws.com",
        port = "5432",
        database = "d1lsdor9ucq2mi"
    )
    com = conn.cursor()
    com.execute("SELECT DISTINCT id_dokter FROM booking_konsultasi WHERE tanggal_konsultasi = '2022-04-17' AND waktu_mulai = 16 AND id_dokter = 4")
    amount = len(com.fetchall())
    conn.close()
    assert len(viewDokter(["Rebecca Knapp", "", "2022-04-17", 16])) == amount
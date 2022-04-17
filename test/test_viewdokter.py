import psycopg2 as pg

def viewDokter(infoDokter):
    import psycopg2 as pg
    conn = pg.connect(
        user = "vyojenvrexevcy",
        password = "78260dce308329a44a00d836c4cda566c328fdcb753a1c3996b5c1bb3d35ede2",
        host = "ec2-3-230-122-20.compute-1.amazonaws.com",
        port = "5432",
        database = "d1lsdor9ucq2mi"
    )
    com = conn.cursor()
    s1 = "SELECT DISTINCT nama_lengkap FROM dokter d LEFT JOIN booking_konsultasi bk ON d.id = bk.id_dokter "
    s2 = "WHERE "
    s3 = "d.nama_lengkap LIKE '%" + str(infoDokter[0]) + "%' "
    s4 = " AND "
    s5 = "d.spesialisasi = '" + str(infoDokter[1]) +"' "
    s6 = " AND "
    
    # Murni cuma tanggal waktu
    s7 = "(bk.tanggal_konsultasi = '" + infoDokter[2] + "' AND " + "bk.waktu_mulai NOT IN ( SELECT waktu_mulai FROM booking_konsultasi WHERE tanggal_konsultasi = '" + infoDokter[2] + "' AND waktu_mulai = " + str(infoDokter[3])

    # Oh ada antara nama, spesial, ato mungkin 2 2 nya
    s8 = " AND id_dokter IN (SELECT id FROM dokter WHERE "
    s9 = " nama_lengkap LIKE '%" + str(infoDokter[0]) + "%' "
    s10 = " AND "
    s11 = " spesialisasi = '" + str(infoDokter[1]) + "' "

    # kurung klo misal ada nama / spesial
    s12 = " )"

    # kurung buat s7
    s13 = ") OR id_dokter NOT IN (SELECT id_dokter FROM booking_konsultasi WHERE tanggal_konsultasi = '" + infoDokter[2] + "')) "

    # sisaan
    s14 = " OR (tanggal_konsultasi IS NULL "
    s15 = ")"
    #janganlupa s8 - s11 lgi

    # Gaada filter
    if infoDokter[0] == "" and infoDokter[1] == "" and infoDokter[2] == "" and infoDokter[3] == "":
        com.execute(s1)
    # Ada nama doang
    elif infoDokter[1] == "" and infoDokter[2] == "" and infoDokter[3] == "":
        com.execute(s1+s2+s3+s14+s8+s9+s12+s15)
    # Ada spesialisasi doang
    elif infoDokter[0] == "" and infoDokter[2] == "" and infoDokter[3] == "":
        com.execute(s1+s2+s5+s14+s8+s11+s12+s15)
    # Ada tanggal doang
    elif infoDokter[0] == "" and infoDokter[1] == "":
        com.execute(s1+s2+s7+s13)
    # Ada nama dan tanggal
    elif infoDokter[1] == "":
        com.execute(s1+s2+s3+s6+s7+s8+s9+s12+s13+s14+s8+s9+s12+s15)
    # Ada spesialisasi dan tanggal
    elif infoDokter[0] == "":
        com.execute(s1+s2+s5+s6+s7+s8+s11+s12+s13+s14+s8+s11+s12+s15)
    # Ada nama dan spesialisasi
    elif infoDokter[2] == "" and infoDokter[3] == "":
        com.execute(s1+s2+s3+s4+s5+s14+s8+s9+s10+s11+s12+s15)
    # Ada semua
    else:
        com.execute(s1+s2+s3+s4+s5+s6+s7+s8+s9+s10+s11+s12+s13+s14+s8+s9+s10+s11+s12+s13+s15)

    listDokter = com.fetchall()
    conn.close()
    return [i[0] for i in listDokter]

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

# def test_viewDokter_tanggal_waktu():
#     conn = pg.connect(
#         user = "vyojenvrexevcy",
#         password = "78260dce308329a44a00d836c4cda566c328fdcb753a1c3996b5c1bb3d35ede2",
#         host = "ec2-3-230-122-20.compute-1.amazonaws.com",
#         port = "5432",
#         database = "d1lsdor9ucq2mi"
#     )
#     com = conn.cursor()
#     com.execute("SELECT DISTINCT id_dokter FROM booking_konsultasi WHERE tanggal_konsultasi = '2022-04-17' AND waktu_mulai = 16")
#     amount = len(com.fetchall())
#     com.execute("SELECT id FROM dokter")
#     amount_doc = len(com.fetchall())
#     conn.close()
#     assert len(viewDokter(["", "", "2020-04-17", 16])) == (amount_doc - amount)

# def test_viewDokter_nama_tanggal_waktu():
#     conn = pg.connect(
#         user = "vyojenvrexevcy",
#         password = "78260dce308329a44a00d836c4cda566c328fdcb753a1c3996b5c1bb3d35ede2",
#         host = "ec2-3-230-122-20.compute-1.amazonaws.com",
#         port = "5432",
#         database = "d1lsdor9ucq2mi"
#     )
#     com = conn.cursor()
#     com.execute("SELECT DISTINCT id_dokter FROM booking_konsultasi WHERE tanggal_konsultasi = '2022-04-17' AND waktu_mulai = 16 AND id_dokter IN (SELECT id FROM dokter WHERE nama_lengkap = 'Rebecca Knapp')")
#     amount = len(com.fetchall())
#     com.execute("SELECT id FROM dokter")
#     amount_doc = len(com.fetchall())
#     conn.close()
#     assert len(viewDokter(["Jonathan Williams", "", "2020-04-17", 16])) == (amount_doc -amount)
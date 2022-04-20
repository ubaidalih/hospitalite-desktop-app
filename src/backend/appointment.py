import psycopg2 as pg

def viewDokter(infoDokter):
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
    s5 = "d.spesialisasi LIKE '%" + str(infoDokter[1]) + "%' "
    s6 = " AND "
    s7 = " (id_dokter NOT IN (SELECT id_dokter FROM booking_konsultasi WHERE tanggal_konsultasi = '" + infoDokter[2] + "') OR (bk.tanggal_konsultasi = '" + infoDokter[2] +"' AND waktu_mulai != " + str(infoDokter[3]) + ")) "
    s8 = " UNION (SELECT DISTINCT nama_lengkap FROM dokter d LEFT JOIN booking_konsultasi bk ON d.id = bk.id_dokter WHERE tanggal_konsultasi IS NULL "
    s9 = " AND "
    # include s3,s5
    s10 = ")"

    # Gaada filter
    if infoDokter[0] == "" and infoDokter[1] == "" and infoDokter[2] == "" and infoDokter[3] == "":
        com.execute(s1)
    # Ada nama doang
    elif infoDokter[1] == "" and infoDokter[2] == "" and infoDokter[3] == "":
        com.execute(s1 + s2 + s3)
    # Ada spesialisasi doang
    elif infoDokter[0] == "" and infoDokter[2] == "" and infoDokter[3] == "":
        com.execute(s1 + s2 + s5)
    # Ada tanggal + waktu doang
    elif infoDokter[0] == "" and infoDokter[1] == "":
        com.execute(s1 + s2 + s7 + s8 + s10)
    # Ada nama dan tanggal + waktu
    elif infoDokter[1] == "":
        com.execute(s1 + s2 + s3 + s4 + s7 + s8 + s9 + s3 + s10)
    # Ada spesialisasi dan tanggal + waktu
    elif infoDokter[0] == "":
        com.execute(s1 + s2 + s5 + s6 + s7 + s8 + s9 + s5 + s10)
    # Ada nama dan spesialisasi
    elif infoDokter[2] == "" and infoDokter[3] == "":
        com.execute(s1 + s2 + s3 + s4 + s5)
    # Ada semua
    else:
        com.execute(s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s3 + s4 + s5 + s10)

    listDokter = com.fetchall()
    conn.close()
    print(len(listDokter))
    return [i[0] for i in listDokter]

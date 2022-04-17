"""function for register"""

import psycopg2 as pg

def register(registerInfo, isDokter):
    conn = pg.connect(
        user = "vyojenvrexevcy",
        password = "78260dce308329a44a00d836c4cda566c328fdcb753a1c3996b5c1bb3d35ede2",
        host = "ec2-3-230-122-20.compute-1.amazonaws.com",
        port = "5432",
        database = "d1lsdor9ucq2mi"
    )
    com = conn.cursor()

    if isDokter:
        com.execute("SELECT * FROM dokter")
        listAkun = com.fetchall()
    else:
        com.execute("SELECT * FROM pasien")
        listAkun = com.fetchall()

    for i in range(len(listAkun)):
        if registerInfo[1] == listAkun[i][2]:
            print("Email sudah ada")
            return False
        elif registerInfo[2] == listAkun[i][3]:
            print("Username sudah ada")
            return False

    idAkun = len(listAkun) + 1
    if isDokter:
        com.execute("INSERT INTO dokter VALUES ({}, '{}', '{}', '{}', '{}')".format(idAkun, registerInfo[0], registerInfo[1], registerInfo[2], registerInfo[3]))
    else:
        com.execute("INSERT INTO pasien VALUES ({}, '{}', '{}' ,'{}' ,'{}')".format(idAkun, registerInfo[0], registerInfo[1], registerInfo[2], registerInfo[3]))
    conn.commit()
    print("Data berhasil ditambahkan")
    return True

import psycopg2 as pg

def login(loginInfo, isDokter):
    conn = pg.connect(
        user = "vyojenvrexevcy",
        password = "78260dce308329a44a00d836c4cda566c328fdcb753a1c3996b5c1bb3d35ede2",
        host = "ec2-3-230-122-20.compute-1.amazonaws.com",
        port = "5432",
        database = "d1lsdor9ucq2mi"
    )

    com = conn.cursor()
    listAkun = []
    if isDokter :
        com.execute("SELECT * FROM dokter")
        listAkun = com.fetchall()
    else :
        com.execute("SELECT * FROM pasien")
        listAkun = com.fetchall()
    
    conn.close()
    for i in range (len(listAkun)):
        if loginInfo[0] == listAkun[i][3] and loginInfo[1] == listAkun[i][4]:
            return True
    
    return False

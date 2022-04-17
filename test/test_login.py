def login(loginInfo, isDokter, com):
    if isDokter :
        com.execute("SELECT * FROM dokter")
        listAkun = com.fetchall()
    else :
        com.execute("SELECT * FROM pasien")
        listAkun = com.fetchall()
    
    for i in range (len(listAkun)):
        if loginInfo[0] == listAkun[i][3] and loginInfo[1] == listAkun[i][4]:
            print("Login berhasil")
            return True
    
    print("Login gagal")
    return False

def foo(a,b):
    return a+b

def test_foo():
    assert foo(2,3) == 5

def test_boo():
    assert foo(3,3) == 1
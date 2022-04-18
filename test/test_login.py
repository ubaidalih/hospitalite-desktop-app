import psycopg2 as pg
import os, sys
sys.path.append(os.path.join(sys.path[0], "../src/backend"))
from login import login

def test_login():
    loginInfo = ["perrydouglas","P6$E!ysM(8"]
    isDokter = False
    assert login(loginInfo, isDokter) == True

def test_login_failed_pass():
    loginInfo = ["aprilspears","123456"]
    isDokter = True
    assert login(loginInfo, isDokter) == False

def test_login_failed_username():
    loginInfo = ["aprilspearss","7gOOSyHV#t"]
    isDokter = True
    assert login(loginInfo, isDokter) == False
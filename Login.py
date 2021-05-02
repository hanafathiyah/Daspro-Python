import data
from LoadData import load_data
from Hashing import hashing
from adding_function import banyak_data
from color import red,green

# load_data("folder_isi")

def is_login_valid(user_username,user_password,datas):
    i = 0
    available = False
    while i < banyak_data(datas) and available == False:
        if (datas[i][1] == user_username) and (datas[i][4] == user_password) and (datas[i][6] == hashing(user_password)):
              available = True
        else:
            i += 1
    return available
    
def login():
    datas = data.user
    user_username = input("Masukkan username: ")
    user_password = input("Masukkan password: ")

     # Mengulang sampai username dan password benar
    while (is_login_valid(user_username,user_password,datas) == False):
        print("\nMasukan username/password", red("salah"))
        user_username = input("\nMasukkan username: ")
        user_password = input("Masukkan password: ")
    
    for array in datas:
        if (array[1] == user_username):
            data.user_login = array
            break

    print("\nHalo", green(user_username)+"! Selamat datang di Kantong Ajaib.")

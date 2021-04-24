import data
from LoadData import load_data
from adding_function import banyak_data

load_data("folder_isi")

def is_username_valid(user_username,datas):
    i = 0
    available = False
    while i < banyak_data(datas) and available == False:
        if (datas[i][1] == user_username):
            available = True
        else:
            i += 1
    return available

def is_password_valid(user_password,datas):
    i = 0
    available = False
    while i < banyak_data(datas) and available == False:
        if (datas[i][4] == user_password):
            available = True
        else:
            i += 1
    return available
    
def login():
    datas = data.user
    print(">> login")
    user_username = input("Masukkan username: ")
    user_password = input("Masukkan password: ")

     # Mengulang sampai username dan password benar
    while (is_username_valid(user_username,datas) == False) or (is_password_valid(user_password,datas) == False):
        print("\nMasukan username/password salah")
        user_username = input("\nMasukkan username: ")
        user_password = input("Masukkan password: ")

    print("\nHalo", user_username, "! Selamat datang di Kantong Ajaib.")

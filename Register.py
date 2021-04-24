import data
from LoadData import load_data
from adding_function import banyak_data

load_data("folder_isi")

def register():
    new_user = []
    datas = []
    datas = data.user

    print(">> register")
    new_user_idx = datas[-1][0] + 1
    new_user_name = input("Masukkan nama: ")
    upper_new_user_name = new_user_name.title()

    # Ngecek apakah username sudah unik sebelum melanjutkan regis
    unique = False
    while unique == False :
        new_user_username = input("Masukkan username: ") 
        ketemu = False
        i = 0
        while ketemu == False and i < banyak_data(datas):
            if datas[i][1] == new_user_username:
                ketemu = True
                print("\nUsername telah digunakan") 
                print("Silahkan masukkan username lain.\n")
            else:
                ketemu = False
                i += 1
        if ketemu == True and i >= banyak_data(datas):
            unique = False
        elif ketemu == False and i >= banyak_data(datas):
            unique = True

    new_user_addres = input("Masukkan alamat: ")
    new_user_password = input("Masukkan password: ")
    new_user_role = "User"
    new_user = [new_user_idx, new_user_username, upper_new_user_name, new_user_addres, new_user_password, new_user_role]

    print("\nUser", new_user_username, "telah berhasil register ke dalam Kantong Ajaib.")

    data.user.append(new_user)

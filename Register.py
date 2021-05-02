import data
from Hashing import hashing
from adding_function import banyak_data
from adding_function import isAdmin
from desain import register_header
from color import red,green

def register():
    register_header()
    if not isAdmin(): # Jika role bukan admin
        print("Fungsi ini hanya dapat diakses oleh", red("Admin."))
    else: # Jika role adalah admin
        new_user = []
        datas = []
        datas = data.user

        new_user_idx = datas[-1][0] + 1
        new_user_name = input("Masukkan nama: ")
        upper_new_user_name = new_user_name.title()

        # Ngecek apakah username sudah unik sebelum melanjutkan regis
        is_unique = False
        while not(is_unique) :
            new_user_username = input("Masukkan username: ") 
            is_ketemu = False
            for array in (datas):
                if array[1] == new_user_username:
                    is_ketemu = True
                    print("\nUsername",red("telah digunakan")) 
                    print("Silahkan masukkan username lain.\n")
                    break
            if not(is_ketemu):
                is_unique = True

        new_user_addres = input("Masukkan alamat: ")
        new_user_password = input("Masukkan password: ")
        new_user_role = "user"
        new_user_hashing = hashing(new_user_password)
        new_user = [new_user_idx, new_user_username, upper_new_user_name, new_user_addres, new_user_password, new_user_role, new_user_hashing]

        print("\nUser", new_user_username, "telah", green("berhasil"), "register ke dalam Kantong Ajaib.")

        data.user.append(new_user)

import data

from adding_function import banyak_data
from adding_function import find_user_name_id
from adding_function import find_consumable_name_id
from adding_function import isAdmin
from adding_function import sortTanggal
from LoadData import load_data

# load_data("folder_isi")

# prosedur melihat riwayat pengambilan consumable
def riwayatambil():
    if not isAdmin(): # validasi akses : akses tidak diizinkan
        print("Fungsi ini hanya dapat diakses oleh Admin.")
    else: # validasi akses : akses diizinkan
        datas = data.consumable_history
        f = "riwayatambil"
        datas_sort = sortTanggal(datas,f) # data yang telah terurut descending berdasarkan tahun disimpan dalam array datas_sort
        i = 0
        while (i < banyak_data(datas_sort)): # perulangan untuk mencetak data ke layar
            print("ID Pengambilan\t\t:", datas_sort[i][0])
            print("Nama Pengambil\t\t:", find_user_name_id(datas_sort[i][1])) # translasi id user menjadi nama user
            print("Nama Consumable\t\t:", find_consumable_name_id(datas_sort[i][2])) # translasi id consumable menjadi nama consumable
            print("Tanggal Pengambilan\t:", datas_sort[i][3])
            print("Jumlah\t\t\t:", datas_sort[i][4])
            print("")
            if ((i + 1) % 5 == 0): # apabila pengguna ingin mengeluarkan entry tambahan
                tambahan = input("Next >> Y/N: ")
                if tambahan == "N": # pengguna tidak ingin mengeluarkan entry tambahan
                    break
                else: # pengguna ingin mengeluarkan entry tambahan
                    print("")
            i += 1
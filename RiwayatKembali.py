import data

from adding_function import banyak_data
from adding_function import find_user_name_id
from adding_function import find_gadget_name_id
from adding_function import isAdmin
from adding_function import sortTanggal
from LoadData import load_data

# load_data("folder_isi")

# prosedur melihat riwayat pengembalian gadget
def riwayatkembali():
    if not isAdmin(): # validasi akses : akses tidak diizinkan
        print("Fungsi ini hanya dapat diakses oleh Admin.")
    else: # validasi akses : akses diizinkan
        datas = data.gadget_return_history
        f = "riwayatkembali"
        datas_sort = sortTanggal(datas,f) # data yang telah terurut descending berdasarkan tahun disimpan dalam array datas_sort
        i = 0
        while (i < len(datas_sort)): # perulangan untuk mencetak data ke layar
            print("ID Pengembalian\t\t:", datas_sort[i][0])
            print("Nama Pengambil\t\t:", find_user_name_id(data.gadget_borrow_history[datas_sort[i][1]-1][1]))
            print("Nama Gadget\t\t:", find_gadget_name_id(data.gadget_borrow_history[datas_sort[i][1]-1][2]))
            print("Tanggal Pengembalian\t:", datas_sort[i][2])
            print("Jumlah Pengembalian\t:", datas_sort[i][3])
            print("")
            if ((i + 1) % 5 == 0): # apabila pengguna ingin mengeluarkan entry tambahan
                tambahan = input("Next >> Y/N: ")
                if tambahan == "N": # pengguna tidak ingin mengeluarkan entry tambahan
                    break
                else: # pengguna ingin mengeluarkan entry tambahan
                    print("")
            i += 1

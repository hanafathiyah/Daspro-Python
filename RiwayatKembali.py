import data
from adding_function import sortTanggal
from adding_function import find_user_name_id
from adding_function import find_gadget_name_id
from LoadData import load_data
load_data("folder_isi")

# procedure melihat riwayat pengembalian gadget
def riwayatkembali():
    datas = data.gadget_return_history
    f = "riwayatkembali"
    datas_sort = sortTanggal(datas,f) # data yang telah terurut descending berdasarkan tahun disimpan dalam array datas_sort
    i = 0
    while (i < len(datas_sort)): # perulangan untuk mencetak data ke layar
        print("ID Pengembalian\t\t:", datas_sort[i][0])
        print("Nama Pengambil\t\t:", find_user_name_id(datas_sort[i][1]))
        print("Tanggal Pengembalian\t:", datas_sort[i][2])
        print("")
        if ((i + 1) % 5 == 0): # apabila pengguna ingin mengeluarkan entry tambahan
            tambahan = input("Next >> Y/N: ")
            if tambahan == "N": # pengguna tidak ingin mengeluarkan entry tambahan
                break
            else: # pengguna ingin mengeluarkan entry tambahan
                print("")
        i += 1

riwayatkembali()

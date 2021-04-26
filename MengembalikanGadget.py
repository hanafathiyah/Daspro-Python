import data
from LoadData import load_data
from adding_function import banyak_data
from adding_function import find_gadget_name_id


# Command buat pengen test
# from Login import login
# load_data('folder_isi')

def mengembalikan_gadget() :
    role_user = data.user_login[5]

    # Validasi role user 
    if (role_user != 'user') :
        return print("Fungsi ini hanya dapat diakses oleh user")

    
    datas = data.gadget_borrow_history
    id_username = data.user_login[0]

    # Inisialisasi 
    i = 0 
    a = 0
    gadget_dipinjam = []
    id_gadget_dipinjam = []
    jumlah_dipinjam = []
    while i < banyak_data(datas) :
                if (datas[i][1] == id_username) and (datas[i][5] == 'False') :
                    a += 1

                    # Pengambilan keterangan gadget yang dipinjam (id & Jumlah)
                    id_gadget = datas[i][2]
                    Jumlah_Gadget_dipinjam = datas[i][4]

                    # Apabila seorang user meminjam gadget yang sama dalam 2 waktu yang berbeda
                    if id_gadget in id_gadget_dipinjam : 
                        jumlah_dipinjam[id_gadget_dipinjam.index(id_gadget)] += datas[i][4]
                    else :
                        # Pembuatan Array ID gadget yang dipinjam
                        id_gadget_dipinjam.append(id_gadget)

                        # Pembuatan Array ID transaksi, dibuat untuk memudahkan proses pengembalian
                        # ID transaksi dipakai karena bersifat unik
                        gadget_dipinjam.append((datas[i][0]))


                        Jumlah_Gadget_dipinjam = datas[i][4] 
                        jumlah_dipinjam.append(Jumlah_Gadget_dipinjam)

                        print(f'{a}. {find_gadget_name_id(id_gadget)}')
                    i += 1
                    
                else:
                    i += 1
    if len(gadget_dipinjam) == 0 : 
        print('Tidak ada gadget yang dipinjam')
    else : 
        no_peminjaman = int(input('Masukkan nomor peminjaman : '))
        if no_peminjaman > len(gadget_dipinjam) :
            print('Nomor peminjaman tidak valid')
        else :
            tanggal = input("Tanggal pengembalian : ")
            i = 0 
            while i < banyak_data(datas) :
                        if gadget_dipinjam[no_peminjaman - 1] == datas[i][0] : # Pencarian gadget yang akan dikembalikan menggunakan ID transaksi
                            id_gadget = id_gadget_dipinjam[no_peminjaman - 1] # Mencari ID gadget yang akan dikembalikan dari array ID gadget yang dipinjam

                            print(f'Anda tercatat telah meminjam {jumlah_dipinjam[no_peminjaman - 1]} gadget {find_gadget_name_id(datas[i][2])}')
                            Jumlah_pengembalian = int(input('Jumlah pengembalian : '))

                            # Validasi jumlah yang akan dikembalikan
                            if Jumlah_pengembalian > jumlah_dipinjam[no_peminjaman - 1] :
                                print("Jumlah pengembalian harus lebih kecil dari yang dipinjam!")
                            elif Jumlah_pengembalian <=0 : 
                                print('Jumlah pengembalian harus lebih besar dari 0!')

                            else : 
                                Total_pengembalian = Jumlah_pengembalian # Untuk di array pengembalian
                                # Proses pengembalian gadget
                                j = 0
                                while j < banyak_data(datas) :
                                    if (datas[j][1] == id_username) and (datas[j][5] == 'False') and (datas[j][2] == id_gadget) :
                                        id_transaksi = datas[j][0]
                                        if Jumlah_pengembalian >= datas [j][4] : 
                                            Jumlah_pengembalian -= datas[j][4]
                                            datas[j][4] = 0 
                                            datas[j][5] = 'True'
                                        else :
                                            datas[j][4] -= Jumlah_pengembalian
                                            Jumlah_pengembalian = 0
                                        j += 1
                                    else :
                                        j += 1
                                    

                                # Pembuatan id pengembalian otomatis
                                id_pengembalian = 1
                                data_pengembalian = data.gadget_return_history
                                i = 0
                                available = False
                                while i < banyak_data(data_pengembalian) and available == False:
                                    if (datas[i][0] != id_pengembalian) and available == True :
                                        available = True
                                    else:
                                        i += 1
                                        id_pengembalian += 1

                                # Penambahan pada array
                                new_pengembalian = [id_pengembalian,id_transaksi,tanggal, Total_pengembalian]
                                data.gadget_return_history.append(new_pengembalian)
                                print(f'Item {find_gadget_name_id(id_gadget)} (x{Total_pengembalian}) berhasil dikembalikan!')

                            break
                        else : 
                            i += 1
    
# login()
# mengembalikan_gadget()

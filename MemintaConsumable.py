import data
from adding_function import isUser

def minta_consume():
    role_user = data.user_login[5]
    
    # validasi role user
    if (not isUser()):
        return print("Fungsi ini hanya dapat diakses oleh User")


    minta_id = input("Masukan ID item: ")

    # validasi id input
    isfound_id = False
    for i in range(len(data.consumable)):
        if data.consumable[i][0] == minta_id:
            isfound_id = True
            idx_id = i
    
    if not(isfound_id) :
        return print("Gagal meminta consumable karena ID tidak valid.")


    minta_jumlah = int(input("Jumlah: "))

    # validasi jumlah input
    isvalid_jumlah = False
    if data.consumable[idx_id][3] >= minta_jumlah:
        isvalid_jumlah = True 

    if not(isvalid_jumlah) :
        return print("Item %s tidak berhasil diminta. Jumlah permintaan terlalu banyak!" % data.consumable[idx_id][1])
    elif minta_jumlah <= 0 :
        return print("Item %s tidak berhasil dipinjam. Jumlah permintaan harus lebih besar dari 0" % data.consumable[idx_id][1])


    minta_tanggal = input("Tanggal permintaan: ")


    data.consumable[idx_id][3] -= minta_jumlah
    print("Item %s (x%i) telah berhasil diminta!" % (data.consumable[idx_id][1], minta_jumlah))

    # proses menambahkan ke dalam file eksternal consumable_history
    id_add                  = len(data.consumable_history) + 1
    id_pengambil_add        = data.user_login[0]
    id_consumable_add       = data.consumable[idx_id][0]
    tanggal_pengambilan_add = minta_tanggal
    jumlah_add              = minta_jumlah

    consumable_history_add = [id_add, id_pengambil_add, id_consumable_add, tanggal_pengambilan_add, jumlah_add]
    data.consumable_history.append(consumable_history_add)
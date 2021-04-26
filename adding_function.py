import data
from LoadData import load_data
load_data("folder_isi")

def is_id_available(id,datas): # mengecek ketersediaan id dalam database
    i = 0 # inisialisasi
    available = False # inisialisasi
    while i < banyak_data(datas) and available == False:
        if (datas[i][0] == id): # id tersedia
            available = True
        else: 
            i += 1
    return available

def is_id_valid(id): # validasi id
    valid = False # inisialisasi
    if (id[0] == "G" or id[0] == "C"): # id valid
        if id[1:].isnumeric() and int(id[1:]) > 0:
            valid = True
    return valid

def find_raw(id, datas): # mencari letak id (dalam baris)
    i = 0 # inisialisasi
    found = False # inisialisasi
    while i < banyak_data(datas) and found == False: 
        if (datas[i][0] == id): # id berhasil ditemukan
            found = True
        else:
            i += 1
    return i

def is_rarity_valid(rarity): # validasi rarity
    valid = False # inisialisasi
    if (rarity == "C" or rarity == "B" or rarity == "A" or rarity == "S"): # rarity valid
        valid = True
    return valid

def is_tahun_valid(tahun): # validasi tahun
    if tahun.isnumeric(): # tahun merupakan angka
        if int(tahun) <= 0: # tahun tidak valid
            return False
        else: # tahun valid
            return True
    else: # tahun bukan merupakan angka
        return False

def is_jumlah_valid(jumlah): # validasi jumlah
    if jumlah.isnumeric(): # jumlah merupakan angka
        if int(jumlah) <= 0: # jumlah tidak valid
            return False
        else: # jumlah valid
            return True
    else: # jumlah bukan merupakan angka
        return False

def find_user_name_id(id): # mencari nama user berdasarkan id
    i = 0 # inisialisasi
    datas = data.user
    found = False # inisialisasi
    while i < banyak_data(datas) and found == False: 
        if (datas[i][0] == id): # id berhasil ditemukan
            found = True
        else:
            i += 1
    return datas[i][2]

def find_gadget_name_id(id): # mencari nama gadget berdasarkan id
    i = 0 # inisialisasi
    datas = data.gadget
    found = False # inisialisasi
    while i < banyak_data(datas) and found == False: 
        if (datas[i][0] == id): # id berhasil ditemukan
            found = True
        else:
            i += 1
    return datas[i][1]

def find_consumable_name_id(id): # mencari nama consumable berdasarkan id
    i = 0 # inisialisasi
    datas = data.consumable
    found = False # inisialisasi
    while i < banyak_data(datas) and found == False: 
        if (datas[i][0] == id): # id berhasil ditemukan
            found = True
        else:
            i += 1
    return datas[i][1]

def isGadgetOrConsumable(id): # mengecek apakah item tersebut gadget atau consumable
    if (id[0] == "G"): # item adalah gadget
        return "gadget"
    else: # item adalah consumable
        return "consumable"

def banyak_data(datas): # menghitung banyak data
    cnt = 0 # inisialisasi
    for data in datas:
        cnt += 1
    return(cnt) # banyak data

def sortTanggal(arr,f): # mengurutkan data descending berdasarkan tanggal menggunakan selection sort

    datas = []

    def convert_date_to_days(date): # mengubah tanggal jadi jumlah hari (dihitung dari 0 Masehi)
        intDD = 0
        if int(date[0]) == 0:
            intDD += int(date[1:2])
        else:
            intDD += int(date[0:2])

        intMM = 0
        if int(date[3]) == 0:
            intMM += int(date[4:5])
        else:
            intMM += int(date[3:5])
        intYY = int(date[6:10])

        return ((intYY-1)*365+(intMM-1)*30+intDD)

    def get_max(arr, index_start, f): 
        if (f == "riwayatambil" or f == "riwayatpinjam"):
            maks = convert_date_to_days(arr[index_start][3])
        # mendapatkan maksimum array dari indeks indeks_start sampai selesai
            for i in range(index_start+1, len(arr)):
                if convert_date_to_days(arr[i][3]) > maks:
                    maks = convert_date_to_days(arr[i][3])  
            return maks 
        else:
            maks = convert_date_to_days(arr[index_start][2])
        # mendapatkan maksimum array dari indeks indeks_start sampai selesai
            for i in range(index_start+1, len(arr)):
                if convert_date_to_days(arr[i][2]) > maks:
                    maks = convert_date_to_days(arr[i][2])  
            return maks      

    def get_idx(arr, number, f):
    # mendapatkan index dari suatu angka dalam array
        i = 0
        found = False
        while(found == False and i < len(arr)):
            if (f == "riwayatambil" or f == "riwayatpinjam"):
                if convert_date_to_days(arr[i][3]) == number:
                    found = True
                else:
                    i += 1
            else:
                if convert_date_to_days(arr[i][2]) == number:
                    found = True
                else:
                    i += 1                
        return i

    def swap(array, indeks_1, indeks_2):
    # swap elemen array indeks 1 dengan indeks 2
        tmp = array[indeks_2]
        array[indeks_2] = array[indeks_1]
        array[indeks_1] = tmp

    for i in range(len(arr)):
        maxArr = get_max(arr, i, f)
        maxIdx = get_idx(arr, maxArr, f)
        swap(arr, i, maxIdx)
        datas.append(arr[i])

    return datas

def isAdmin(): # memvalidasi apakah role dari pengguna merupakan admin atau bukan
    admin = False # inisialisasi
    if(data.user_login[5] == "Admin"): # pengguna adalah admin
        admin = True
    return admin 

def isUser(): # memvalidasi apakah role dari pengguna merupakan user atau bukan
    user = False # inisialiasi
    if(data.user_login[5] == "User"): # pengguna adalah user
        user = True
    return user
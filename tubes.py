def open_gadget_csv():

    f = open("Gadget.csv","r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n","") for raw_line in raw_lines]

    def convert_array_data_to_real_values(array_data):
        arr_cpy = array_data[:]
        for i in range(6):
            if ( i == 3 or i == 5 ):
                arr_cpy[i] = int(arr_cpy[i])   
        return arr_cpy

    def convert_line_to_data(line):
        raw_array_of_data = line.split(";")
        array_of_data = [data.strip() for data in raw_array_of_data]
        return array_of_data

    raw_header = lines.pop(0)
    header = convert_line_to_data(raw_header)

    datas = []

    for line in lines:
        array_of_data = convert_line_to_data(line)
        real_values = convert_array_data_to_real_values(array_of_data)
        datas.append(real_values)

    return datas

gadget_csv_origin = open_gadget_csv()
gadget_csv_modified = open_gadget_csv()

def open_consumable_csv():

    f = open("Consumable.csv","r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n","") for raw_line in raw_lines]

    def convert_array_data_to_real_values(array_data):
        arr_cpy = array_data[:]
        for i in range(5):
            if ( i == 3 ):
                int(arr_cpy[i])
        return arr_cpy

    def convert_line_to_data(line):
        raw_array_of_data = line.split(";")
        array_of_data = [data.strip() for data in raw_array_of_data]
        return array_of_data

    raw_header = lines.pop(0)
    header = convert_line_to_data(raw_header)

    datas = []

    for line in lines:
        array_of_data = convert_line_to_data(line)
        real_values = convert_array_data_to_real_values(array_of_data)
        datas.append(real_values)

    return datas

consumable_csv_origin = open_consumable_csv()
consumable_csv_modified = open_consumable_csv()  

def is_id_available(id,datas):
    i = 0
    available = False
    while i < banyak_data(datas) and available == False:
        if (datas[i][0] == id):
            available = True
        else:
            i += 1
    return available

def is_id_valid(id):
    valid = False
    if (id[0] == "G" or id[0] == "C"):
        valid = True
    return valid

def find_raw(id, datas):
    i = 0
    found = False
    while i < banyak_data(datas) and found == False:
        if (datas[i][0] == id):
            found = True
        else:
            i += 1
    return i

def is_rarity_valid(rarity):
    valid = False
    if (rarity == "C" or rarity == "B" or rarity == "A" or rarity == "S"):
        valid = True
    return valid
    
def isGadgetOrConsumable(id):
    if (id[0] == "G"):
        return "gadget"
    else:
        return "consumable"

def banyak_data(datas):
    cnt = 0
    for data in datas:
        cnt += 1
    return(cnt)

def convert_datas_to_string(id,datas):
    if (isGadgetOrConsumable(id) == "gadget"):
        header = ["id","nama","deskripsi","jumlah","rarity","tahun_ditemukan"]
    else:
        header = ["id","nama","deskripsi","jumlah","rarity"]

    string_data = ";".join(header) + "\n"
    for arr_data in datas:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    return string_data

def tambah_item():
    new_item = []
    datas = []
    id = input("Masukan ID: ")
    if (not is_id_valid(id)):
        print("Gagal menambahkan item karena ID tidak valid.")
    else: 
        if (isGadgetOrConsumable(id) == "gadget"):
            datas = gadget_csv_modified
        else:
            datas = consumable_csv_modified
        if(is_id_available(id, datas) == True):
            print("Gagal menambahkan item karena ID sudah ada.")
        else:
            nama = input("Masukan Nama: ")
            deskripsi = input("Masukan Deskripsi: ")
            jumlah = int(input("Masukan Jumlah: "))
            rarity = input("Masukan Rarity: ")
            if (not is_rarity_valid(rarity)):
                print("Input rarity tidak valid!")
            else:
                if (isGadgetOrConsumable(id) == "gadget"):
                    tahun_ditemukan = int(input("Masukan tahun ditemukan: "))
                    new_item = [id,nama,deskripsi,jumlah,rarity,tahun_ditemukan]
                else:
                    new_item = [id,nama,deskripsi,jumlah,rarity]
                print("Item telah berhasil ditambahkan ke database.")
                if (isGadgetOrConsumable(id) == "gadget"):
                    gadget_csv_modified.append(new_item)
                else:
                    consumable_csv_modified.append(new_item)

def pinjam():
    datas = gadget_csv_modified
    id = input("Masukan ID: ")
    if (not is_id_valid(id)):
        print("Gagal meminjam item karena ID tidak valid.")
    else: 
        if(not is_id_available(id, datas)):
            print("Gagal meminjam item karena ID tidak ada.")
        else:
            tgl = input("Tanggal peminjaman: ")
            jumlah = int(input("Jumlah peminjaman: "))
            if jumlah > datas[find_raw(id, datas)][3]:
                print(f"Item {datas[find_raw(id, datas)][1]} tidak berhasil dipinjam. Jumlah tidak cukup!")
            else:
                print(f"Item {datas[find_raw(id, datas)][1]} (x{jumlah}) berhasil dipinjam!")
                gadget_csv_modified[find_raw(id, datas)][3] -= jumlah
                
exit = False

while exit == False:
    perintah = input()
    if (perintah == "tambahitem"):
        tambah_item()
    elif(perintah == "pinjam"):
        pinjam()
    elif(perintah == "exit"):
        print(gadget_csv_modified)
        exit = True
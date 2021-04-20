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

def open_consumable_csv():

    f = open("Consumable.csv","r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n","") for raw_line in raw_lines]

    def convert_array_data_to_real_values(array_data):
        arr_cpy = array_data[:]
        for i in range(5):
            if ( i == 3 ):
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

gadget_csv_modified = open_gadget_csv()
consumable_csv_modified = open_consumable_csv()

def is_id_valid(id):
    valid = False
    if (id[0] == "G" or id[0] == "C"):
        valid = True
    return valid

def is_id_available(id,datas):
    i = 0
    available = False
    while i < banyak_data(datas) and available == False:
        if (datas[i][0] == id):
            available = True
        else:
            i += 1
    return available

def banyak_data(datas):
    cnt = 0
    for data in datas:
        cnt += 1
    return(cnt)

def find_raw(id, datas):
    i = 0
    found = False
    while i < banyak_data(datas) and found == False:
        if (datas[i][0] == id):
            found = True
        else:
            i += 1
    return i

def isGadgetOrConsumable(id):
    if (id[0] == "G"):
        return "gadget"
    else:
        return "consumable"

def mengubah_jumlah_item() :
    id = input("Masukan ID: ")
    if (isGadgetOrConsumable(id) == "gadget"):
        datas = gadget_csv_modified
    else:
        datas = consumable_csv_modified
    while (not is_id_valid(id)) or (not is_id_available(id, datas)) :
        if (not is_id_valid(id)):
            print("Gagal menambah item karena ID tidak valid.")
            id = input("Masukan ID: ")
        else: 
            if(not is_id_available(id, datas)):
                print("Gagal menambah item karena ID tidak ada.")
                id = input("Masukan ID: ")
    jumlah_diganti = int(input("Masukkan jumlah : "))
    if jumlah_diganti < 0 :
        while (jumlah_diganti * -1) > datas[find_raw(id, datas)][3]:
            jumlah_diganti = jumlah_diganti * -1
            print(f"{jumlah_diganti} {datas[find_raw(id, datas)][1]} tidak berhasil dibuang. Stok sekarang : {datas[find_raw(id, datas)][3]} (<{jumlah_diganti})")
            jumlah_diganti = int(input("Masukkan jumlah : "))
    if (isGadgetOrConsumable(id) == "gadget"):
        gadget_csv_modified[find_raw(id, datas)][3] += jumlah_diganti
    else:
        consumable_csv_modified[find_raw(id, datas)][3] += jumlah_diganti


mengubah_jumlah_item()

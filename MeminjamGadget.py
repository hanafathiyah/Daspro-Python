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

gadget_csv_modified = open_gadget_csv()

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

def pinjam():
    datas = gadget_csv_modified
    id = input("Masukan ID: ")
    while (not is_id_valid(id)) or (not is_id_available(id, datas)) :
        if (not is_id_valid(id)):
            print("Gagal meminjam item karena ID tidak valid.")
            id = input("Masukan ID: ")
        else: 
            if(not is_id_available(id, datas)):
                print("Gagal meminjam item karena ID tidak ada.")
                id = input("Masukan ID: ")
        
    tgl = input("Tanggal peminjaman: ")
    jumlah = int(input("Jumlah peminjaman: "))
    
    while jumlah > datas[find_raw(id, datas)][3]:
        print(f"Item {datas[find_raw(id, datas)][1]} tidak berhasil dipinjam. Jumlah peminjaman terlalu banyak!")
        jumlah = int(input("Jumlah peminjaman: "))
    while jumlah <= 0 : 
        print(f"Item {datas[find_raw(id, datas)][1]} tidak berhasil dipinjam. Jumlah peminjaman harus lebih besar dari 0")
        jumlah = int(input("Jumlah peminjaman: "))
    print(f"Item {datas[find_raw(id, datas)][1]} (x{jumlah}) berhasil dipinjam!")
    gadget_csv_modified[find_raw(id, datas)][3] -= jumlah

pinjam()
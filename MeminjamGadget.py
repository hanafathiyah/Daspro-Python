f = open("Gadget.csv","r")
raw_line = f.readlines()
f.close()
lines = [raw_line.replace("\n", "") for raw_line in raw_line]

def array_menjadi_nilai_real(array_data) :
    arr_cpy = array_data[:]
    for i in range (6) :
        if (i == 3) :
            arr_cpy[i] = int(arr_cpy[i])
        elif (i == 6 ) : 
            arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

def baris_menjadi_data(line) : 
    raw_lines_list = []
    kata = ''
    for ch in line :
        if ch == ';':
            raw_lines_list.append(kata)
            kata = ''
        else :
            kata += ch
    lines_list = [data.strip() for data in raw_lines_list]
    return lines_list

raw_header = lines.pop(0)
header = baris_menjadi_data(raw_header)

datas = []
for line in lines :
    lines_list = baris_menjadi_data(line)
    nilai_asli = array_menjadi_nilai_real(lines_list)
    datas.append(nilai_asli)

IDValid = False
while IDValid == False :    
    ID = input("Masukkan ID item : ")
    ketemu =  False
    a = 0
    while ketemu == False and a < 7 : # Jumlah gadget di fix 8
        if ID == datas[a][0] :
            Barang = datas[a][1]
            Jumlah = datas[a][3]
            ketemu = True
        else : 
            a += 1 
            ketemu = False
    if a >= 7 : 
        print("Gadget tidak ditemukan")
        IDValid = False
    else : 
        IDValid = True


TGL = input("Tanggal peminjaman : ")


NValid = False
while NValid == False : 
    N = int(input("Jumlah Peminjaman : "))
    if N > Jumlah : 
        print("Jumlah tidak valid!")
        NValid = False
    else : 
        NValid = True

print("Gadget " + Barang + " (x" + str(N) + ") " + "telah berhasil dipinjam!")


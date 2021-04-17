def convert_csv_to_data(file_csv):
    # mengubah dari csv menjadi list berisi data per baris
    raw_lines = file_csv.readlines()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]

    # mengubah dari list data per baris menjadi matriks 
    raw_data_csv = convert_lines_to_raw_data(lines)

    # mengubah tipe variable dari tiap sel pada matriks sesuai dengan tipe data seharusnya
    data_csv = convert_raw_data_to_data(raw_data_csv)

    return(data_csv)

def convert_lines_to_raw_data(lines):
    raw_data = []
    for line in lines:
        raw_line_list = []
        kata = ''
        for char in line:
            if char == ';':
                raw_line_list.append(kata)
                kata = ''
            else:
                kata += char
        
        # menghapus spasi awal dan akhir tiap sel menggunakan fungsi .strip()
        line_list = [word.strip() for word in raw_line_list]
        raw_data.append(line_list)
    
    return(raw_data)

def convert_raw_data_to_data(raw_data):
    data_cpy = raw_data
    for i in range(len(raw_data)):          # i sebagai baris
        for j in range(len(raw_data[i])):   # j sebagai kolom
            if is_number(data_cpy[i][j]):
                data_cpy[i][j] = int(data_cpy[i][j])    
    return(data_cpy)

def is_number(s): # menghasilkan true apabila string berupa angka
    try:
        float(s)
        return True
    except ValueError:
        return False    

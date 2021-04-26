import data

def load_data(directory):
    file_csv_user                   = open("%s/user.csv" % directory, 'r')
    file_csv_gadget                 = open("%s/gadget.csv" % directory, 'r')
    file_csv_gadget_borrow_history  = open("%s/gadget_borrow_history.csv" % directory, 'r')
    file_csv_gadget_return_history  = open("%s/gadget_return_history.csv" % directory, 'r')
    file_csv_consumable             = open("%s/consumable.csv" % directory, 'r')
    file_csv_consumable_history     = open("%s/consumable_history.csv" % directory, 'r')

    data.user                   = convert_csv_to_data(file_csv_user)
    data.gadget                 = convert_csv_to_data(file_csv_gadget)
    data.gadget_borrow_history  = convert_csv_to_data(file_csv_gadget_borrow_history)
    data.gadget_return_history  = convert_csv_to_data(file_csv_gadget_return_history)
    data.consumable             = convert_csv_to_data(file_csv_consumable)
    data.consumable_history     = convert_csv_to_data(file_csv_consumable_history)

    file_csv_user.close()
    file_csv_gadget.close()
    file_csv_gadget_borrow_history.close()
    file_csv_gadget_return_history.close()
    file_csv_consumable.close()
    file_csv_consumable_history.close()

    data.header_user                   = data.user.pop(0)
    data.header_gadget                 = data.gadget.pop(0)          
    data.header_gadget_borrow_history  = data.gadget_borrow_history.pop(0)
    data.header_gadget_return_history  = data.gadget_return_history.pop(0)
    data.header_consumable             = data.consumable.pop(0)
    data.header_consumable_history     = data.consumable_history.pop(0)

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
            if char == ',':
                raw_line_list.append(kata)
                kata = ''
            else:
                kata += char
        
        raw_line_list.append(kata)
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

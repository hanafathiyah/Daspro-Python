import os
import time
import data

def save_data():
    folder_penyimpanan = input("Masukkan nama folder penyimpanan: ")
    
    if not(os.path.exists(folder_penyimpanan)):
        os.makedirs(folder_penyimpanan)
    
    string_user                   = convert_data_to_string(data.user, data.header_user)
    string_gadget                 = convert_data_to_string(data.gadget, data.header_gadget)
    string_gadget_borrow_history  = convert_data_to_string(data.gadget_borrow_history, data.header_gadget_borrow_history)
    string_gadget_return_history  = convert_data_to_string(data.gadget_return_history, data.header_gadget_return_history)
    string_consumable             = convert_data_to_string(data.consumable, data.header_consumable)
    string_consumable_history     = convert_data_to_string(data.consumable_history, data.header_consumable_history)

    file_csv_user                   = open("%s/user.csv" % folder_penyimpanan, 'w')
    file_csv_gadget                 = open("%s/gadget.csv" % folder_penyimpanan, 'w')
    file_csv_gadget_borrow_history  = open("%s/gadget_borrow_history.csv" % folder_penyimpanan, 'w')
    file_csv_gadget_return_history  = open("%s/gadget_return_history.csv" % folder_penyimpanan, 'w')
    file_csv_consumable             = open("%s/consumable.csv" % folder_penyimpanan, 'w')
    file_csv_consumable_history     = open("%s/consumable_history.csv" % folder_penyimpanan, 'w')
    
    file_csv_user.write(string_user)
    file_csv_gadget.write(string_gadget)
    file_csv_gadget_borrow_history.write(string_gadget_borrow_history)
    file_csv_gadget_return_history.write(string_gadget_return_history)
    file_csv_consumable.write(string_consumable)
    file_csv_consumable_history.write(string_consumable_history)

    file_csv_user.close()
    file_csv_gadget.close()
    file_csv_gadget_borrow_history.close()
    file_csv_gadget_return_history.close()
    file_csv_consumable.close()
    file_csv_consumable_history.close()

    print("\nLoading . . .")
    time.sleep(2)
    
    print("\nData berhasil disimpan ke dalam folder %s" % folder_penyimpanan)

def convert_data_to_string(file_data, file_header):
    string_data = ", ".join(file_header)
    string_data += "\n"
    for arr_data in file_data:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ", ".join(arr_data_all_string)
        string_data += "\n"
    return string_data
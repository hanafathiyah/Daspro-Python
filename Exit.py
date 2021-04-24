from SaveData import save_data

def exit():
    exit_input = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    if exit_input == 'y' or exit_input == 'Y' :
       print("\n")
       save_data()

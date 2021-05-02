from SaveData import save_data
from desain import exit_header
from thankyou import thankyou
import os

def exit():
    exit_header()
    exit_input = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    if exit_input == 'y' or exit_input == 'Y' :
       print("\n")
       save_data()
    os.system("cls")   
    thankyou()
    quit()

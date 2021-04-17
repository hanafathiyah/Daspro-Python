import argparse
import os

from ConvertCSVToData import convert_csv_to_data
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

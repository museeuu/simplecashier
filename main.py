from module import *

custName = input('Masukan nama Anda: ')
custID = input("Masukkan ID Anda: ")

trx = Customer(custName, custID)
trx.welcome()
trx.input_item()
trx.change_item()
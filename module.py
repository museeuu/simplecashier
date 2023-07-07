import os

class Customer:
    '''
    Merupakan sebuah class untuk menjalankan programnya
    '''
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.transID = name + '-' + id
        self.transaction = Transaction()

    def welcome(self):
        '''
        Method yang berisi ucapan selamat datang kepada pengguna baru
        '''
        print(f'Selamat Datang di Tokoku {self.transID.title()}!')
        os.system("pause")
        os.system("cls")
        print("Selamat Berbelanja!")

    def input_item(self):
        '''
        Merupakan sebuah method yang akan melakukkan penambahan item/barang secara berulang
        '''
        while True:
            item = input("Masukkan nama barang: ").title()
            try:
                quantity = int(input('Masukan jumlah barang yang ingin dibeli: '))
                price = int(input('Masukan harga barang: '))
                self.transaction.add_item(item, quantity, price)
                print("Item berhasil Ditambahkan!")
                os.system("pause")
                self.transaction.check_order()
                while True:
                    ans = input('Apakah kamu ingin menambah order? (ya/tidak) ')
                    if ans.lower() == 'tidak':
                        break
                    elif ans.lower()== 'ya':
                        break
                    else:
                        print('Silahkan untuk memasukkan jawaban "ya/tidak"')
                if ans.lower() == 'tidak':
                    break
            except ValueError:
                print(f'Jumlah barang dan/atau harga barang harus berupa angka')

    def change_item(self):
        '''
        Merupakan sebuah method yang berfungsi menampilkan 7 buah inputan pilihan menu
        '''
        while True:
            print('\nApakah ada yang ingin Anda ubah?\n')
            print('  0. Melanjutkan ke pembayaran.')
            print('  1. Ubah nama barang.')
            print('  2. Ubah jumlah barang.')
            print('  3. Ubah harga.')
            print('  4. Hapus barang, jumlah & harga sekaligus.')
            print('  5. Tambah barang belanjaan.')
            print('  6. Batalkan transaksi.\n')

            try:
                answer = int(input('Silahkan masukan angka yang sesuai dengan pilihan: '))
                if answer == 6:
                    self.transaction.reset()
                    break
                elif answer == 1:
                    while True:
                        old_name1 = input('Masukan nama barang yang ingin diubah: ').title()
                        if old_name1 in self.transaction.Cart:
                            new_name1 = input('Masukan nama barang yang baru: ').title()
                            self.transaction.update_name(old_name1, new_name1)
                            os.system("pause")

                            self.transaction.check_order()
                            break
                        else:
                            print("Item yang anda masukkan tidak ada di keranjang belanja.")
                elif answer == 2:
                    while True:
                        old_name1 = input('Masukan nama barang yang ingin diubah: ').title()
                        if old_name1 in self.transaction.Cart:
                            new_quantity1 = int(input('Masukan jumlah barang: '))
                            self.transaction.update_quantity(old_name1, new_quantity1)
                            os.system("pause")
                            self.transaction.check_order()
                            break
                        else:
                            print("Item yang anda masukkan tidak ada di keranjang belanja.")
                elif answer == 3:
                    while True:
                        old_name1 = input('Masukan nama barang yang ingin diubah: ').title()
                        if old_name1 in self.transaction.Cart:
                            new_price1 = int(input('Masukan harga barang: '))
                            self.transaction.update_price(old_name1, new_price1)
                            os.system("pause")
                            self.transaction.check_order()
                            break
                        else:
                            print("Item yang anda masukkan tidak ada di keranjang belanja.")
                elif answer == 4:
                    while True:
                        old_name1 = input('Masukan nama barang yang ingin dihapus: ').title()
                        if old_name1 in self.transaction.Cart:
                            self.transaction.delete_item(old_name1)
                            os.system("pause")
                            self.transaction.check_order()
                            break
                        else:
                            print("Item yang anda masukkan tidak ada di keranjang belanja.")
                elif answer == 5:
                    self.input_item()
                else:
                    os.system("cls")
                    payment = f'Anda perlu melakukkan pembayaran sejumlah Rp {int(self.transaction.Total-self.transaction.Diskon):,}.'
                    print(payment)
                    try:
                        while True:
                            pay = int(input("Kamu akan membayar berapa: "))
                            if pay >= (self.transaction.Total-self.transaction.Diskon):
                                change = pay - (self.transaction.Total-self.transaction.Diskon)
                                cashout = f'Kembalian anda: Rp {int(change):,}.'
                                print(cashout)
                                break
                            else:
                                print("Uang mu kurang!")
                    except ValueError:
                        print("Pembayaran harus dalam Rupiah. Silahkan coba kembali!")
                    print('Terima kasih sudah berbelanja di Tokoku!')
                    break

            except ValueError:
                print('Apa yang Anda masukkan tidak ada di pilihan.')

class Transaction:
    '''
    Merupakan sebuah class yang berisi kerangka program
    '''
    Cart = {}
    Total = 0
    Diskon = 0

    def add_item(self, item_name, item_quantity, item_price):
        '''
        Merupakan method yang berfungsi untuk menambahkan item
        '''
        self.item_name = item_name
        self.item_quantity = item_quantity
        self.item_price = item_price
        self.Cart.update({item_name: [item_quantity, item_price]})

    def update_name(self, old_name, new_name):
        '''
        Merupakan method yang berfungsi untuk mengubah nama item
        '''
        self.Cart[new_name] = self.Cart.pop(old_name)
        print(f'Item {old_name} berhasil diubah menjadi {new_name}.')
    
    def update_quantity(self, item_name, new_quantity):
        '''
        Merupakan method yang berfungsi untuk mengubah jumlah item
        '''
        self.Cart[item_name][0] = new_quantity
        print(f'Jumlah Item {item_name} berhasil diubah menjadi {new_quantity}.')

    def update_price(self, item_name, new_price):
        '''
        Merupakan method yang berfungsi untuk mengubah harga item
        '''
        self.Cart[item_name][1] = new_price
        print(f'Harga Item {item_name} berhasil diubah menjadi Rp. {new_price}.')

    def delete_item(self, item_name):
        '''
        Merupakan method yang berfungsi untuk menghapus item
        '''
        self.Cart.pop(item_name)
        print(f'Item {item_name} berhasil dihapus.')

    def reset(self):
        '''
        Merupakan method yang berfungsi untuk mengulangi dari awal
        '''
        self.Cart = {}
        self.Total = 0
        print(f'Order berhasil dibatalkan.')

    def check_order(self):
        '''
        Merupakan method yang berfungsi untuk melakukkan pengecekan terhadap item
        '''
        os.system("cls")
        if not self.Cart:
            print('Keranjang Anda kosong.')
            return

        print('Keranjang belanja Anda:')
        self.Total = 0
        print("Nama Barang \t    Jumlah Barang \tHarga \t\tTotal")
        for index, (item_name, item_info) in enumerate(self.Cart.items()):
            quantity = item_info[0]
            price = item_info[1]
            subtotal = quantity * price
            self.Total += subtotal
            print(f'{item_name}\t\t    {quantity} \t\t\t {price:,}', f'\t\tRp. {subtotal:,}\n')
            

        '''
        Mendapatkan Diskon ketika berbelanja dengan nomilai tertentu
        '''
        if self.Total > 500000:
            diskon = self.Total * 0.1
            self.Diskon += diskon
        elif self.Total > 300000:
            diskon = self.Total * 0.08
            self.Diskon += diskon
        elif self.Total > 200000:
            diskon = self.Total * 0.05
            self.Diskon += diskon
        else:
            diskon = 0

        print("-" * 30)
        print('\nSubtotal', f'Rp {self.Total:,}')
        print('Diskon', f'Rp {int(diskon):,}')
        print('Total', f'Rp {int(self.Total - diskon):,}')   
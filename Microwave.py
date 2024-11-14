import time
import os
import csv

class comp: #Kelas comp ini menjadi parent class untuk kelas-kelas yang lain
    def __init__(self, time:int, temp:int, moisture:int): #Kelas ini memiliki tiga atribut atau nilai, yaitu time (waktu), temperature (suhu), dan moisture (kelembaban) yang disimpan dalam variabel self
        self.time = time*60 #waktu diubah menjadi satuan detik dari inputnya menit
        self.temp = temp #nilai temperature dari self diambil dari nilai temp
        self.moisture = moisture #nilai moisture dari self diambil dari nilai moisture

    #Pada program microwave ini nilai kelembaban berkurang seiring dengan berjalannya pemasakan makanan
    def moisture1(self, limit): #Fungsi ini digunakan untuk mengurangi nilai kelembaban
        if self.moisture >= limit: #Mulai dari sini sampai bawah merupakan fungsi untuk mengurangi persentase kelembaban kondisi di dalam microwave
            time = self.time
            while time > 0: #Selama waktu memasak masih tersisa, kelembaban akan terus berkurang sebesar temperatur/1200 sampai nilai kelembabannya di bawah batas minimum kelembaban microwave (limit)
                self.moisture = self.moisture - (self.temp/1200)
                if self.moisture <= limit:
                    break
                time -= 1     

class mode(comp): #Kelas ini merupakan anakan dari kelas comp yang digunakan untuk melakukan 3 mode pemasakan cepat (tanpa pengaturan manual), yaitu quick heat, defrost, dan gril
    def __init__(self, time, temp, moisture): #Seperti kelas comp, kelas mode ini juga memiliki nilai waktu, temperatur, dan kelembaban yang disimpan dalam variabel self
        super().__init__(time, temp, moisture)
    def quick_heat(self): #Fungsi untuk menggunakan mode quick heat
        comp.moisture1(self, 40) #Mode ini  memiliki batas (limit) kelembaban sebesar 40 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def Deforst(self): #Fungsi untuk menggunakan mode defrost
        comp.moisture1(self, 60) #Mode ini  memiliki batas (limit) kelembaban sebesar 60 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def Grill(self): #Fungsi untuk menggunakan mode grill
        comp.moisture1(self, 30) #Mode ini  memiliki batas (limit) kelembaban sebesar 30 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
class vegetable(comp): #Kelas ini merupakan anakan dari kelas comp yang digunakan untuk melakukan pemasakan sayuran
    def __init__(self, time, temp, moisture): #Seperti kelas comp, kelas vegetable ini juga memiliki nilai waktu, temperatur, dan kelembaban yang disimpan dalam variabel self
        super().__init__(time, temp, moisture)
    def menu(): #Fungsi ini adalah fungsi untuk menampilkan menu sayuran yang tersedia
        Microwave.display1() #Seiring dengan penampilan menu sayuran, microwave juga menampilkan interfacenya (akan dijelaskan lebih lanjut fdi bawah)
        print(" 1. brokoli")
        print(" 2. wortel\n 3. kembang kol\n 4. bayam")
        print(" 5. jagung manis\n 6. paprika")
        print(" 7. zucchini")
    def brokoli(self): #Fungsi ini adalah fungsi untuk memasak brokoli
        comp.moisture1(self, 70) #Pemasakan brokoli  memiliki batas (limit) kelembaban sebesar 70 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def wortel(self): #Fungsi ini adalah fungsi untuk memasak wortel
        comp.moisture1(self, 60) #Pemasakan wortel  memiliki batas (limit) kelembaban sebesar 60 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def kembang_kol(self): #Fungsi ini adalah fungsi untuk memasak kembang kol
        comp.moisture1(self, 70) #Pemasakan kembang kol  memiliki batas (limit) kelembaban sebesar 70 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def bayam(self): #Fungsi ini adalah fungsi untuk memasak bayam
        comp.moisture1(self, 80) #Pemasakan bayam  memiliki batas (limit) kelembaban sebesar 80 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def jagung_manis(self): #Fungsi ini adalah fungsi untuk memasak jagung manis
        comp.moisture1(self, 70) #Pemasakan jagung manis  memiliki batas (limit) kelembaban sebesar 70 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def paprika(self): #Fungsi ini adalah fungsi untuk memasak paprika
        comp.moisture1(self, 60) #Pemasakan paprika  memiliki batas (limit) kelembaban sebesar 60 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def zucchini(self): #Fungsi ini adalah fungsi untuk memasak zuncchini
        comp.moisture1(self, 70) #Pemasakan zucchini  memiliki batas (limit) kelembaban sebesar 70 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
class seafood(comp): #Kelas ini merupakan anakan dari kelas comp yang digunakan untuk melakukan pemasakan seafood
    def __init__(self, time, temp, moisture): #Seperti kelas comp, kelas seafood ini juga memiliki nilai waktu, temperatur, dan kelembaban yang disimpan dalam variabel self
        super().__init__(time, temp, moisture)
    def menu(): #Fungsi ini adalah fungsi untuk menampilkan menu sayuran yang tersedia
        Microwave.display1() #Seiring dengan penampilan menu seafood, microwave menampilkan interfacenya
        print(" 1. Ikan fillet")
        print(" 2. Udang")
        print(" 3. Cumi-cumi")
        print(" 4. Kerang")
        print(" 5. Lobster")
    def fish(self): #Fungsi ini adalah fungsi untuk memasak ikan fillet
        comp.moisture1(self, 70) #Pemasakan ikan fillet  memiliki batas (limit) kelembaban sebesar 70 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def shrimp(self): #Fungsi ini adalah fungsi untuk memasak udang
        comp.moisture1(self, 75) #Pemasakan udang  memiliki batas (limit) kelembaban sebesar 75 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def squid(self): #Fungsi ini adalah fungsi untuk memasak cumi-cumi
        comp.moisture1(self, 70) #Pemasakan cumi-cumi  memiliki batas (limit) kelembaban sebesar 70 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def shellfish(self): #Fungsi ini adalah fungsi untuk memasak kerang
        comp.moisture1(self, 70) #Pemasakan kerang  memiliki batas (limit) kelembaban sebesar 70 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def lobster(self): #Fungsi ini adalah fungsi untuk memasak lobster
        comp.moisture1(self, 70) #Pemasakan lobster  memiliki batas (limit) kelembaban sebesar 70 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
class incode(comp): #Kelas ini merupakan anakan dari kelas comp yang digunakan untuk membaca kode barcode paket makanan yang tersedia
    def __init__(self, time:int, temp:int, moisture:int, barcode:int, namefood):
        super().__init__(time, temp, moisture) #Kelas ini memiliki nilai time, temp, dan moisture seperti comp, namun juga memiliki nilai barcode dan namefood yang eksklusif bagi kelas ini saja
        self.barcode = barcode
        namefood = namefood        
    def detect(self, code): #Fungsi ini adalah fungsi untuk mendeteksi kode barkode dari file barcodes.csv yang tersedia
        csvfile = open('barcodes.csv', newline='')
        foodcode = csv.reader(csvfile)
        next(foodcode)
        barcode = []
        namefood = []
        timefood = []
        tempfood = []
        moisturefood = []
        #Pertama-tama seluruh paket makanan yanng tersedia di file barcodes.csv dilist dan dimasukkan ke dalam array
        for row in foodcode:
            barcode.append(int(row[1]))
            namefood.append(row[2])
            timefood.append(int(row[3])*60)
            tempfood.append(int(row[4]))
            moisturefood.append(int(row[5]))
        csvfile.close()
        for i in range(len(barcode)):
            #Kemudian di sini, masukan dicek kesesuaiannya dengan barcode nomor ke berapa
            if code == barcode[i]:
                #Jika sudah ditemukan, maka barcode nomor tersebutlah yang kemudian akan dimasak
                self.namefood = namefood[i]
                self.barcode = barcode[i]
                self.time = timefood[i]
                self.temp = tempfood[i]
                self.moisture = moisturefood[i]
                break               
    def cook(self): #Fungsi ini adalah fungsi untuk memasak makanan yang telah terpilih sesuai barcode
        comp.moisture1(self, 0) #Pemasakan paket makanan yang telah dipilih memiliki batas kelembaban sebesar 0 %
        Microwave.display2(self)
         
class Microwave(comp): #Kelas ini merupakan anakan kelas comp yang digunakan untuk melakukan display interface dan pemasakan pada microwave, serta untuk memulai penggunaan microwave
    def __init__(self, time, temp, moisture): #Seperti kelas comp, kelas seafood ini juga memiliki nilai waktu, temperatur, dan kelembaban yang disimpan dalam variabel self
        super().__init__(time, temp, moisture)
    def displayup(): #Fungsi ini merupakan fungsi untuk menampilakn display bagian atas microwave
        print('='*38)
        print('||',end='')
        print('='*18,end='')
        print('||',end='')
        print('='*14,end='')
        print('||')
    def displaydown(): #Fungsi ini merupakan fungsi untuk menampilakn display bagian bawah microwave
        print('||',end='')
        print('='*18,end='')
        print('||',end='')
        print('='*14,end='')
        print('||')
        print('='*38)
    def display1(): #Fungsi ini adalah fungsi untuk menampilkan interface / menu utama dari microwave
        Microwave.displayup()
        side_v = 6
        while side_v>0:
            side_h = 38
            while side_h>0:
                if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                    print('|', end='')
                elif (side_h == 1):
                    print('|')
                elif side_h<37 and side_h>18:
                    print(' ',end='')
                elif side_h == 16:
                    if side_v == 6:
                        print(f'Temp || --- ||',end='')
                    elif side_v == 5:
                        print(f'Time ||--:--||',end='')
                    elif side_v == 4:
                        print(f'Mois || --- ||',end='')
                    elif side_v == 3:
                        print(" _ _ _ _ _ ___",end='')
                    elif side_v == 2:
                        print("|1|3|4|5|6|   ",end='')
                    else:
                        print("|7|8|0| 99|___",end='')
                    #Display ini menunjukkan fungsi-fungsi atau fitur-fitur yang dapat dipilih oleh user untuk digunakan
                side_h-=1
            side_v-=1
        Microwave.displaydown()

        #Tamplian menu utama microwave akan terlihat seperti ini
        # ======================================
        # ||==================||==============||
        # ||                  ||Temp || --- ||||
        # ||                  ||Time ||--:--||||
        # ||                  ||Mois || --- ||||
        # ||                  || _ _ _ _ _ ___||
        # ||                  |||1|3|4|5|6|   ||
        # ||                  |||7|8|0| 99|___||
        # ||==================||==============||
        # ======================================
        # ======================================
        # ||1. Manual mode  ||6. Seafood      ||
        # ||==================================||
        # ||2. Quick Heat   ||7. input kode   ||
        # ||==================================||
        # ||3. Defrost      ||8. Cleaning     ||
        # ||==================================||
        # ||4. Grill        ||0. Stop         ||
        # ||==================================||
        # ||5. Vegetable    ||99. Child Lock  ||
        # ||==================================||
        # Pilih menu :

    def display2(self): #Fungsi ini adalah fungsi untuk menampilkan keadaan microwave saat sedang melakukan pemasakan
        while self.time >= 0:
            os.system('cls')
            Microwave.displayup()
            side_v = 6
            while side_v>0:
                side_h = 38
                while side_h>0:
                    if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                        print('|', end='')
                    elif (side_h == 1):
                        print('|')
                    elif side_h<37 and side_h>18:
                        print(' ',end='')
                    elif side_h == 16:
                        if side_v == 6:
                            if self.temp < 10:
                                print(f'Temp || {self.temp}°C ||',end='')
                            elif self.temp < 100:
                                print(f'Temp || {self.temp}°C||',end='')
                            else:
                                print(f'Temp ||{self.temp}°C||',end='')
                        elif side_v == 5:
                            min, sec = divmod(self.time, 60)
                            print(f'Time ||{min:02d}:{sec:02d}||',end='')
                            #Fungsi ini menampilkan display secara dinamis dengan menunjukkan countdown waktu pemasakan dan pengurangan nilai kelembaban
                        elif side_v == 4:
                            moisture = self.moisture + (self.temp/1500)*self.time
                            if moisture <10:
                                print(f'Mois ||   {int(round(moisture, 0))}%||',end='')
                            elif moisture<100:
                                print(f'Mois ||  {int(round(moisture, 0))}%||',end='')
                            else:
                                moisture = 100
                                print(f'Mois || {int(round(moisture, 0))}%||',end='')
                        elif side_v == 3:
                            print(" _ _ _ _ _ ___",end='')
                        elif side_v == 2:
                            print("|1|3|4|5|6|   ",end='')
                        else:
                            print("|7|8|0| 99|___",end='')
                    side_h-=1
                side_v-=1
            Microwave.displaydown()
            time.sleep(0.0001) 
            self.time -= 1
        
        #Tampilan microwave saat ditengah-tengah pemasakan akan terlihat seperti ini
        # ======================================
        # ||==================||==============||
        # ||                  ||Temp ||500°C||||
        # ||                  ||Time ||01:03||||
        # ||                  ||Mois ||  46%||||
        # ||                  || _ _ _ _ _ ___||
        # ||                  |||1|3|4|5|6|   ||
        # ======================================
        # ||==================||==============||

    def displayover(self): #Fungsi ini adalah fungsi untuk menampilkan hasil pemasakan yang "overcooked" dan juga menampilkan kembali menu utama microwave
        Microwave.displayup()
        side_v = 6
        while side_v>0:
            side_h = 38
            while side_h>0:
                if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                    print('|', end='')
                elif (side_h == 1):
                    print('|')
                elif side_h<37 and side_h>18:
                    if side_v == 4:
                        if side_h>29 or side_h<26:
                            print(' ',end='')
                        elif side_h == 29:
                            print("OVER", end='')
                    elif side_v == 3:
                        if side_h>29 or side_h<26:
                            print(' ',end='')
                        elif side_h == 29:
                            print("COOK", end='')
                    else:
                        print(' ',end='')
                elif side_h == 16:
                    if side_v == 6:
                        if self.temp < 10:
                            print(f'Temp || {self.temp}°C ||',end='')
                        elif self.temp < 100:
                            print(f'Temp || {self.temp}°C||',end='')
                        else:
                            print(f'Temp ||{self.temp}°C||',end='')
                    elif side_v == 5:
                        print(f'Time ||00:00||',end='')
                    elif side_v == 4:
                        if self.moisture<10:
                            print(f'Mois ||   {int(round(self.moisture, 0))}%||',end='')
                        else:
                            print(f'Mois ||  {int(round(self.moisture, 0))}%||',end='')
                    elif side_v == 3:
                        print(" _ _ _ _ _ ___",end='')
                    elif side_v == 2:
                        print("|1|3|4|5|6|   ",end='')
                    else:
                        print("|7|8|0| 99|___",end='')
                side_h-=1
            side_v-=1
        Microwave.displaydown()

        # Tamplian menu setelah pemasakan akan terlihat seperti ini
        # ======================================
        # ||==================||==============||
        # ||                  ||Temp || 300°C|||
        # ||                  ||Time ||00:00||||
        # ||       OVER       ||Mois ||  1 %||||
        # ||       COOK       || _ _ _ _ _ ___||
        # ||                  |||1|3|4|5|6|   ||
        # ||                  |||7|8|0| 99|___||
        # ||==================||==============||
        # ======================================
        # ======================================
        # ||1. Manual mode  ||6. Seafood      ||
        # ||==================================||
        # ||2. Quick Heat   ||7. input kode   ||
        # ||==================================||
        # ||3. Defrost      ||8. Cleaning     ||
        # ||==================================||
        # ||4. Grill        ||0. Stop         ||
        # ||==================================||
        # ||5. Vegetable    ||99. Child Lock  ||
        # ||==================================||
        # Pilih menu : 

    def displaydry(self): #Fungsi ini adalah fungsi untuk menampilkan hasil pemasakan yang "dry cook" dan juga menampilkan kembali menu utama microwave
        Microwave.displayup()
        side_v = 6
        while side_v>0:
            side_h = 38
            while side_h>0:
                if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                    print('|', end='')
                elif (side_h == 1):
                    print('|')
                elif side_h<37 and side_h>18:
                    if side_v == 4:
                        if side_h>29 or side_h<27:
                            print(' ',end='')
                        elif side_h == 29:
                            print("DRY", end='')
                    elif side_v == 3:
                        if side_h>29 or side_h<26:
                            print(' ',end='')
                        elif side_h == 29:
                            print("COOK", end='')
                    else:
                        print(' ',end='')
                elif side_h == 16:
                    if side_v == 6:
                        if self.temp < 10:
                            print(f'Temp || {self.temp}°C ||',end='')
                        elif self.temp < 100:
                            print(f'Temp || {self.temp}°C||',end='')
                        else:
                            print(f'Temp ||{self.temp}°C||',end='')
                    elif side_v == 5:
                        print(f'Time ||00:00||',end='')
                    elif side_v == 4:
                        if self.moisture<10:
                            print(f'Mois ||   {int(round(self.moisture, 0))}%||',end='')
                        else:
                            print(f'Mois ||  {int(round(self.moisture, 0))}%||',end='')
                    elif side_v == 3:
                        print(" _ _ _ _ _ ___",end='')
                    elif side_v == 2:
                        print("|1|3|4|5|6|   ",end='')
                    else:
                        print("|7|8|0| 99|___",end='')
                side_h-=1
            side_v-=1
        Microwave.displaydown()

        # Tamplian menu setelah pemasakan akan terlihat seperti ini
        # ======================================
        # ||==================||==============||
        # ||                  ||Temp || 200°C|||
        # ||                  ||Time ||00:00||||
        # ||       DRY        ||Mois ||  25%||||
        # ||       COOK       || _ _ _ _ _ ___||
        # ||                  |||1|3|4|5|6|   ||
        # ||                  |||7|8|0| 99|___||
        # ||==================||==============||
        # ======================================
        # ======================================
        # ||1. Manual mode  ||6. Seafood      ||
        # ||==================================||
        # ||2. Quick Heat   ||7. input kode   ||
        # ||==================================||
        # ||3. Defrost      ||8. Cleaning     ||
        # ||==================================||
        # ||4. Grill        ||0. Stop         ||
        # ||==================================||
        # ||5. Vegetable    ||99. Child Lock  ||
        # ||==================================||
        # Pilih menu : 

    def displaydone(self): #Fungsi ini adalah fungsi untuk menampilkan hasil pemasakan yang baik (well done) dan juga menampilkan kembali menu utama microwave
        Microwave.displayup()
        side_v = 6
        while side_v>0:
            side_h = 38
            while side_h>0:
                if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                    print('|', end='')
                elif (side_h == 1):
                    print('|')
                elif side_h<37 and side_h>18:
                    if side_v == 4:
                        if side_h>29 or side_h<26:
                            print(' ',end='')
                        elif side_h == 29:
                            print("WELL", end='')
                    elif side_v == 3:
                        if side_h>29 or side_h<26:
                            print(' ',end='')
                        elif side_h == 29:
                            print("DONE", end='')
                    else:
                        print(' ',end='')
                elif side_h == 16:
                    if side_v == 6:
                        if self.temp < 10:
                            print(f'Temp || {self.temp}°C ||',end='')
                        elif self.temp < 100:
                            print(f'Temp || {self.temp}°C||',end='')
                        else:
                            print(f'Temp ||{self.temp}°C||',end='')
                    elif side_v == 5:
                        print(f'Time ||00:00||',end='')
                    elif side_v == 4:
                        if self.moisture<10:
                            print(f'Mois ||   {int(round(self.moisture, 0))}%||',end='')
                        else:
                            print(f'Mois ||  {int(round(self.moisture, 0))}%||',end='')
                    elif side_v == 3:
                        print(" _ _ _ _ _ ___",end='')
                    elif side_v == 2:
                        print("|1|3|4|5|6|   ",end='')
                    else:
                        print("|7|8|0| 99|___",end='')
                side_h-=1
            side_v-=1
        Microwave.displaydown()

        # Tamplian menu setelah pemasakan akan terlihat seperti ini
        # ======================================
        # ||==================||==============||
        # ||                  ||Temp || 70°C||||
        # ||                  ||Time ||00:00||||
        # ||       WELL       ||Mois ||  80%||||
        # ||       DONE       || _ _ _ _ _ ___||
        # ||                  |||1|3|4|5|6|   ||
        # ||                  |||7|8|0| 99|___||
        # ||==================||==============||
        # ======================================
        # ======================================
        # ||1. Manual mode  ||6. Seafood      ||
        # ||==================================||
        # ||2. Quick Heat   ||7. input kode   ||
        # ||==================================||
        # ||3. Defrost      ||8. Cleaning     ||
        # ||==================================||
        # ||4. Grill        ||0. Stop         ||
        # ||==================================||
        # ||5. Vegetable    ||99. Child Lock  ||
        # ||==================================||
        # Pilih menu : 

    def menu(): #Fungsi ini digunakan untuk menampilkan menu utama microwave dalam keadaan normal
        print(f'======================================')
        print(f'||1. Manual mode  ||6. Seafood      ||')
        print(f'||==================================||')
        print(f'||2. Quick Heat   ||7. input kode   ||')
        print(f'||==================================||')
        print(f'||3. Defrost      ||8. Cleaning     ||')
        print(f'||==================================||')
        print(f'||4. Grill        ||0. Stop         ||')
        print(f'||==================================||')
        print(f'||5. Vegetable    ||99. Child Lock  ||')
        print(f'||==================================||')
    def menulock(): #Fungsi ini digunakan untuk menampilkan menu utama microwave dalam keadaan child lock
        print(f'======================================')
        print(f'||1. Manual mode🔒||6. Seafood🔒    ||')
        print(f'||==================================||')
        print(f'||2. Quick Heat🔒 ||7. input kode🔒 ||')
        print(f'||==================================||')
        print(f'||3. Defrost🔒    ||8. Cleaning🔒   ||')
        print(f'||==================================||')
        print(f'||4. Grill🔒      ||0. Stop🔒       ||')
        print(f'||==================================||')
        print(f'||5. Vegetable🔒  ||99.Child Lock🔒 ||')
        print(f'||==================================||')

    def Start(): #Fungsi start ini adalah fungsi utama dalam program microwave ini, fungsi ini mengintegrasikan semua fungsi-fungsi yang ada untuk user menggunakan microwave
        ChildLock = False #Awalnya mode childlock dalam keadaan tidak aktif
        Microwave.display1() #Menampilkan menu utama microwave
        while True: #Selama user masih mau menggunakan microwave
            if ChildLock == False:
                Microwave.menu() #Microwave menampilan menu-menu yang dapat dipilih oleh user
                choice = int(input("Pilih menu : ")) #User menginput menu yang ingin digunakan
                os.system('cls')
                if choice == 1: #User memilih untuk menggunakan mode manual
                    Microwave.display1()
                    #User memasukkan nilai waktu dan temperatur pemasakan sesuai kehendaknya
                    time = int(input("Masukan waktu Memasak(menit) : "))
                    temp = int(input("Masukan Temperatur(°C) : "))
                    moisture = 100
                    food = Microwave(time, temp, moisture)
                    food.moisture1(0.8)
                    food.display2()
                    if food.moisture < 1: #Apabila pada akhir pemasakan kelembabannya kurang dari 1% maka hasil pemasakan menjadi kering
                        os.system('cls')
                        food.displaydry()
                    elif food.moisture < 40: #Apabila pada akhir pemasakan kelembabannya kurang dari 40% maka hasil pemasakan menjadi overcooked
                        os.system('cls')
                        food.displayover()
                    else: #Selain dari kedua itu, maka hasil pemasakan baik (well-done)
                        os.system('cls')
                        food.displaydone()
                elif choice == 2: #User memilih untuk menggunakan mode quick heat untuk memanaskan makanan
                    food = mode(2, 150, 90) #Mode ini berjalan selama 2 menit dengan temperatur 150 derajat celsius dan kelembaban awal 90%
                    food.quick_heat()
                elif choice == 3: #User memilih untuk menggunakan mode defrost untuk mencairkan makanan (terutama daging)
                    food = mode(8, 40, 90) #Mode ini berjalan selama 8 menit dengan temperatur 40 derajat celsius dan kelembaban awal 90%
                    food.Deforst() 
                elif choice == 4: #User memilih untuk menggunakan mode grill untuk memanggang makanan
                    food = mode(7, 230, 100) #Mode ini berjalan selama 7 menit dengan temperatur 230 derajat celsius dan kelembaban awal 100%
                    food.Grill()
                elif choice == 5: #User memilih untuk menggunakan mode memasak sayur
                    while True:
                        vegetable.menu() #Microwave menampilkan menu sayur yang tersedia
                        sayur = int(input("Pilih Sayur : ")) #User memasukkan pilihan sayur untuk dimasak
                        os.system('cls')
                        if sayur == 1: #Pilihan sayur pertama: brokoli, dengan lama pemasakan 2 menit, temperatur 200 derajat celsius dan kelembaban awal 100%
                            vegen = vegetable(2, 200, 100)
                            vegen.brokoli()
                            break
                        elif sayur == 2: #Pilihan sayur kedua: wortel, dengan lama pemasakan 4 menit, temperatur 200 derajat celsius dan kelembaban awal 100%
                            vegen = vegetable(4, 200, 100)
                            vegen.wortel()
                            break
                        elif sayur == 3: #Pilihan sayur ketiga: kembang kol, dengan lama pemasakan 4 menit, temperatur 180 derajat celsius dan kelembaban awal 100%
                            vegen = vegetable(4, 180, 100)
                            vegen.kembang_kol()
                            break
                        elif sayur == 4: #Pilihan sayur keempat: bayam, dengan lama pemasakan 3 menit, temperatur 160 derajat celsius dan kelembaban awal 100%
                            vegen = vegetable(3, 160, 100)
                            vegen.bayam()
                            break
                        elif sayur == 5: #Pilihan sayur kelima: jagung manis, dengan lama pemasakan 4 menit, temperatur 180 derajat celsius dan kelembaban awal 100%
                            vegen = vegetable(4, 180, 100)
                            vegen.jagung_manis()
                            break
                        elif sayur == 6: #Pilihan sayur keenam: paprika, dengan lama pemasakan 4 menit, temperatur 200 derajat celsius dan kelembaban awal 100%
                            vegen = vegetable(4, 200, 100)
                            vegen.paprika()
                            break
                        elif sayur == 7: #Pilihan sayur ketujuh: zucchini, dengan lama pemasakan 4 menit, temperatur 180 derajat celsius dan kelembaban awal 100%
                            vegen = vegetable(4, 180, 100)
                            vegen.zucchini()
                            break
                elif choice == 6: #User memilih untuk menggunakan mode memasak seafood
                    while True:
                        seafood.menu() #Microwave menampilkan menu seafood yang tersedia
                        seaf = int(input("Pilih Seafood : ")) #User memasukkan pilihan seafood untuk dimasak
                        if seaf == 1: #Pilihan seafood pertama: ikan fillet, dengan lama pemasakan 5 menit, temperatur 90 derajat celsius dan kelembaban awal 100%
                            ikan = seafood(5, 90, 100)
                            ikan.fish()
                            break
                        elif seaf == 2: #Pilihan seafood kedua: udang, dengan lama pemasakan 3 menit, temperatur 80 derajat celsius dan kelembaban awal 100%
                            udang = seafood(3, 80, 100)
                            udang.shrimp()
                            break
                        elif seaf == 3: #Pilihan seafood ketiga: cumi-cumi, dengan lama pemasakan 3 menit, temperatur 80 derajat celsius dan kelembaban awal 100%
                            cumi = seafood(3, 80, 100)
                            cumi.squid()
                            break
                        elif seaf == 4: #Pilihan seafood keempat: kerang, dengan lama pemasakan 4 menit, temperatur 80 derajat celsius dan kelembaban awal 100%
                            kerang = seafood(4, 80, 100)
                            kerang.shellfish()
                            break
                        elif seaf == 5: #Pilihan seafood kelima: lobster, dengan lama pemasakan 7 menit, temperatur 90 derajat celsius dan kelembaban awal 100%
                            lobster = seafood(7, 90, 100)
                            lobster.lobster()
                            break
                elif choice == 7: #User memilih untuk memasak paket makanan yang telah tersedia dari barcode
                    while True:
                        code = int(input("Masukan Code barcode: ")) #User memasukkan barcode makanan yang ingin dimasaknya
                        food = incode(0,0,0,0,0)
                        food.detect(code)
                        confirm = input(f'{food.namefood}? (y/n): ').lower() #Masukkan konfirmasi pemasakan makanan yang dipilih
                        if confirm == 'y':
                            food.cook() #Microwave melakukan pemasakan makanan yang dipilh
                            break
                elif choice == 8: #User memilih untuk melakukan pembersihan otomatis pada microwave
                    Microwave.display1()
                    print("Microwave telah dibersikan") #Microwave selesai dibersihkan
                elif choice == 99: #User memilih untuk mengaktifkan mode child-lock
                    Pinlock = int(input("Atur PIN :")) #Set pin untuk digunakan pada penggunaan microwave selanjutnya
                    ChildLock = True
                    os.system('cls')
                elif choice == 0: #User memilih untuk selesai menggunakan microwave
                    print("Terima Kasih telah menggunakan produk kami hehehe")
                    break
            else: #Child lock = True
                Microwave.display1()
                Microwave.menulock() #Karena mode child-lock nya aktif, maka display microwave menjadi berubah (ada lambang gemboknya)
                pin = int(input("Masukan PIN :")) #Masukkan pin yang telah dibuat sebelumnya untuk dapat menggunakan microwave
                if pin == Pinlock: #Apabila pin yang dimasukkan benar, maka mode child-lock akan dinonaktifkan kembali
                    ChildLock = False
                    os.system('cls')
                    Microwave.display1()
                elif pin == 0: #Apabila user memberi masukan 0 maka user memilih untuk selesai menggunakan microwave
                    print("Terima Kasih telah menggunakan produk kami hehehe")
                    break
                else: #Jika masukan pin salah, maka user tidak bisa menggunakan microwave hingga masukan pin benar
                    os.system('cls')
                                 
Microwave.Start() #Inisiasi memulai penggunaan microwave

# -*- coding: utf-8 -*-
"""TebakBuah.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1513tB7BA1jlZS9VEHfKYOdRfsBPr22Zz
"""

import random, time

def nama_buah():
    databuah = [
        "anggur", "apel", "aprikot", "asam", "atap", "arbei", "abiu", "alpukat", "anjeng", "bacang",
        "baguk", "belimbing", "bengkuang", "benda", "binjai", "bisbul", "blueberry", "burahol", "blewah", "bit",
        "cempedak", "ceplukan", "cermai", "ceri", "cokelat", "delima", "duku", "durian", "duwet", "enau",
        "enamenam", "frambos", "hamoi", "hamlam", "holdi", "jamblang", "jambuair", "jambubatu", "jambubol", "jambumawar",
        "jambumede", "jengkol", "jeruk", "jerukbali", "jerukkeprok", "jerukkingkit", "jeruknipis", "jerukpurut", "kapulasan", "kawista",
        "kecapi", "kedondong", "kelapa", "kelengkeng", "kelubi", "ketela", "kemang", "kepel", "kersen", "kesemek",
        "kokosan", "kiwi", "koldi", "kurma", "kelawi", "kenitu", "lai", "langsat", "lemon", "leci",
        "lobak", "maja", "malaka", "mangga", "manggis", "markisa", "melon", "mengkudu", "menteng", "matoa",
        "mentimun", "namnam", "nanas", "nangka", "naga", "nona", "pepaya", "persik", "pir", "pisang",
        "pete", "rambai", "rambusa", "rambutan", "rukem", "sawo", "semangka", "sirsak", "siwalan", "srikaya",
        "stroberi", "sukun", "terap", "terong", "tomat", "timunsuri", "ubi", "waluh", "wuni", "zaitun"
    ]
    buah = random.choice(databuah)
    return buah.upper()


def animasi_berpikir():
    print(f"\nPython sedang memikirkan nama buah 🤔", end="", flush=True )
    for _ in range(4):
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\b\b\b", end="", flush=True)
        time.sleep(0.4)

    print("\b\b\b, AHHHHA!! 💡\n", flush=True)
    time.sleep(0.5)


def main(kata):
    nyawa = len(kata)
    buah_sensor = "-" * len(kata)
    huruf_ditebak = []
    tertebak = False
    salah = 0

    animasi_berpikir()
    print(f"Ini dia nama buah yang harus kamu tebak: {buah_sensor}")
    print(f"Kamu punya {nyawa} kesempatan untuk menebak nama buah tersebut.")

    while (nyawa > 0) and (not tertebak):
        hati = "❤️" * nyawa + "💔" * salah
        print(f"\n{hati}")
        tebakan = input("Tebakan kamu? ").upper()

        if (len(tebakan) > 1) or (not tebakan.isalpha()):
            print("🙅‍♂️ Input kamu tidak valid, ulangi lagi")
            print("Masukkan satu huruf saja yaa 🙏")

        else:
            if tebakan in huruf_ditebak:
                print(f'🤦 Huruf "{tebakan}" sudah kamu tebak! ')

            elif tebakan not in kata:
                print(f'😢 Sayang sekali. Huruf "{tebakan}" tidak ada di dalam nama buah tersebut.')
                huruf_ditebak.append(tebakan)
                nyawa -= 1
                salah += 1

            else:
                print(f'🎉 Benar! Huruf "{tebakan}" ada di dalam nama buah tersebut.')
                list_buah_sensor = list(buah_sensor)
                indexing = [i for i, huruf in enumerate(kata) if tebakan == huruf]
                for index in indexing:
                    list_buah_sensor[index] = tebakan
                buah_sensor = "".join(list_buah_sensor)
                huruf_ditebak.append(tebakan)

                if "-" not in buah_sensor:
                    tertebak = True

        print(f"\nNama buah: {buah_sensor}")

    if tertebak:
        print(f"\n🎊🥳 YEYYY SELAMAT! Kamu berhasil menebak nama buah dengan benar: {kata} 🥳🎊\n")
    else:
        print("\n" + "💔" * salah)
        print("Yahhh kamu kalah 😔")
        print(f"Nama buahnya adalah: {kata}\n")


def loop_program():
    print(f"🍇🍎🍊🍋🍏 Selamat datang di Permainan Tebak Nama Buah! 🍇🍎🍊🍋🍏\n")
    lagi = "y"
    while lagi != "t":
        time.sleep(0.7)
        kata = nama_buah()
        main(kata)
        while True:
            lagi = input("Mau main lagi (y/t)? ").lower()
            if lagi in ["y", "t"]:
                break
    print("🍉🍒🍈 *SELESAI* 🍉🍒🍈")
    print("Terima kasih telah bermain! Dahhh 👋")


# =====================================
"""PROGRAM UTAMA"""
print("""
Permainan Tebak Nama Buah
Oleh Kelompok 9
Radhi Athaya Nugraha\t(1306622013)
Maudina Rohmah\t\t(1306622016)
Windi Putri Lisna Dewi\t(1306622019)
""")
loop_program()
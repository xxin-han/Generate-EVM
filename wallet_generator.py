import time
import sys
import random
from eth_account import Account
from colorama import init, Fore, Style
import os

init(autoreset=True)  

def show_banner():
    os.system('cls' if os.name == 'nt' else 'clear')  

    print(Fore.YELLOW)
    print("                    XXXXXXX       XXXXXXX  iiii                         999999999          888888888     ")
    print("                    X:::::X       X:::::X i::::i                      99:::::::::99      88:::::::::88   ")
    print("                    X:::::X       X:::::X  iiii                     99:::::::::::::99  88:::::::::::::88 ")
    print("                    X::::::X     X::::::X                          9::::::99999::::::98::::::88888::::::8")
    print("xxxxxxx      xxxxxxxXXX:::::X   X:::::XXXiiiiiii nnnn  nnnnnnnn    9:::::9     9:::::98:::::8     8:::::8")
    print(" x:::::x    x:::::x    X:::::X X:::::X   i:::::i n:::nn::::::::nn  9:::::9     9:::::98:::::8     8:::::8")
    print("  x:::::x  x:::::x      X:::::X:::::X     i::::i n::::::::::::::nn  9:::::99999::::::9 8:::::88888:::::8 ")
    print("   x:::::xx:::::x        X:::::::::X      i::::i nn:::::::::::::::n  99::::::::::::::9  8:::::::::::::8  ")
    print("    x::::::::::x         X:::::::::X      i::::i   n:::::nnnn:::::n    99999::::::::9  8:::::88888:::::8 ")
    print("     x::::::::x         X:::::X:::::X     i::::i   n::::n    n::::n         9::::::9  8:::::8     8:::::8")
    print("     x::::::::x        X:::::X X:::::X    i::::i   n::::n    n::::n        9::::::9   8:::::8     8:::::8")
    print("    x::::::::::x    XXX:::::X   X:::::XXX i::::i   n::::n    n::::n       9::::::9    8:::::8     8:::::8")
    print("   x:::::xx:::::x   X::::::X     X::::::Xi::::::i  n::::n    n::::n      9::::::9     8::::::88888::::::8")
    print("  x:::::x  x:::::x  X:::::X       X:::::Xi::::::i  n::::n    n::::n     9::::::9       88:::::::::::::88 ")
    print(" x:::::x    x:::::x X:::::X       X:::::Xi::::::i  n::::n    n::::n    9::::::9          88:::::::::88   ")
    print("xxxxxxx      xxxxxxxXXXXXXX       XXXXXXXiiiiiiii  nnnnnn    nnnnnn   99999999             888888888     ")
    print(Style.RESET_ALL)
    print(Fore.CYAN + "🚀 Welcome to the xXin98 auto generate EVM Wallet!")
    print(Fore.MAGENTA + "🐦 Follow us on Twitter: @xXin98")
    time.sleep(3)


show_banner()

def loading_animation(text="Membuat wallet", duration=1.5):
    spinner = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    idx = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{text}... {spinner[idx % len(spinner)]}")
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * (len(text) + 10) + "\r")

def generate_wallets():
    Account.enable_unaudited_hdwallet_features()

    try:
        jumlah = int(input("🔢 Masukkan jumlah wallet yang ingin dibuat: "))
        if jumlah <= 0:
            print("❌ Jumlah harus lebih dari 0.")
            return
    except ValueError:
        print("❌ Input tidak valid. Harus berupa angka.")
        return

    private_file = "private_keys.txt"
    mnemonic_file = "mnemonics.txt"

    with open(private_file, "w") as f_priv, open(mnemonic_file, "w") as f_mnem:
        for i in range(jumlah):
            print("=" * 50)
            print(f"🧪 Membuat Wallet #{i+1}")
            loading_animation()

            # Buat wallet baru
            account, mnemonic = Account.create_with_mnemonic()
            address = account.address
            private_key = "0x" + account.key.hex()

            # Validasi
            regenerated = Account.from_key(private_key)
            assert regenerated.address == address

            # Tampilkan di terminal
            print(f"🏷️ Address       : {address}")
            print(f"🔐 Private Key  : {private_key}")
            print(f"🧠 Mnemonic     : {mnemonic}")
            print("✅ Wallet berhasil dibuat!")

            # Simpan ke file
            f_priv.write(private_key + "\n")
            f_mnem.write(f"{address} : {mnemonic}\n")

            time.sleep(random.uniform(0.4, 0.9))
            print("=" * 50)

    print(f"\n📁 Semua private key disimpan di: '{private_file}'")
    print(f"📁 Address + mnemonic disimpan di: '{mnemonic_file}'")

if __name__ == "__main__":
    generate_wallets()

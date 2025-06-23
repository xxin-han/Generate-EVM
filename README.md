# Wallet Generator

Script Python ini digunakan untuk membuat wallet Ethereum secara otomatis lengkap dengan:
- 🔐 Private Key
- 🧠 Mnemonic Phrase
- 🏷️ Public Address
---

## 📦 Fitur

- Membuat banyak wallet sekaligus
- Menyimpan Private Key ke `private_keys.txt`
- Menyimpan Mnemonic + Address ke `mnemonics.txt`
- Validasi alamat berdasarkan Private Key

---

## Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/xxin-han/Generate-EVM.git
cd Generate-EVM
```

## Buat Virtual Environment (Opsional tapi Direkomendasikan)
```bash
python -m venv venv
source venv/bin/activate     # Untuk Linux/macOS
venv\\Scripts\\activate      # Untuk Windows
```

## Install Dependensi
```bash
pip install -r requirements.txt
```
## Run Bot
```bash
python wallet_generator.py
```

## 🗂️ Output
Setelah selesai, kamu akan mendapatkan 2 file:

private_keys.txt — berisi daftar private key

mnemonics.txt — berisi address dan mnemonic phrase


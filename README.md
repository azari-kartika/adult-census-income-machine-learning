# Adult Census Income - Machine Learning

Repositori ini berisi:

1. File ipynb eksplorasi data (EDA) untuk dataset Adult Census Income (sumber: Kaggle / UCI Machine Learning Repository), digunakan untuk mengisi https://www.kaggle.com/datasets/uciml/adult-census-income Laporan Karakteristik Dataset.
2. Laporan Karakteristik Dataset
3. File ipynb untuk melanjutkan hasil EDA sebelumnya (`analisis_adult_dataset.ipynb`) dengan menerapkan teknik optimasi untuk menangani temuan-temuan pada analisis sebelumnya.

## Instalasi

### 1. Clone repository
```bash
git clone https://github.com/azari-kartika/adult-census-income-machine-learning.git
cd adult-census-income-machine-learning
```

### 2. Buat virtual environment
```bash
python -m venv .venv
```

### 3. Aktifkan virtual environment
Windows (Git Bash / MINGW64):
```bash
source .venv/Scripts/activate
```
Windows (Command Prompt):
```bash
.venv\Scripts\activate
```
macOS / Linux:
```bash
source .venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Jalankan notebook
Buka folder ini di VSCode, lalu buka file `.ipynb` yang diinginkan dan pilih kernel `.venv` (Python 3.13.15) di pojok kanan atas notebook.

## Struktur File

| File | Deskripsi |
|---|---|
| `adult.csv` | Dataset mentah Adult Census Income |
| `analisis_adult_dataset.ipynb` | Notebook eksplorasi data (EDA) |
| `analisis_adult_dataset_optimasi.ipynb` | Notebook lanjutan dengan teknik optimasi model (handling class imbalance) |
| `requirements.txt` | Daftar dependency Python yang dibutuhkan |
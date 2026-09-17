import pandas as pd

df = pd.read_csv('adult.csv')

# ======================================================
# 1. INFORMASI UMUM DATASET
# ======================================================
print("=== INFORMASI UMUM ===")
print("Shape (baris, kolom):", df.shape)
print()
print("Tipe data tiap kolom:")
print(df.dtypes)
print()
print("Contoh data:")
print(df.head(3))
print()


# ======================================================
# 2. DATA DICTIONARY (unique value untuk kolom kategorikal)
# ======================================================
print("=== JUMLAH NILAI UNIK PER KOLOM KATEGORIKAL ===")
cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    print(f"{col}: {df[col].nunique()} kategori -> {df[col].unique()[:10]}")
print()


# ======================================================
# 3. ANALISIS KUALITAS DATA
# ======================================================
print("=== MISSING VALUES (NaN literal) ===")
print(df.isna().sum())
print()

# dataset ini menandai data hilang dengan simbol '?', bukan NaN
print("=== MISSING VALUES (simbol '?') ===")
for col in cat_cols:
    cnt = (df[col] == '?').sum()
    if cnt > 0:
        print(f"{col}: {cnt} baris ({cnt/len(df)*100:.2f}%)")
print()

print("=== DATA DUPLIKAT ===")
print("Jumlah baris duplikat penuh:", df.duplicated().sum())
print()

# deteksi outlier numerik dengan metode IQR (1.5 x IQR)
print("=== OUTLIER (metode IQR) ===")
num_cols = ['age', 'fnlwgt', 'education.num',
            'capital.gain', 'capital.loss', 'hours.per.week']

for col in num_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"{col}: {len(outliers)} outlier ({len(outliers)/len(df)*100:.2f}%), "
          f"batas normal=({lower:.2f}, {upper:.2f})")
print()


# ======================================================
# 4. STATISTIK DESKRIPTIF (FITUR NUMERIK)
# ======================================================
print("=== STATISTIK DESKRIPTIF ===")
desc = df[num_cols].describe().T[['mean', 'std', 'min', '25%', '50%', '75%', 'max']]
pd.set_option('display.float_format', lambda x: f'{x:,.2f}')
print(desc)
print()


# ======================================================
# 5. DISTRIBUSI TARGET & KORELASI
# ======================================================
print("=== DISTRIBUSI VARIABEL TARGET (income) ===")
print(df['income'].value_counts())
print(df['income'].value_counts(normalize=True) * 100)
print()

print("=== KORELASI FITUR NUMERIK TERHADAP TARGET ===")
# ubah target jadi biner (1 = '>50K', 0 = '<=50K') agar bisa dihitung korelasinya
df['income_bin'] = (df['income'] == '>50K').astype(int)

corr = df[num_cols + ['income_bin']].corr()
print("Korelasi terhadap target (diurutkan):")
print(corr['income_bin'].sort_values(ascending=False))
print()
print("Matriks korelasi lengkap:")
print(corr.round(2))

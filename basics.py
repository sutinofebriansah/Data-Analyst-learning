import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1. BACA DATA
# =========================
df = pd.read_csv("data_penjualan.csv")

print("=== DATA AWAL ===")
print(df)

# =========================
# 2. STATISTIK DASAR
# =========================
rata_penjualan = df["Penjualan"].mean()
total_penjualan = df["Penjualan"].sum()

print("\nRata-rata penjualan:", rata_penjualan)
print("Total penjualan:", total_penjualan)

# =========================
# 3. FILTER DATA
# =========================
print("\nProduk dengan penjualan > 30")
print(df[df["Penjualan"] > 30])

# =========================
# 4. TAMBAH KOLOM KATEGORI
# =========================
def kategori_penjualan(x):
    if x > 40:
        return "Tinggi"
    else:
        return "Rendah"

df["Kategori"] = df["Penjualan"].apply(kategori_penjualan)

print("\nData dengan Kategori")
print(df)

# =========================
# 5. SORTING & RANKING
# =========================
df_sorted = df.sort_values(by="Penjualan", ascending=False)
df_sorted["Ranking"] = range(1, len(df_sorted) + 1)

print("\nData setelah sorting & ranking")
print(df_sorted)

# =========================
# 6. PRODUK TERLARIS & TERENDAH
# =========================
produk_terlaris = df.loc[df["Penjualan"].idxmax()]
produk_terendah = df.loc[df["Penjualan"].idxmin()]

print("\nProduk Terlaris")
print(produk_terlaris)

print("\nProduk Terendah")
print(produk_terendah)

# =========================
# 7. KONTRIBUSI PENJUALAN (%)
# =========================
df_sorted["Kontribusi (%)"] = (
    df_sorted["Penjualan"] / total_penjualan * 100
).round(2)

print("\nKontribusi Penjualan (%)")
print(df_sorted)

# =========================
# 8. RINGKASAN PER KATEGORI
# =========================
ringkasan = df.groupby("Kategori").agg(
    Jumlah_Produk=("Produk", "count"),
    Rata_Penjualan=("Penjualan", "mean"),
    Total_Penjualan=("Penjualan", "sum")
).reset_index()

print("\nRingkasan per Kategori")
print(ringkasan)

# =========================
# 9. VISUALISASI
# =========================

# Bar chart penjualan per produk
plt.bar(df["Produk"], df["Penjualan"])
plt.title("Penjualan per Produk")
plt.xlabel("Produk")
plt.ylabel("Penjualan")
plt.show()

# Pie chart kontribusi penjualan
plt.pie(
    df_sorted["Kontribusi (%)"],
    labels=df_sorted["Produk"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Kontribusi Penjualan per Produk")
plt.show()

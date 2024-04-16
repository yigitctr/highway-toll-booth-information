import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Veri seti yükleme
data = pd.read_csv("toll_data.csv")  # Örnek bir veri dosyası

# Ana uygulama penceresini oluşturma
root = tk.Tk()
root.title("Ücretli Yol Ücret Hesaplama")

# Giriş alanlarını ve etiketleri oluşturma
label1 = tk.Label(root, text="Araba Kilometresi:")
label1.grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

# Giriş alanlarını ve etiketleri oluşturma devamı
label2 = tk.Label(root, text="Araç Sınıfı:")
label2.grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Ücret hesapla fonksiyonu
def calculate_fee():
    try:
        # Girişlerden değerleri al
        km = float(entry1.get())
        vehicle_class = int(entry2.get())

        # Veri setinden ilgili ücreti al
        fee = data.loc[data['Vehicle Class'] == vehicle_class, 'Fee'].iloc[0]

        # Hesaplanan ücreti ekrana yazdır
        messagebox.showinfo("Ücret", f"Ödenecek Ücret: {fee * km} TL")
    except Exception as e:
        messagebox.showerror("Hata", "Hesaplama sırasında bir hata oluştu. Lütfen girdileri kontrol edin.")

# Hesapla düğmesi oluşturma
calculate_button = tk.Button(root, text="Hesapla", command=calculate_fee)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Ana döngüyü başlatma
root.mainloop()

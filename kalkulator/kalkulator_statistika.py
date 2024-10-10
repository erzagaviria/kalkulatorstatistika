import os
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import math

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_data():
    while True:
        try:
            n = int(input("Masukkan jumlah data yang akan diinputkan: "))
            if n <= 0:
                print("Jumlah data harus lebih dari 0.")
                continue
            break
        except ValueError:
            print("Input harus berupa angka.")
    data = []
    for i in range(n):
        while True:
            try:
                num = float(input(f"Masukkan data ke-{i+1}: "))
                data.append(num)
                break
            except ValueError:
                print("Input harus berupa angka.")
    data.sort()
    print("Data telah diurutkan:", data)
    input("Tekan Enter untuk melanjutkan...")
    clear_screen()
    return data

def calculate_mean(data):
    mean = sum(data) / len(data)
    print(f"Rata-rata (Mean): {mean}")
    input("Tekan Enter untuk melanjutkan...")
    clear_screen()
    return mean

def calculate_mode(data):
    count = Counter(data)
    modes = [k for k, v in count.items() if v == max(count.values())]
    if len(modes) == len(data):
        print("Tidak ada modus.")
        input("Tekan Enter untuk melanjutkan...")
        clear_screen()
        return None
    print(f"Modus: {modes}")
    input("Tekan Enter untuk melanjutkan...")
    clear_screen()
    return modes

def calculate_median(data):
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        median = (data[mid - 1] + data[mid]) / 2
    else:
        median = data[mid]
    print(f"Median: {median}")
    input("Tekan Enter untuk melanjutkan...")
    clear_screen()
    return median

def calculate_midrange(data):
    midrange = (data[0] + data[-1]) / 2
    print(f"Midrange: {midrange}")
    input("Tekan Enter untuk melanjutkan...")
    clear_screen()
    return midrange

def calculate_midhinge(data):
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        Q1 = (data[mid - 1] + data[mid]) / 2
        Q3 = (data[mid - 1] + data[mid]) / 2  # Adjust if needed
    else:
        Q1 = data[mid // 2]
        Q3 = data[mid + mid // 2]
    midhinge = (Q1 + Q3) / 2
    print(f"Midhinge: {midhinge}")
    input("Tekan Enter untuk melanjutkan...")
    clear_screen()
    return midhinge

def calculate_quartiles(data):
    n = len(data)
    def interpolate_quartile(pos):
        lower = math.floor(pos)
        upper = math.ceil(pos)
        if lower == upper:
            return data[lower - 1]
        else:
            return data[lower - 1] + (pos - lower) * (data[upper - 1] - data[lower - 1])

    Q1_pos = 0.25 * (n + 1)
    Q2_pos = 0.50 * (n + 1)
    Q3_pos = 0.75 * (n + 1)

    Q1 = interpolate_quartile(Q1_pos)
    Q2 = interpolate_quartile(Q2_pos)
    Q3 = interpolate_quartile(Q3_pos)

    print(f"Kuartil 1 (Q1): {Q1}")
    print(f"Kuartil 2 (Q2/Median): {Q2}")
    print(f"Kuartil 3 (Q3): {Q3}")
    input("Tekan Enter untuk melanjutkan...")
    clear_screen()
    return Q1, Q2, Q3

def calculate_iqr(Q1, Q3):
    IQR = Q3 - Q1
    print(f"Jangkauan Antar Kuartil (IQR): {IQR}")
    input("Tekan Enter untuk melanjutkan...")
    clear_screen()
    return IQR

def calculate_outliers(data, Q1, Q3, IQR):
    LIF = Q1 - 1.5 * IQR
    UIF = Q3 + 1.5 * IQR
    LOF = Q1 - 3 * IQR
    UOF = Q3 + 3 * IQR
    potential_outliers = [x for x in data if x < LIF or x > UIF]

    print(f"Lower Inner Fence (LIF): {LIF}")
    print(f"Upper Inner Fence (UIF): {UIF}")
    print(f"Lower Outer Fence (LOF): {LOF}")
    print(f"Upper Outer Fence (UOF): {UOF}")
    print(f"Outliers: {potential_outliers}")

    input("Tekan Enter untuk melanjutkan...")
    clear_screen()
    return LIF, UIF, LOF, UOF, potential_outliers

def box_whisker_plot(data, Q1, Q2, Q3, IQR, LIF, UIF, LOF, UOF):
    plt.figure(figsize=(10, 6))
    plt.boxplot(data, vert=False, patch_artist=True,
                boxprops=dict(facecolor='lightblue'))

    # Data in between Q1 and Q3
    between_Q1_Q3 = [x for x in data if Q1 <= x <= Q3]
    
    # Add fences and other statistics to plot
    plt.axvline(x=LIF, color='red', linestyle='--', label='Lower Inner Fence (LIF)')
    plt.axvline(x=UIF, color='green', linestyle='--', label='Upper Inner Fence (UIF)')
    plt.axvline(x=LOF, color='orange', linestyle=':', label='Lower Outer Fence (LOF)')
    plt.axvline(x=UOF, color='purple', linestyle=':', label='Upper Outer Fence (UOF)')
    
    plt.title('Box-Whisker Plot')
    plt.xlabel('Nilai')
    plt.legend()

    # Display points between Q1 and Q3
    print(f"Data di antara Q1 dan Q3: {between_Q1_Q3}")
    
    # Save the plot
    plt.savefig('box_whisker_plot.png')
    plt.show()
    print("Box-Whisker plot telah disimpan sebagai 'box_whisker_plot.png'.")
    input("Tekan Enter untuk melanjutkan...")
    clear_screen()

def stem_leaf(data):
    print("Stem-and-Leaf Diagram:")
    stems = {}
    for num in data:
        stem = int(num)
        leaf = int(round((num - stem) * 10))
        if stem in stems:
            stems[stem].append(leaf)
        else:
            stems[stem] = [leaf]
    for stem in sorted(stems):
        leaves = ' '.join(map(str, sorted(stems[stem])))
        print(f"{stem} | {leaves}")
    input("Tekan Enter untuk melanjutkan...")
    clear_screen()

def main_menu():
    data = []
    while True:
        print("\n=== Kalkulator Probabilitas dan Statistika ===")
        print("1. Masukkan Data")
        print("2. Tampilkan Data Terurut")
        print("3. Analisis Statistika")
        print("4. Exit")
        choice = input("Pilih menu: ")
        
        if choice == '1':
            data = input_data()
        elif choice == '2':
            if not data:
                print("Data belum diinputkan.")
            else:
                print("Data Terurut:", data)
            input("Tekan Enter untuk melanjutkan...")
            clear_screen()
        elif choice == '3':
            if not data:
                print("Data belum diinputkan.")
                continue
            while True:
                print("\n--- Menu Analisis Statistika ---")
                print("1. Hitung Rata-rata (Mean)")
                print("2. Hitung Modus")
                print("3. Hitung Median")
                print("4. Hitung Midrange")
                print("5. Hitung Midhinge")
                print("6. Hitung Kuartil")
                print("7. Hitung Desil")
                print("8. Hitung Presentil")
                print("9. Hitung Jangkauan Antar Kuartil (IQR)")
                print("10. Tampilkan Diagram Stem-and-Leaf")
                print("11. Tampilkan Box-Whisker Plot")
                print("12. Kembali ke Menu Utama")
                sub_choice = input("Pilih menu analisis: ")

                if sub_choice == '1':
                    calculate_mean(data)
                elif sub_choice == '2':
                    calculate_mode(data)
                elif sub_choice == '3':
                    calculate_median(data)
                elif sub_choice == '4':
                    calculate_midrange(data)
                elif sub_choice == '5':
                    calculate_midhinge(data)
                elif sub_choice == '6':
                    Q1, Q2, Q3 = calculate_quartiles(data)
                elif sub_choice == '7':
                    calculate_deciles(data)
                elif sub_choice == '8':
                    calculate_percentiles(data)
                elif sub_choice == '9':
                    if 'Q1' not in locals() or 'Q3' not in locals():
                        Q1, Q2, Q3 = calculate_quartiles(data)
                    IQR = calculate_iqr(Q1, Q3)
                elif sub_choice == '10':
                    stem_leaf(data)
                elif sub_choice == '11':
                    if 'Q1' not in locals() or 'Q3' not in locals():
                        Q1, Q2, Q3 = calculate_quartiles(data)
                    IQR = calculate_iqr(Q1, Q3)
                    LIF, UIF, LOF, UOF, _ = calculate_outliers(data, Q1, Q3, IQR)
                    box_whisker_plot(data, Q1, Q2, Q3, IQR, LIF, UIF, LOF, UOF)
                elif sub_choice == '12':
                    clear_screen()
                    break
                else:
                    print("Pilihan tidak valid.")
                    input("Tekan Enter untuk melanjutkan...")
                    clear_screen()
        elif choice == '4':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk melanjutkan...")
            clear_screen()

if __name__ == '__main__':
    main_menu()

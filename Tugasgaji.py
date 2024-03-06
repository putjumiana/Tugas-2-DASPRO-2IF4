print("========Aplikasi Gaji Karyawan========")
def hitung_gaji_pokok(gaji_pokok, kehadiran):
    return gaji_pokok * kehadiran

def hitung_gaji_lembur(jam_lembur, tarif_lembur):
    return jam_lembur * tarif_lembur

def format_rupiah(total):
    return "Rp {:,.2f}".format(total).replace(",", ".")

def main():
    # Input data
    gaji_pokok = float(input("Masukkan gaji pokok karyawan per hari: "))
    kehadiran = int(input("Masukkan jumlah kehadiran kerja dalam sebulan: "))
    jam_lembur_per_hari = float(input("Masukkan jumlah jam lembur per hari: "))
    tarif_lembur = float(input("Masukkan tarif lembur per jam: "))

    # Hitung gaji pokok
    total_gaji_pokok = hitung_gaji_pokok(gaji_pokok, kehadiran)
    # Hitung total jam lembur dalam sebulan
    total_jam_lembur = kehadiran * jam_lembur_per_hari
    # Hitung gaji lembur
    total_gaji_lembur = hitung_gaji_lembur(total_jam_lembur, tarif_lembur)
    # Hitung total gaji
    total_gaji = total_gaji_pokok + total_gaji_lembur
    # Tampilkan total gaji dalam format rupiah
    total_gaji_rupiah = format_rupiah(total_gaji)
    print("Total gaji karyawan dalam sebulan: ", total_gaji_rupiah)
if __name__ == "__main__":
    main()


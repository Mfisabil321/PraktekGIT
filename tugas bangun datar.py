# Kelas dasar/ parent yang akan digunakan sebagai dasar untuk bangun datar
class BangunDatar:
    def hitung_luas(self):
        pass

# Kelas turunan untuk persegi
class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

# Kelas turunan untuk persegi panjang
class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

# Kelas turunan untuk segitiga
class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

# Kelas turunan untuk lingkaran
class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        return 3.14 * self.jari_jari ** 2

# Kelas turunan untuk trapesium
class Trapesium(BangunDatar):
    def __init__(self, sisi_atas, sisi_bawah, tinggi):
        self.sisi_atas = sisi_atas
        self.sisi_bawah = sisi_bawah
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * (self.sisi_atas + self.sisi_bawah) * self.tinggi


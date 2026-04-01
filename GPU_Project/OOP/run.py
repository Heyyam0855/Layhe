import random
class CV:
    def __init__(self, ad, soyad, yas,tehsil, bacariqlar):
        self.ad = f"{ad} {soyad}"
        self.yas=yas
        self.tehsil = tehsil
        self.bacariqlar = bacariqlar

    def sade_cv(self):
        print( f"Ad: {self.ad}, Yaş: {self.yas}, Təhsil: {self.tehsil}, Bacarıqlar: {', '.join(self.bacariqlar)}")
    def detalli_cv(self):
        #  Daha seliqli formatda CV təqdim edir.return yox print istifade et bacariqlari daha ferqli goster
        print(f"Ad: {self.ad}")
        print(f"Yaş: {self.yas}")
        print(f"Təhsil: {self.tehsil}")
        print("Bacarıqlar:")
        for bacariq in self.bacariqlar:
            print(f"- {bacariq}")

class Yemek:
    def __init__(self, ad, qiymet, tərkib,kategoriya="Yemək"):
        self.ad = ad
        self.qiymet = qiymet
        self.tərkib = tərkib
        self.kategoriya = kategoriya

    def yemeyi_goster(self):
        print(f"Yemək: {self.ad}, Qiymət: {self.qiymet} AZN, Tərkib: {', '.join(self.tərkib)}, Kategoriya: {self.kategoriya}")

    def yemek_kateqoriyasini_deyis(self, yeni_kateqoriya):
        self.kategoriya = yeni_kateqoriya
        print(f"Yeməyin kateqoriyası '{self.ad}' üçün '{yeni_kateqoriya}' olaraq dəyişdirildi.")
    def qiymeti_deyis(self, yeni_qiymet):
        self.qiymet = yeni_qiymet
        print(f"Yeməyin qiyməti '{self.ad}' üçün '{yeni_qiymet} AZN' olaraq dəyişdirildi.")
    def tərkibi_deyis(self, yeni_tərkib):
        self.tərkib = yeni_tərkib
        print(f"Yeməyin tərkibi '{self.ad}' üçün '{', '.join(yeni_tərkib)}' olaraq dəyişdirildi.")
    def adini_deyis(self, yeni_ad):
        self.ad = yeni_ad
        print(f"Yeməyin adı '{self.ad}' olaraq dəyişdirildi.")

class Musteri:
    def __init__(self, ad, soyad, yas, telefon):
        self.no= random.randint(1, 9999)
        self.ad = f"{ad} {soyad}"
        self.yas = yas
        self.telefon = telefon

    def musterini_goster(self):
        print(f"No: {self.no}")
        print(f"Ad: {self.ad}")
        print(f"Yaş: {self.yas}")
        print(f"Telefon: {self.telefon}")

    def musteriye_mesaj_gonder(self, mesaj):
        print(f"{self.ad} üçün mesaj: {mesaj}")

    def musterinin_telefonunu_deyis(self, yeni_telefon):
        self.telefon = yeni_telefon
        print(f"{self.ad} üçün telefon nömrəsi '{yeni_telefon}' olaraq dəyişdirildi.")

samir= Musteri("Samir", "Huseynov", 30, "0501234567")
memmed= Musteri("Memmed", "Aliyev", 25, "0507654321")
xeyyam= Musteri("Xeyyam", "Quliyev", 28, "0509876543")

samir.musterini_goster()
memmed.musterini_goster()
xeyyam.musterini_goster()
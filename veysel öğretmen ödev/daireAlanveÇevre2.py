# Biraz araştırma ile yaptığım ödev
import math

# sayı dışında bir veri geldiğinde program hata vermesin diye while döngüsü kullandım
while True:
    # kullanıcıdan aldığım veriyi değişkene atadım
    r = input("Lütfen dairenin cm cinsinden yarıçapını giriniz.")
    # eğer bir sayı ise döngüden çıkmasını sağladım böylece en alttaki print fonksiyonlarına geçecek
    if r == "q":
        break
    # eğer bir sayı değilse burada h değişkenini floata çeviriyor
    try:
        r = float(r)
        break
    # floata çevirirken hata verirse exept komutu devreye giriyor ve ekrana sayı girmemiz
    # gerektiği ile ilgili bir uyarı geliyor
    except:
        print("Lütfen bir sayı giriniz.")
    # uyarıyı verdikten sonra while döngüsünden dolayı işleme baştan başlıyor

print("Dairenin alanı: ", math.pi*r**2, "cm²dir.")
print("Dairenin çevresi: ", 2*math.pi*r, "cm'dir.")

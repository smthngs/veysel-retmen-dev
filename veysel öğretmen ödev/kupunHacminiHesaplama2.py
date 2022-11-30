# Biraz araştırma ile yaptığım ödev

# sayı dışında bir veri geldiğinde program hata vermesin diye while döngüsü kullandım
while True:
    # kullanıcıdan aldığım veriyi değişkene atadım
    h = input("Lütfen küpün kenar cm cinsinden uzunluğunu giriniz.")
    # eğer bir sayı ise döngüden çıkmasını sağladım böylece en alttaki print fonksiyonlarına geçecek
    if h == "q":
        break
    # eğer bir sayı değilse burada h değişkenini floata çeviriyor
    try:
        h = float(h)
        break
    # floata çevirirken hata verirse exept komutu devreye giriyor ve ekrana sayı girmemiz
    # gerektiği ile ilgili bir uyarı geliyor
    except:
        print("Lütfen bir sayı giriniz.")
    # uyarıyı verdikten sonra while döngüsünden dolayı işleme baştan başlıyor

print("Küpün hacmi = ", h ** 3, "cm³dir.")
print("Küpün yüzey alanı = ", 6 * h ** 2, "cm²dir.")

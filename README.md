# E-posta Kontrolü

Bu proje hakkında Türkçe ve İngilizce dillerinde bilgi alabilirsiniz.

- [Türkçe Dokümantasyon (Varsayılan)](README.md)
- [English Documentation](README_EN.md)

## Açıklama

Bu Python programı, e-posta hesaplarınızı kontrol eder ve  en son e-postanın içeriğini yazdırır.

## Özellikler

- IMAP kullanarak bir e-posta hesabına bağlanır.
- En son gönderilen e-postayı yazdırır.
- Verimlilik için asenkron işlemleri destekler.

## Gereksinimler

- Python 3.7+
- `imaplib`, `email`, `asyncio`, `pickle` (Standart Python kütüphaneleri)

## Kurulum

1. **Depoyu Klonlayın**

    ```bash
    git clone https://github.com/emi-ran/MailReceiver.git
    ```

2. **Proje Dizine Geçin**

    ```bash
    cd MailReceiver
    ```

3. **Bağımlılıkları Kurun**

    Bu proje herhangi bir dış bağımlılık gerektirmemektedir.

4. **E-posta Kimlik Bilgileri Dosyası Oluşturun**

    Aşağıdaki formatta e-posta kimlik bilgileri içeren bir `mails.txt` dosyası oluşturun:

    ```plaintext
    email@example.com:password
    anotheremail@example.com:anotherpassword
    ```

5. **Programı Çalıştırın**

    ```bash
    python main.py
    ```

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakınız.

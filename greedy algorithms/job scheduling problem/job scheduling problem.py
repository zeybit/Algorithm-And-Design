def greedy_job_scheduling(I):
    # İş listesini artan sırayla sırala
    I.sort()  # İş listesini artan sırayla sırala

    # Sıralı düzende işleri gerçekleştir
    while I:
        x = I[0]  # İş listesinin ilk elemanını seç
        del I[0]  # İlk işi listeden çıkar
        # İşi gerçekleştir
        print("Performs the job", x)  # Burada işin gerçekleştirilme işlemi tanımlanmalı
        # İşlemi gerçekleştirmek için iş fonksiyonunuzu veya iş kodunuzu burada çağırabilirsiniz

# Örnek iş listesi
I = [3, 1, 4, 2]  # İş listesi örnek olarak verildi, işlerin sürelerini temsil ediyor

# Greedy Job Scheduling Algorithm'ı çağır
greedy_job_scheduling(I)

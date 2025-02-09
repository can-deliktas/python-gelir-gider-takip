def tavsiye_ver(kalan_bakiye):
    """Kalan bakiyeye göre finansal öneriler verir."""
    if kalan_bakiye < 0:
        return (
            "Dikkat! Giderleriniz, gelirinizden fazla.\n"
            "Hemen gereksiz harcamaları azaltmayı düşünün ve tasarruf etmeye başlayın.\n"
            "Borçlarınızı kapatmak için bütçe yapmalısınız."
        )
    
    elif kalan_bakiye == 0:
        return (
            "Şu an gelir ve gideriniz dengede, ancak hiçbir birikiminiz yok.\n"
            "Beklenmedik durumlar için acil birikim yapmayı düşünmelisiniz."
        )

    elif kalan_bakiye < 5000:
        return (
            "Bakiyeniz pozitif, ancak düşük seviyede.\n"
            "Aylık giderlerinizin altında bir acil durum fonu oluşturmayı düşünebilirsiniz."
        )
    
    elif 5000 <= kalan_bakiye < 20000:
        return (
            "Güzel! Birikim yapmaya başlayabilirsiniz.\n"
            "Gelirinizin %10'unu yatırıma ayırarak finansal güvenliğinizi artırabilirsiniz."
        )

    elif 20000 <= kalan_bakiye < 50000:
        return (
            "Mali durumunuz oldukça iyi! \n"
            "Daha büyük yatırımlara yönelmek için hisse senetleri, tahviller veya yatırım fonları düşünebilirsiniz."
        )

    else:
        return (
            "Harika! Güçlü bir finansal seviyeniz var.\n"
            "Riskinizi çeşitlendirmek için farklı yatırım araçlarına yönelebilir veya pasif gelir kaynakları oluşturabilirsiniz."
        )

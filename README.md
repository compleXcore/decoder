# decoder
Staj da hash şifreleme metodunu anlattılar. Ve bana da buna benzer bir decoder yapmam söylendi. Ben de çok ama çok amatörce bir program yazdım. Test ettim çalışıyordu.

# Nasıl çalışıyor
Mantığı çok basit çünkü benim seviyemde ki bir kişiden maksimum bu çıkardı herhalde. Neyse önce şifreyi ters çeviriyor sonra ascii kodunun artı 1 haline dönüştürüyor. Sonra bu ascii kodlu halinin sayıları, benim belirlemiş olduğum özel karakterler ile yer değiştiriyor. Sonra bu özel karakterlerde gene benim belirlemiş olduğum karakterler ile yer değiştiriyor. Sonra bunları bir diziye aktarıyorum çünkü dizide yerlerini değiştiririm dedim. Fakat şifreyi çözmek için yaptığım programda fark ediyorum ki, aslında bu yer değiştirme mantığını yapamadım aklımdakini yada gereksiz oldu(büyük ihtimalle yapamadım aklımdakini). Sonra bunları diziden çıkarttım sonuna -xCore ekleyip bitirdim.

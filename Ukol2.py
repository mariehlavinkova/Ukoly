#stav skladu
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

produkt = input("Zadej kod soucastky: ")


if produkt in sklad:
    mnozstvi = input("Zadej mnozstvi soucastek: ")
    if int(mnozstvi) > sklad[produkt]:
        print (f'Na sklade mame pouze {sklad[produkt]} kusu.')
        sklad.pop(produkt)
    else: 
        print (f'Na sklade mame dostatecne mnozstvi')
        sklad[produkt] = sklad[produkt] - int(mnozstvi)
        print(sklad)



else: 
    print (f'Bohuzel, produkt {produkt} nemame skladem.')

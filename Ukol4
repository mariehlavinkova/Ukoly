def number_cor(number):

    """
    Returns True/False statement about correctly imported tel. number.
    """

    len_number = len(number)
    dial_code = str("+420")
    first_four_digits = number[:4]
    var = 0

    if first_four_digits == dial_code:

        if len_number == 13:
            var = True
        else:
            var = False

    else:

        if len_number == 9:
            var = True
        else:
            var = False

    return var

def sms_price(sms_text):

    """
    Returns price of the sms.
    """
    len_text = len(sms_text)
    price = 3
    char_num = 0

    for _ in range(len_text):
        char_num = char_num + 1
        if char_num == 180:
            price = price + 3
            char_num = 0

    return price

#Program pro odesílání sms.

cislo = input("Zadejte tel. cislo adresata: ")
number_crit = number_cor(cislo)

if number_crit == False:
    print("Zadane cislo neexistuje.")
else: 
    text_sms = input("Napiste text sms zpravy: ")
    cena = sms_price(text_sms)
    print(f"Odeslano. Cena vasi sms byla: {cena} CZK.")

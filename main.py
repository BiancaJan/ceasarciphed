def code(s:str,p:int):
    sifra=""
    for znak in s.upper():
        if znak.isalpha():
            znak_code = ord(znak)
            novy_znak_code = znak_code + p

            if novy_znak_code > 90:
                 novy_znak_code -= 26

            novy_znak = chr(novy_znak_code)
            sifra += novy_znak
        else:
            sifra += znak
    print(sifra)


code('Hello, World!', 7)

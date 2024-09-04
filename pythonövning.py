import math

# skriv ut information
print('KORVPAKETSKOLLEN')
print('----------------')
print('KOSTNAD 10kr')
print('KORVAR 5st')
print('----------------')

# hämta input
print('hur månag korvar')
print('behöver du?')
korvar = input('svar: ')
korvar = int(korvar)

# beräkna antal paket och kostnad
paket_antal = math.ceil(korvar / 5)
paket_kostnad = paket_antal * 10
print(paket_antal, paket_kostnad)

# skriv ut antal paket och kostnad
print('----------------')
print('PAKET:    ' + str(paket_antal))
print('KOSTNAD:      ' + str(paket_kostnad)+'kr')

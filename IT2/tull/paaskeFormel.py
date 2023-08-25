class ptyp:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(ptyp.HEADER + 'Lurer du på hvilken dato første påskedag faller på mellom to årstall?' + ptyp.END)

førsteÅr = input('Skriv inn det første årstallet: ')
sisteÅr = input('Skriv inn det siste årstallet: ')
try:
  førsteÅr = int(førsteÅr)
  sisteÅr = int(sisteÅr)
except ValueError:
  print(ptyp.FAIL + 'Du må skrive inn to heltall.' + ptyp.END)



def dato(år):
    a = år % 19
    b = år // 100
    c = år % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    n = (h + l - 7 * m + 114) // 31
    p = (h + l - 7 * m + 114) % 31
    print(f'Første påskedag {år} er den {p+1}/{n}')

for år in range(førsteÅr, sisteÅr+1):
    dato(år)
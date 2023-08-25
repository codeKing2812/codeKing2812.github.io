'''
class design:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(design.GREEN + 'Lurer du på hvilken dato første påskedag faller på mellom to årstall?' + design.END)

førsteÅr = input('Skriv inn det første årstallet: ')
sisteÅr = input('Skriv inn det siste årstallet: ')
try:
  førsteÅr = int(førsteÅr)
  sisteÅr = int(sisteÅr)
except ValueError:
  print(design.FAIL + 'Du må skrive inn to heltall.' + design.END)
'''


from timeit import timeit


orginal = '''
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

for år in range(1999, 2023+1):
    dato(år)

'''

forbedret = '''
for år in range(1999, 2023+1):
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

'''


orginal_tid:  float = timeit(stmt=orginal)
forbedret_tid: float = timeit(stmt=forbedret)

print(f"Orginal tid:  {round(orginal_tid, 4)} sekund.")
print(f"Forbedret tid: {round(forbedret_tid, 4)} sekund.")
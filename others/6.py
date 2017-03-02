import re

# Extract LRF/12
string1 = '''
Carlisle Farm Specialist F-1 Farm Tire - 12.5L-15 LRF/12 ply (Wheel Not Included)
'''

# Extract 205/50ZR16 OWL87
string2 = '''
Evergreen EU72 205/50ZR16 OWL87W RT-5 Truck tire 
'''

# Extract ST215/75R14 LRC
string3 = '''
Goodyear Marathon Trailer Tire w/Galvanized Rim ST215/75R14 LRC (5 Lug On 4.5)
'''

# Extract 265/35ZR18 97W XL
string4 = '''
1 X New Achilles "ATR Sport" 265/35ZR18 97W XL High Performance Tires 265/35/18
'''

# Extract ST235/85R16-14PR TL
string5 = '''
Set of 2 ZEEMAX Heavy Duty All Steel ST235/85R16-14PR TL Trailer Tire - 11073
'''

# Extract LT285/70R17/8 118Q BW
string6 = '''
1 X New Lexani LXHT-106 LT285/70R17/8 118Q BW All Season Performance SUV Tires
'''

# Extract LT245/75R16 120
string7 = '''
1 X New Nankang N889 Mudstar M/T LT245/75R16 120/116N E/10 Ply ROWL Mud Tires MT
'''

# Extract 130/90-16 2211500
string8 = '''
Pirelli Night Dragon Motorcycle Front Tire 130/90-16 2211500  
'''

strings = [string1, string2, string3, string4, string5, string6, string7, string8]


generic_re = '[A-Z]*\d*[/]\d+[A-Z]*\d*[-]?[/]?\d*\s?[/]?\d*[A-Z]*\s[A-Z]*[/]?\d*'

length = len(strings)

for i in range(length):
    extract_str = re.findall(generic_re, strings[i])
    print extract_str[0]

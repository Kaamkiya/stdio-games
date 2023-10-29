"""
Periodic table

teach the user about the Periodic Table of Elements
"""

import json
import requests

# fetch the json data
ELEMENTS = requests.get('https://api.dedolist.com/api/v1/science/periodic-table-detailed/')
ELEMENTS = json.loads(ELEMENTS.text)

ALL_STATS = ['name', 'number', 'atomic_mass', 'category', 'boil', 'density']
LONGEST_ROW = len('atomic_mass')

while True:
    print('''
                Periodic Table of Elements

    H                                                  He
    Li Be                               B  C  N  O  F  Ne
    Na Mg                               Al Si P  S  Cl Ar
    K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
    Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
    Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
    Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

            Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
            Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')

    print('\nEnter an element symbol to examine, or QUIT to quit.')

    # get the input, make it title case, and remove the whitespace
    response = input('> ').title().strip()

    if response == 'Quit':
        break # exit the program
    
    for i, element in enumerate(ELEMENTS):
        if element['symbol'] == response:
            for key in ALL_STATS:
                print(key.title().rjust(LONGEST_ROW) + ': ' + str(element[key]))
            input('Press Enter to continue...')

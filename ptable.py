import sys
elements = [
    "H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V",
    "Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge", "As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru",
    "Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy",
    "Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac",
    "Th","Pa","U","Np", "Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn",
    "Nh","Fl","Mc","Lv","Ts","Og"
    ]

word = (sys.argv[1]).replace(" ", "").lower()
wordLength = len(word)
elementsInWord = []

def createWord(word, arrElements, lengthElement):
    if wordLength == lengthElement:
        for l in arrElements:
            print(l,end=' | ')
        print()
        return

    firstLetter = word[0].upper()
    twoLetters = ""

    if len(word) > 1:
        twoLetters = firstLetter+word[1]

    if firstLetter in elements:
        arrElements.append(firstLetter)
        createWord(word[1:], arrElements, lengthElement+1)
        arrElements.pop()

    if twoLetters in elements:
        arrElements.append(twoLetters)
        createWord(word[2:], arrElements, lengthElement+2)
        arrElements.pop()

createWord(word, elementsInWord, len(elementsInWord))
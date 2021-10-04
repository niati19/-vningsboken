ålder = input("Mata in din ålder: ")

ålder = int(ålder)

if ålder > 18 and ålder < 100:
    print("Du är för gammal")
elif ålder < 18:
    print("Grattis du måste plugga")
elif ålder > 100:
    print("Hur är du vid liv?")

print("Hur lång:\n [1.] 160 cm\n [2.] 170 cm\n [3.] 180 cm\n [4.] 190+ cm")

svar = ""

svar = input("Välj längd 1-4: ")
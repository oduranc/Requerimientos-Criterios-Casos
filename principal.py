def principal():
    print("Welcome to Arabic2Roman Convertor!")

    ex = False
    while ex != True:
        print("")
        try:
            arabic = int(input("Please, give me an arabic number: "))
            if arabic < 1:
                print("Can't convert negative numbers into roman numerals. Please, try again.")
                #raise ValueError("Not an arabic number. Try again.")
                ex = False
            else:
                roman = convertToRoman(arabic)
                print(f"{arabic} = {roman}")
                opt = input("Do you want to convert another number? (y/n)")
                if opt != "y":
                    ex = True
        except:
            print("The given input is not an arabic number. Arabic numbers are natural numbers. Please, try again.")
            #raise ValueError("Not an arabic number. Try again.")
            ex = False

def convertToRoman(num):
    if num < 4000:
        return walkArray(num)
    else:
        i = 0
        while num >= 4000:
            num = num / 1000
            i += 1
        return walkArray(num) + "-"*i

def walkArray(num):
    result = ""
    romanDictionary = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    for arab, rom in romanDictionary.items():
        while arab <= num:
            num -= arab
            result += rom
    return result

principal()
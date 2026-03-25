import string

"""
    SIMPLE TOOL FOR HEX UTILITY
"""


def hexInfo(hex_string):
    
    
    if len(hex_string) % 2 != 0:
        hex_string = "0" + hex_string
    integer_value= int(hex_string,16)
    byteNum =  bytes.fromhex(hex_string)

    
    print(f"[+]Decimal value: {integer_value}")
    print(f"[+]Bytes: {byteNum}")
    print(f"[+] Byte length: {len(byteNum)}")
    print(f"[+]Little Endian: {int.from_bytes( byteNum, "little")}")
    print(f"[+]Big Endian: {int.from_bytes(byteNum, "big")}")
    print(f"[+]Binary: {' '.join(format(b, '08b') for b in byteNum)}")
    
    #checks readability
    try:
        asciiVal = byteNum.decode('utf-8')
        if all(32 <= b <= 126 for b in byteNum): print(f"[+] ASCII readable: {asciiVal}")
        else:
            print("[+] ASCII: non-printable")
    except:
            print("[+] ASCII: cannot decode")
    
def isHex(s):
    return all(c in string.hexdigits for c in s)
    
def main():
    
    
        while True:
            hexString= input("enter the hex string: ")
            hexString = hexString.replace("0x", "").replace(" ", "").lower()
            if(isHex(hexString)):
                hexInfo(hexString)
                break
            else:
                print("[-] Invalid, try again")
        
    
    
if __name__ == "__main__":
    main()      
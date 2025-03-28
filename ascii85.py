#!/usr/bin/env python3
import sys
import sysconfig
import base64


def handle_input(inp): 
    args = sys.argv
    if '-d' in args: 
        return decode(inp) 
    else: 
        return encode(inp) 


def encode(string):
    hexes = [hex(i) for i in bytearray(string.encode())]
    
    while len(hexes) % 4 != 0: 
        hexes.append('0x00')
        
    bytes5 = [] 
    for i in range(0, len(hexes), 4): 
        word = '0x'
        for j in range(4): 
            word += hexes[i + j][2:] 
        bytes5.append(word) 
        
    encoded_string = ""
    for t in bytes5:
     x = int(t,16)
     N0 = int((x / 85**4) % 85) + 33
     N1 = int((x / 85**3) % 85) + 33
     N2 = int((x / 85**2) % 85) + 33
     N3 = int((x / 85) % 85) + 33
     N4 = int(x % 85) + 33
     
     d = [N0,N1,N2,N3,N4]
     estring = "".join(chr(i) for i in d)
     encoded_string+= estring
     
    
    return encoded_string
    
    
def decode(encoded_string):
    p = [ord(i) - 33 for i in encoded_string]
    r = ""
    while len(encoded_string) % 5 != 0: 
        encoded_string += 'u'
    for i in range(0, len(p),5):
     pp = p[i:i+5]
     f = sum(pp[4 - i] * (85**i) for i in range(0,5))
     w = hex(f)
     m = w[2:]
     r+= bytearray.fromhex(m).decode()
    r.split("\x00")[0]
    
    return r
    

if name == "main": 
    input_string = "".join(sys.stdin.readlines())
    try: 
        print(handle_input(input_string.strip())) 
    except Exception as e: 
        print('Error: invalid string for decoding') 
        sys.exit(1)

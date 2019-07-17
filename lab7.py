#------------------------------------------------------------------------------
# Jeff Hejna
# 10/13/14
# This program encodes a message inputed by the user and then decodes it back.
#
#                      Algorithm
#         1) Have the user input phrase and number to shift phrase
#         2) Encode and print new phrase
#         3) Decode and print phrase
#
#-------------------------------------------------------------------------------





def printEncoding(astring,numshift):
    print("Encoded:")
    encodedString=""
    for x in astring:
        newChar=chr(ord(x)+numshift)   #creates new encoded character for each character in string
        encodedString=encodedString+newChar  #creates the new encoded phrase
    return encodedString

def printDecoding(encodedstring,numshift):
    print("Decoded:")
    decodedString=""
    for x in encodedstring:
        newChar=chr(ord(x)-numshift) #turns encoded character back to origianl character
        decodedString=decodedString+newChar #creates the decoded phrase
    return decodedString    

def main():
    String=input("What would you like to encode?: ")
    Shift=int(input("Pick a number: "))
    encoded=printEncoding(String,Shift)
    print(encoded)
    decoded = printDecoding(encoded,Shift)
    print(decoded)

main()    

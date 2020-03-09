'''

Name    :   Sai Krishna Uddagiri
Email   :   suddagir@uncc.edu
ID      :   801167439

'''

#importing required modules
import sys,struct,os

#Fetching the arguments from command line
if len(sys.argv) == 3:
    INPUT_FILE_NAME = str(sys.argv[1])
    BIT_LENGTH = int(sys.argv[2])
else:
    sys.exit("Invalid number of arguments!")


#Initializing the ASCII Table ( Character : ASCIIValue pairs )
END_POINTER = 256
TABLE = {chr(i):i for i in range(END_POINTER)}

#Function to write the zoutput(list) to a file in 16bit format
def writeToFile(OUTPUT):
    ''' Takes a LIST of strings as argument and writes to a file in 16 bit UTF-16BE Unsigned Short encoded format'''
    global INPUT_FILE_NAME
    OUTPUT_FILE_NAME = str(INPUT_FILE_NAME).split(".")[0] + '.lzw'
    #Opening the file handle to write in bytes (wb)
    OUTPUT_FILE = open(OUTPUT_FILE_NAME, "wb")
    for ENCODED_DATA in OUTPUT:
        # '>H' represents UTF-16BE for unsigned short(16 Bit)
        s = struct.Struct('>H')
        #Packing the data in 16bit and writing to the file
        OUTPUT_FILE.write(s.pack(int(ENCODED_DATA)))

#LZW Encoder Function
def LZWEncoder(INPUT_FILE_NAME, BIT_LENGTH):
    ''' Takes Input File Name and Bit Length as arguments and returns a list of Encoded Data '''
    global TABLE, END_POINTER
    STRING = ''

    #Getting the current working directory
    currentpath = os.getcwd()
    
    #setting the filelocation
    filelocation = str(currentpath)+"/"+INPUT_FILE_NAME
    
    #Checking if the file exists or not in the current directory
    if os.path.exists(filelocation):
        #If file exists, the data in the file is read and 
        f = open(INPUT_FILE_NAME)
        DATA = f.read()
        f.close()
    else:
        #If file does not exist, exit the program
        sys.exit("File does not exist!") 
    #Initializing maximum table size
    MAX_TABLE_SIZE = 2 ** (BIT_LENGTH)
    #Initializing a list to store the LZW Encoded output
    OUTPUT = []

    #LZW Encoding Algorithm starts here*****************
    for SYMBOL in DATA:
        if(STRING+SYMBOL) in TABLE:
            STRING += SYMBOL
        else:
            OUTPUT.append(TABLE[STRING])
            if(len(TABLE)<=MAX_TABLE_SIZE):
                TABLE[STRING + SYMBOL] = END_POINTER
                END_POINTER +=1
            STRING = SYMBOL
    if STRING in TABLE:
        OUTPUT.append(TABLE[STRING])
    #LZW Encoding ALgorithm ends here*******************

    #Returning the output list containing encoded output
    return OUTPUT

#The LZW Compression
writeToFile(
    #Passing the LZWEncoder() function's return value as an argument to writeToFile()
    LZWEncoder(
        #Passing the input file name and bit length as an argument to LZWEncoder() function
        INPUT_FILE_NAME, 
        BIT_LENGTH
        )
    )


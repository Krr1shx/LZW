'''

Name    :   Sai Krishna Uddagiri
Email   :   suddagir@uncc.edu
ID      :   801167439

'''

#importing required modules
import sys,struct,os,collections

#Fetching the arguments from command line
if len(sys.argv) == 3:
    INPUT_FILE_NAME = str(sys.argv[1])
    BIT_LENGTH = int(sys.argv[2])
else:
    sys.exit("Invalid number of arguments!")          


#Initializing the ASCII Table ( ASCIIValue : Character pairs )
END_POINTER = 256
TABLE = {i:chr(i) for i in range(END_POINTER)}


#Function to read the input file
def readFromFile(INPUT_FILE_NAME):
    ''' Reading input from the file and unpacking it '''
    
    #Getting the current working directory
    currentpath = os.getcwd()
    
    #setting the filelocation
    filelocation = str(currentpath)+"/"+INPUT_FILE_NAME
    
    #We read 2 bytes each iteration.
    buffersize = 2
    
    #The encoded data is in 16 bit format. Set the format to ">H" which is UTF-16BE for Unsigned Short
    s=struct.Struct(">H")

    #A List to store the data from File
    readData = []
    #Checking if the file exists or not in the current directory
    if os.path.exists(filelocation):
        #Opening a file handle
        INPUT_FILE = open(filelocation,"rb")
        #Infinite loop to read the bytes from the file.
        while True:
            buffer = INPUT_FILE.read(buffersize)
            #Exiting the loop when al data is read
            if len(buffer) != buffersize:
                break
            #Unpacking the buffer read.
            bufferData = s.unpack(buffer)[0]
            #Saving the bufferData unpacked to a list
            readData.append(bufferData)
    else:
        #If file does not exist, exit the program
        sys.exit("File does not exist!")
    INPUT_FILE.close()
    #Returning the list containing the data that is read
    return readData

#LZW Decoding function
def LZWDecoder(readData, BIT_LENGTH):
    ''' Takes the unpacked data from the file and decodes it and saves to a file '''
    global END_POINTER,TABLE
    #Initializing the maximum table size 
    MAX_TABLE_SIZE = 2 ** int(BIT_LENGTH)
    OUTPUT=[]
    #Converting the list to a double ended queue for pop operations to get the next symbol
    encodedData = collections.deque(readData)
    
    #LZW Decoding Algorithm starts here
    OLD = encodedData.popleft()
    OUTPUT.append(TABLE[OLD])
    while ( len(encodedData) > 0):
        NEW = encodedData.popleft()
        if NEW not in TABLE.keys():
            S=TABLE[OLD]
            S=S+S[0]
        else:
            S=TABLE[NEW]
        OUTPUT.append(S)
        if(len(TABLE)<MAX_TABLE_SIZE):
            TABLE[int(END_POINTER)]=TABLE[OLD]+S[0]
            END_POINTER+=1
        OLD=NEW
    #LZW Decoding Algorithm ends here

    #Returning the decoded output
    return OUTPUT

#Function to write the decoded output to file
def writeToFile(OUTPUT):
    ''' Takes decoded data and writes to a text file '''
    global INPUT_FILE_NAME
    #Initializing the output file name
    OUTPUT_FILE_NAME = INPUT_FILE_NAME.split('.')[0] + '_decoded.txt'
    #Opening the file handle to write
    OUTPUT_FILE = open(OUTPUT_FILE_NAME,"w")
    for DATA in OUTPUT:
        OUTPUT_FILE.write(DATA)
    OUTPUT_FILE.close()

#The LZW Decompression 
writeToFile(
    #Passing the Decoded data from LZWDecoder() as an argument to writeToFile()
    LZWDecoder(
        #Passing readFromFile() and Bit Length to LZW Encoder
        readFromFile(
            #Passing Input file name to read the data
            INPUT_FILE_NAME
            ),
        BIT_LENGTH
        )
    )
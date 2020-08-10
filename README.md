___
***Name*** : *Sai Krishna Uddagiri*    
***ID***: *801167439*  
***Email***: *suddagir@uncc.edu*  
***Language***	: *Python 3.6.0*  
***Operating System***: *Windows 10 64-Bit*
___

# Lempel-Ziv-Welch Algorithm:

LZW Algorithm is a lossless data compression adaptive algorithm that does not assume prior knowledge of input data distribution. This algorithm is best when the data is large and redundant. LZW Compression is mostly used for GIF image formats and TIFF image formats and PDF formats. The algorithm involves two steps. Uncompressed data takes a lot of space, so LZW compression can be used to compress the data and decrease its size.


1. Encoding/ Compressing
2. Decoding/ Decompressing



## Encoding/Compressing:

The algorithm reads an input sequence of symbols, grouping the symbols into strings, and converting the strings into codes. LZW Compression uses a code table, which consists of codes ranging from 0 to 255 and their ASCII characters. When the encoding begins, the table consists of 256 entries. It then reads symbols from the sequence and appends then one by one to the current string. Each time it reads the next symbol, it checks whether the resulting string has a code in the dictionary. If the code exists, it reads the next symbol from the sequence and appends to the current string and repeats the process. If the code does not exist, it means that a new code is found. This code is then added to the table and assigned the next value(which is the last value in the table incremented by one), and then outputs the code corresponding to the string without the newest symbol and resets the current string to the newest symbol and the process continues until the last string. The algorithm then outputs the code for the remaining string. LZW adaptively builds the dictionary based on the input sequence.

### Usage (Encoding/Compressing):
**File**		: LZW_Encoding.py  
**Requirements**	: Python Environment Version 3.6.0 (Minimum)

### Instructions:
1. Open command prompt.
2. Navigate to directory where the "LZW_Encoding.py" file and the input file is present. 
>**Note :** The "LZW_Encoding.py" file and the input file should be in the same directory
3. To start the encoding algorithm, run the following command:
```
python LZW_Encoding.py <INPUT_FILE_NAME> <BIT_LENGTH>
``` 

### Example (Encoding/Compressing):
**Input File**	: input.txt  
**Number of bits**	: 16  
To compress the above file, run the following command:  
```
python LZW_Encoding.py input.txt 16
```   

Once the above command is executed, a new file "input.lzw" is generated with the compressed data of input.txt file.



## Decoding/Decompressing:

Decoding works in the reverse way of encoding. In this process, the integer codes are converted into strings. No prior information is needed in this decoding process. A TABLE similar to the TABLE created in the encoding process is created. The decoder first reads the input code from the encoded sequence of integers. It then looks up the code in the TABLE and outputs the string associated with it. Then, the decoder reads in a new code from the encoded sequence and outputs it if in the table and the first character of this new string is concatenated to the old string and the resulting string is added to the dictionary with value equals the last value incremented by one. The decoded new string then becomes the previous string and the process repeats.

### Usage (Decoding/Decompressing):
**File:**		: LZW_Decoding.py  
**Requirements**	: Python Environment Version 3.6.0 (Minimum)  

### Instructions:
1. Open command prompt.
2. Navigate to directory where the "LZW_Decoding.py" file and the file(.lzw extension) to be decoded is present. 
>Note: The "LZW_Decoding.py" file and the .lzw file should be in the same directory
3. To start the Decoding algorithm, run the following command:
```
python LZW_Decoding.py <INPUT_FILE_NAME> <BIT_LENGTH>
```


### Example (Decoding/Decompressing):
Input File	: input.lzw   
Number of bits	: 16   
To decompress the above file, run the following command:   
```
python LZW_Decoding.py input.lzw 16
```

Once the above command is executed, a new file "input_decoded.txt" is generated with the decompressed data of input.lzw file.



## Test Cases:

| TEST CASE | INPUT  | RESULT  | INFORMATION  |  
|--|--|--|--|
| Input file **input.txt** is present in the current directory. | input.txt 16 | PASS | **input.lzw** file is created.  |
| Input file **input.txt** is not present in the current directory. | input.txt 16 | FAIL | Program terminates with error ***File does not exist!*** . |
| Only one argument is provided. | input.txt | FAIL | Program terminates with error ***Invalid number of arguments!***  |
| **3** arguments are provided. | input.txt 16 17 | FAIL | Program terminates with error ***Invalid number of arguments!***  |
| Invalid file format provided for Encoding. Assume **input.lzw** exists in the current directory. | input.lzw 16 | FAIL | Program terminates with ***UnicodeDecodeError***. |
| Invalid file format provided for Decoding. Assume **input.txt** exists in the current directory. | input.txt 16 | FAIL | Program terminates with ***KeyError*** |

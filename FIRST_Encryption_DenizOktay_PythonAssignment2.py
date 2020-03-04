# This program can be used for to encrypt text files.
# This technique is called Caesar Cipher.It is a type of substitution
#cipher in which each letter in the plaintext is 'shifted' a certain 
#number of places down the alphabet.
#In this program this number is 1.
#With a shift of 1, A would be replaced by B, B would become C,and so on.

from easygui import *

title = "Encryption"

lineslist = []

#Create a new list for to store the modifications.
newlineslist = []

inputfile=open('encryptionInputText.txt')
outputfile=open('encryptionOutputText.txt','w')


for line in inputfile:
	Newstring=""
	for character in line :
		if character=='Z':
			#Z is the last letter. So we can't shift ONE place down the alphabet.
			#So we will replace it with by A.
			Newstring = Newstring + "A"
		elif character=='z':
			#z is the last letter. So we can't shift ONE place down the alphabet.
			#So we will replace it with by a.
			Newstring = Newstring + "a"
		#Each character has a number from 0 to 65,535.
		#The number value for each character is defined by an international 
		#standard called Unicode.
		#In this program I used Unicode value of 'a','z','A','Z'
		#The symbol for the letter A is represented by character number 65.
		#The symbol for the letter Z is represented by character number 90.
		#The symbol for the letter a is represented by character number 97.
		#The symbol for the letter z is represented by character number 122.

		elif (ord(character)>=65 and ord(character)<90) or (ord(character)>=97 and ord(character)<122):
			#By add 1 we will shift ONE place down the alphabet.
			x=ord(character)+1
			y=chr(x)
			Newstring = Newstring + y
		else:
			Newstring = Newstring + character
#I added each line of the input file to a list.
	lineslist.append(line)
	lineslist = [item.strip() for item in lineslist]

#I added new lines which we created above to another list.	
	newlineslist.append(Newstring)
	newlineslist = [item.strip() for item in newlineslist]

#I convert this two lists to strings.So I will be able to display them by using EasyGui.
	Oldlines=""
	for item in lineslist:
		Oldlines= Oldlines+ item +"\n"
	Newlines=""
	for item in newlineslist:
		Newlines= Newlines+ item +"\n"

while True:
	#Output which explains the purpose of the program
	msgbox("This program can be used for to encrypt text files.It uses an encryption technique in which each letter in the plaintext is 'shifted' ONE place down the alphabet.", title)
	choice = ccbox("Do you want to encrypte 'encryptionInputText.txt' file? ", title)
	if choice == 0:
		break
	#File Output
	outputfile.write(Newlines)
	
	#Information about input file.
	msgbox("Content of Input File:\n"+Oldlines, title)
	
	#Information about output file.	
	msgbox("It has encrypted!\nOutput file is 'encryptionOutputText.txt'.\nContent of Output File:\n"+Newlines, title)
	break
msgbox("Finished!", title)




outputfile.close()
inputfile.close()

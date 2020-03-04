# AFTER encrypt the file WITH FIRST_Encryption_DenizOktay_PythonAssignment2.py
# This program can be used for to decrypt text files.

#With a shift of 1, B would be replaced by A, C would become B,and so on.

from easygui import *

title = "Decryption"

lineslist = []

#Create a new list for to store the modifications.
newlineslist = []

inputfile=open('encryptionOutputText.txt')
outputfile=open('decryptionOutputText.txt','w')


for line in inputfile:
	Newstring=""
	for character in line :
		if character=='A':
			#A is the first letter. So we can't shift ONE place up the alphabet.
			#So we will replace it with by Z.
			Newstring = Newstring + "Z"
		elif character=='a':
			#a is the first letter. So we can't shift ONE place up the alphabet.
			#So we will replace it with by z.
			Newstring = Newstring + "z"
		#Each character has a number from 0 to 65,535.
		#The number value for each character is defined by an international 
		#standard called Unicode.
		#In this program I used Unicode value of 'a','z','A','Z'
		#The symbol for the letter A is represented by character number 65.
		#The symbol for the letter Z is represented by character number 90.
		#The symbol for the letter a is represented by character number 97.
		#The symbol for the letter z is represented by character number 122.

		elif (ord(character)>65 and ord(character)<=90) or (ord(character)>97 and ord(character)<=122):
			#By summation 1 we will shift ONE place up the alphabet.
			x=ord(character)-1
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
	msgbox("This program can be used for to decrypt text files.It uses an decryption technique in which each letter in the plaintext is 'shifted' ONE place up the alphabet.", title)
	choice = ccbox("Do you want to decrypte 'encryptionOutputText.txt' file? ", title)
	if choice == 0:
		break
	#File Output
	outputfile.write(Newlines)
	
	#Information about input file.
	msgbox("Content of Input File:\n"+Oldlines, title)
	
	#Information about output file.	
	msgbox("It has decrypted!\nOutput file is 'decryptionOutputText.txt'.\nContent of Output File:\n"+Newlines, title)
	break
msgbox("Finished!", title)




outputfile.close()
inputfile.close()


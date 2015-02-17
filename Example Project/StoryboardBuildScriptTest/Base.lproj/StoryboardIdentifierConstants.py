def determineIdentiferNameFromString(string):
	identiferName = ""
	for stringSection in string.split(" "):
	    if "identifier=" in stringSection:
	        identiferName = stringSection.split("=")[1].replace("\"", "")
	return identiferName

def stripOutIdentifierNames(arrayOfStrings):
	arrayOfIdentiferNames = []
	for string in arrayOfStrings:
		if "<segue" in string:
			if( determineIdentiferNameFromString(string) != "" ):
				arrayOfIdentiferNames.append( determineIdentiferNameFromString(string) )
	return arrayOfIdentiferNames

def identifierNamesToConstantCodeString(identifierNames):
	resultCodeString = ""
	for identifierName in identifierNames:
		resultCodeString = resultCodeString + "NSString * const k" + identifierName.title() + " = @\"" + identifierName + "\";\n"
	return resultCodeString

def storyboardNamesToConstantCodeString(storyboardNames):
	resultCodeString = ""
	for storyboardName in storyboardNames:
		resultCodeString = resultCodeString + "NSString * const k" + storyboardName.title() + "Storyboard = @\"" + storyboardName + "\";\n"
	return resultCodeString

def buildImplementationFileStringFromCodeBody(Bodystring):
	return "#import \"StoryboardIdentifiers.h\"\n\n" + Bodystring

def identifierNamesToExternConstantsString(identifierNames):
	resultCodeString = ""
	for identifierName in identifierNames:
		resultCodeString = resultCodeString + "extern NSString * const k" + identifierName.title() + ";\n"
	return resultCodeString

def storyboardNamesToExternConstantsString(storyboardNames):
	resultCodeString = ""
	for storyboardName in storyboardNames:
		resultCodeString = resultCodeString + "extern NSString * const k" + storyboardName.title() + "Storyboard;\n"
	return resultCodeString

def buildInterfaceFileStringFromCodeBody(Bodystring):
	return "#import <Foundation/Foundation.h>\n\n" + Bodystring

#--- script begin ---

import glob
storyboardFileNames = glob.glob("./*.storyboard")

strippedStoryboardNames = []

for storyboardFileName in storyboardFileNames:
    strippedName = storyboardFileName.split("/")[-1].replace(".storyboard","")
    strippedStoryboardNames.append(strippedName)

identifierNames = []

for storyboardName in storyboardFileNames:
	data = 0
	with open (storyboardName, "r") as myfile:
		data=myfile.readlines()

	identifierNames = identifierNames + stripOutIdentifierNames(data)

identifierNames = list(set(identifierNames))

codeBodyString =  storyboardNamesToConstantCodeString(strippedStoryboardNames) + "\n\n" + identifierNamesToConstantCodeString(identifierNames)
implementationFileString = buildImplementationFileStringFromCodeBody(codeBodyString)

with open('StoryboardIdentifiers.m', 'w+') as f:
    f.truncate()
    f.write(implementationFileString)
    f.close()

codeExternString = storyboardNamesToExternConstantsString(strippedStoryboardNames) + "\n\n" + identifierNamesToExternConstantsString(identifierNames)
interfaceFileString = buildInterfaceFileStringFromCodeBody(codeExternString)

with open('StoryboardIdentifiers.h', 'w+') as f:
    f.truncate()
    f.write(interfaceFileString)
    f.close()

print implementationFileString
print interfaceFileString


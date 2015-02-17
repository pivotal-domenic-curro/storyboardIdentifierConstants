# storyboardIdentifierConstants
A python script that can be added to Xcode's run script to generate storyboard identifier files that auto maintain a list of segue identifiers as k-constants.

#Installation
1. In the left bar in Xcode, select the folder icon.
1. Select the project file
1. In the top tab bar, select Build Phases
1. Select the + on the tab bar below the one containing Build Phases
1. Select New Run Script Phase
1. In the black command window input:

  `cd ./${TARGET_NAME}/Base.lproj`
  
  `pythonw storyboardIdentifierConstants.py`

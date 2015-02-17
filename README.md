# storyboardIdentifierConstants
A python script that can be added to Xcode's run script to generate storyboard identifier files that auto maintain a list of segue identifiers as k-constants.  This script works across multiple storyboards.

#Installation
1. In the left bar in Xcode, select the folder icon.
1. Select the project file
1. In the top tab bar, select Build Phases
1. Select the + on the tab bar below the one containing Build Phases
1. Select New Run Script Phase
1. In the black command window input:

  `cd ./${TARGET_NAME}/Base.lproj`
  
  `pythonw storyboardIdentifierConstants.py`

#Usage
Add the 'StoryboardIdentifiers' files to your project.  They will be located under Xcode/{Project name}/{Project name}/Base.lproj.  Do not 'Copy item if needed'.

Whenever a build is created, the files will be updated with the latest storyboard identifiers.

#Example Output
**StoryboardIdentifiers.h**

`#import <Foundation/Foundation.h>`

`@interface StoryboardIdentifiers : NSObject`

`extern NSString * const kMikemikemike;`

`extern NSString * const kAstoryboardidentifier;`

`@end`

**StoryboardIdentifiers.m**

`#import "StoryboardIdentifiers.h"`

`@implementation StoryboardIdentifiers`

`NSString * const kMikemikemike = @"mikemikemike";`

`NSString * const kAstoryboardidentifier = @"aStoryboardIdentifier";`

`@end`

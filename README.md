# String Exand

expand strings with groups for all the possible outcomes.
Groups are identified by the chars:
  {} for optional groups
  () for non-optional groups

Inside a group, we use the | char as a item separator.
The escape character is the \ character.

Example of use:

  from expand import expand 
  
  expand("hi{ there}!, (what is up|how are you doing)?")

Returns: ["hi there!, what is up?", "hi there!, how are you doing?",
          "hi!, what is up?", "hi!, how are you doing?"]

There is also a pprint() function that whould print a long sentence in multiple lines making it easier to understand.

Example:

  from pprint import pprint
  
  pprint("My (son in law|mother|dad|uncle|brother|sister|daughter) is sick")
  
Outputs:
   My (son in law|
       mother|
       dad|
       uncle|
       brother|
       sister|
       daughter) is sick
       


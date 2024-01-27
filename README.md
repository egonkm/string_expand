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
  
Output:
   My (son in law|
       mother|
       dad|
       uncle|
       brother|
       sister|
       daughter) is sick
       
       
# Add variables:

For expand, let's add the possibility of using a dictionary for variable substitution.
The value of a variable is a list of one or more strings that will be replaced by the variable name wherever we found it in the string.
We will use the $ character to identify a variable.

Example of use:

  from expand import expand
  
  v = { "hello" : ["Hello", "Hi there", "Morning"],
           "thanks" : ["Thank you!", "Thanks!", "Thanks a lot."] 
           }
           
  expand("$hello! Please follow the procedure. $thanks", v)
  
Returns:
  [ "Hello! Please follow the procedure. Thank you!", "Hi there! Please follow the procedure. Thank you!", ...]
  
  
  

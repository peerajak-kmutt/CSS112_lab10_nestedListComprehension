# Map Reduce any all 

## 1. Map Replace the word 'The', case insensitive, with 'xxx' from a text

atext="""The split method is used to split the strings and store them in the list. The built-in method returns a list of the words in the string, using the “delimiter” as the delimiter string. If a delimiter is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace."""

### The Answer is

anstext="""xxx split method is used to split xxx strings and store them in xxx list. xxx built-in method returns a list of xxx words in xxx string, using xxx “delimiter” as xxx delimiter string. If a delimiter is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and xxx result will contain no empty strings at xxx start or end if xxx string has leading or trailing whitespace."""

def Problem1():

    ltext = atext.split(" ")
    ####Your code here####
    #def replace_the_map
    ###########
    ####Your code here, rtext must be a list####
    #rtext = ?map?                             #
    ############################################
    
    # Check your rtext does not contain 'the'
    # if not any(map(lambda# Your code here
        return ' '.join(rtext)
    # else:
        return 'still exist the word the'


## 2. Reduce.  Replace the word 'The', case insensitive, with 'xxx' from a text

atext="""The split method is used to split the strings and store them in the list. The built-in method returns a list of the words in the string, using the “delimiter” as the delimiter string. If a delimiter is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace."""

### The Answer is

anstext="""xxx split method is used to split xxx strings and store them in xxx list. xxx built-in method returns a list of xxx words in xxx string, using xxx “delimiter” as xxx delimiter string. If a delimiter is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and xxx result will contain no empty strings at xxx start or end if xxx string has leading or trailing whitespace."""

def Problem2():

    ltext = atext.split(" ")

    ####Your code here####
    #def relace_the_reduce(
    #    return ??
    #####################
    ####Your code here###
    #anstext=reduce(
    #####################
    return anstext



'''
Zach Bogart
06/21/2019

Is Unique: Implement an algorithm to determine if a string
has all unique characters.
What if you cannot use additional data structures?
'''

'''
Notes:
- initial idea is to loop through array and add new characters
to a dictionary "seen". If the character is not in "seen",
add it. If it is already there, return false. If I get to the
end looking at my "seen" dictionary and don't see anything 
already there, return true.

Time should be O(n) since it must go through the entire string
Space should be O(n) since the dict size depends on the string size
'''

def is_unique(str):
    seen = {}
    for char in str:
        if char in seen:
            return False
        else:
            seen[char] = 1

    return True

'''
If I cannot use additional data structures, then
comparing every character would work
'''


'''
Solution made a good point that could store the entire alphabet as ASCII boolean.
This way the space complexity would be O(1) since it would no longer 
depend on the size of the string.
'''

def is_unique_improved(str):
    seen = [False] * 256 # extended ASCII, could be 128

    for char in str:
        if seen[ord(char)]:
            return False
        else:
            seen[ord(char)] = True
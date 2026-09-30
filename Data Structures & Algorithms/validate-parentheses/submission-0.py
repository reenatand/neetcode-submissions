class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #create a dictionary for mapings
        mapping = {'(': ')', '{': '}', '[': ']'}
        #looks at each character in the string
        for char in s:
            #if the character is in the mapping, then it will add it to the stack, this checks the keys of the dict 
            if char in mapping:
                #now if it is an open i.e. in the keys then add to the top of the list
                stack.append(char)
            #If the character is not in our dictionary's keys, then it is closing
            else:
                #if there is a closing that is not in the stack, then immediately we know it is wrong and we output false
                if not stack:
                    return False
                #back to closing, if it is the definition for the last key, matches the next one
                top_item = stack.pop()
                #We feed our popped opening bracket into the dictionary to see what its closer should be. We then compare that to the current char we are looking at.
                if mapping[top_item] != char:
                    return False
        return len(stack) == 0
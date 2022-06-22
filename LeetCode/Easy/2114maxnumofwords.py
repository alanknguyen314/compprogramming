"""
2114. Maximum Number of Words Found in Sentences

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.

"""
# 29 ms
# 13.8 MB
# 06/18/2022 20:28

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        num = 0
        maxlocal = 0
        test = []
        
        
        # I only take care of the number of spaces 
        # (because num of words = num of spaces + 1)
        
        for i in range(len(sentences)):
            num = sentences[i].count(" ") + 1
            test.append(num)
            maxlocal = max(test)
        
        return maxlocal
        
        
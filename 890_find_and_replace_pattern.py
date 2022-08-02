# 890. Find and Replace Pattern

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def word_to_index_list(word: str):
            wordd = dict()
            
            for i in range(len(word)):
                if wordd.get(word[i]) is None:
                    wordd[word[i]] = [i]
                else:
                    wordd[word[i]].append(i)
                    
            return list(wordd.values())
            
        if len(pattern) == 1:
            return words
        
        ret = []
        
        patternd = word_to_index_list(pattern)                
        for word in words:
            wordd = word_to_index_list(word)
            
            if patternd == wordd:
                ret.append(word)
                
        return ret
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        result = []
        
        for i in range(word_len):
            left = i
            right = i
            current_count = {}
            count = 0  
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    current_count[word] = current_count.get(word, 0) + 1
                    count += 1
                    
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    if count == num_words:
                        result.append(left)
                        
                else:
                    current_count.clear()
                    count = 0
                    left = right
        
        return result
            

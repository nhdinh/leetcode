# 1451. Rearrange Words in a Sentence

class Solution:
    def arrangeWords(self, text: str) -> str:
        if text.strip() == "":
            return text
        
        text = sorted(text.split(" "), key=lambda w: len(w))
        return " ".join(text).capitalize()
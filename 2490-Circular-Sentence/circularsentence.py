class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]: return False
        sentence_list = sentence.split(' ')
        for i in range(len(sentence_list)-1):
            if sentence_list[i][-1] != sentence_list[i+1][0]:
                return False
        return True

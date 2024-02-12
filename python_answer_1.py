# "write write write all the number from from from 1 to 100"


class DSIQ:
    def __init__(self) -> None:
        pass
    
    def evaluateHighestFreqWord(self,sentence) -> int:
        word_list = sentence.split(' ')
        tempDir = {} 
        for word in word_list:
            count = 1
            if word not in tempDir.keys():
                tempDir[word] = count
            else:
                tem_val = tempDir[word]
                tempDir[word] = tem_val+1
        maxFreqWord = max(zip(tempDir.values(), tempDir.keys()))[1]
        return len(maxFreqWord)

if __name__ == "__main__":
    cls_obj = DSIQ()
    sentence_list = [
            "write write write all the number from from from 1 to 100",
            "mohit is a student of mohit ineuron is a good place",
            "colony is the biggest place in colony place is today colony"
        ]
    for sentence in sentence_list:
        print('Sentence : ',sentence)
        print('Output : ',cls_obj.evaluateHighestFreqWord(sentence))

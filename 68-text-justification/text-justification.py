class Solution:
    # We can split  creating a line into two subtasks: determine which words should be on the line and take the workds from first task and create the line

    # getWords helper method basically returns the lis of words in that should be in line, starting at words[i]
    # we can use a while loop to add words to current_line until addding another word would violate the condition, we add + 1 to account for space for the next check
    def getWords(self, i, words, maxWidth): 
        current_line = []
        curr_length = 0

        while i < len(words) and curr_length + len(words[i]) <= maxWidth:
            current_line.append(words[i])
            curr_length += len(words[i]) + 1
            i += 1
        return current_line
    
    # createLine helper method basically converts it into a line of maxwidth using extra spaces to reach the length. Extra soaces should be distributed evenly. If not distributed evenly, add extra spaces to left. fianl line should have only one space btw the words
    def createLine(self, line, i, words, maxWidth):
        # -1 because the last word does not have any spaces after it
        base_length = -1 
        for word in line: 
            base_length += len(word) + 1
        extra_spaces = maxWidth - base_length

        # aline with only one string or last line
        if len(line) == 1 or i == len(words): 
            return " ".join(line) + " "*extra_spaces
        
        # -1 because the last word does not have any spaces after it
        word_count = len(line) - 1
        spaces_per_word = extra_spaces // word_count
        extra_spaces_needed = extra_spaces % word_count

        for j in range(extra_spaces_needed): 
            line[j] += " "
        for j in range(word_count): 
            line[j] += " " * spaces_per_word
        return " ".join(line)

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0 
        while i < len(words): 
            current_line = self.getWords(i, words, maxWidth)
            i += len(current_line)
            result_line = self.createLine(current_line, i, words, maxWidth)
            res.append(result_line)
        return res  
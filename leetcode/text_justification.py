class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        used = 0
        lines = []
        while used < len(words):
            line, used = self.pack_line(words, used, maxWidth)
            lines.append(line)
        return lines
    
    def pack_line(self, words, start, max_width):
        slen = -1
        wlen = 0
        wi = start
        while slen + len(words[wi]) + 1 <= max_width:
            slen += len(words[wi]) + 1
            wlen += len(words[wi])
            wi += 1
            if wi == len(words):
                return ' '.join(words[start:]).ljust(max_width), len(words)
        
        s = ''
        space_budget = max_width - wlen
        if wi - start > 1:
            normal_width, extra_space = divmod(space_budget, (wi - start) - 1)
        else:
            normal_width, extra_space = space_budget, 0
        for i in xrange(start, wi):
            space = ' ' * normal_width
            if extra_space:
                space += ' '
                extra_space -= 1
            s += words[i] + space
        return s[:max_width], wi
                

        
            
        

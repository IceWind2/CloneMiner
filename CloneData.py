class CloneData:
    def __init__(self, tokenArray) -> None:
        self.cloneClass = 0
        self.clones = {}
        self.tokens = tokenArray
        
    def add_clone_case(self, clone):
        for clnId, clnCases in self.clones.items():
            for idx in range(len(clnCases)):
                if (idx >= len(clone)):
                    continue
                
                if (clnCases[idx][0] <= clone[idx][0] and clnCases[idx][1] >= clone[idx][1]):
                    return
                
        self.clones[self.cloneClass] = clone.copy()
        self.cloneClass += 1
    
    def add_repeat_case(self, repeat):
        self.clones[self.cloneClass] = [[repeat[0], repeat[1]]]
        self.cloneClass += 1
            
    def __repr__(self):
        width = 55
        sep = 18
        
        repr = ('-' * width) + "\nClone Class Id" + (' ' * sep) + "Cases\n" + ('-' * width) + '\n'
        for cloneClass, cases in self.clones.items():
            for idx in range(len(cases)):
                if idx == len(cases) // 2:
                    ccstr = f'      {cloneClass}'
                    repr += ccstr + (' ' * (sep - len(ccstr)))
                else:
                    repr += ' ' * sep
                    
                repr += (f'Line {self.tokens[cases[idx][0]].raw.line} Col {self.tokens[cases[idx][0]].raw.column + 1} ... '
                         f'Line {self.tokens[cases[idx][1]].raw.line} Col {self.tokens[cases[idx][1]].raw.column + len(self.tokens[cases[idx][1]].txt) + 1}\n')
            
            repr += '-' * width + '\n'
                
        return repr
import TextDuplicateSearch as tds

if __name__ == '__main__':
    fin = "text.txt"
    fout = "res.txt"
    tds.enable_token_classes()
    tds.find_clones(fin, 3, fout)

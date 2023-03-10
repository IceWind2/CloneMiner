import TextDuplicateSearch as tds
from TextDuplicateSearch.DataModels.SearchConfig import SearchConfig

if __name__ == '__main__':
    cfg = SearchConfig(input_file="text.txt", output_file="res.txt", min_dup_length=3)
    tds.find_clones(cfg)

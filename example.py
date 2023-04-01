import TextDuplicateSearch as tds

if __name__ == '__main__':
    cfg = tds.create_config()
    cfg.input_file = "text.txt"
    cfg.output_file = "output.txt"

    tds.strict_search(cfg)

import cProfile
import pstats
from pstats import SortKey
import TextDuplicateSearch as tds


def main():
    cfg = tds.create_config()
    cfg.input_file = "text.txt"
    cfg.output_file = "output.txt"
    cfg.min_dup_length = 10
    tds.strict_search(cfg)


prof = cProfile.Profile()
prof.run('main()')

stats = pstats.Stats(prof).strip_dirs().sort_stats(SortKey.CUMULATIVE)
stats.print_stats(20)

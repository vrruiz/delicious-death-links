#!/usr/bin/env python
from datetime import datetime

def main():
    output = open('delicious-status.txt')
    year = 0
    stats = [] # 2004...2012
    year_stats = [] # [alive, bad requests]
    for bookmark in output.readlines():
        (timestamp, title, status) = bookmark[:-1].split('\t')
        date = datetime.fromtimestamp(int(timestamp))
        if (year <> date.year):
            if (year <> 0):
                stats.append((year, year_stats))
            year = date.year
            year_stats = [0, 0]
        if (status == '200'):
            year_stats[0] = year_stats[0] + 1
        else:
            year_stats[1] = year_stats[1] + 1
    stats.append((year, year_stats))
    print "Year\tAlive\tDead\tDead (%)"
    for stat in stats:
        (year, year_stats) = stat
        (alive, dead) = year_stats
        dead_prctg = dead / float(alive + dead) * 100.0
        print "%d\t%d\t%d\t%0.1f" % (year, alive, dead, dead_prctg)

if __name__ == '__main__':
    main()

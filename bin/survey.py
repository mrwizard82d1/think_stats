"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import sys

from think_stats import survey


def main(name, data_dir='.'):
    resp = survey.Respondents()
    resp.ReadRecords(data_dir)
    print 'Number of respondents', len(resp.records)

    preg = survey.Pregnancies()
    preg.ReadRecords(data_dir)
    print 'Number of pregnancies', len(preg.records)

    
if __name__ == '__main__':
    main(*sys.argv)

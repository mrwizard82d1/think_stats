__author__ = 'l.jones'


import survey

# Print the number of pregnancies
table = survey.Pregnancies()
table.ReadRecords(data_dir='../etc')
print 'Number of pregnancies', len(table)

# Print the number of live births
live_births = [r for r in table.records if r.outcome == 1]
print 'Number of live births:', len(live_births)
first_live_births = [r for r in live_births if r.birthord == 1]
print 'Number of first live births:', len(first_live_births)
print 'Number of other live births;', len(live_births) - len(first_live_births)

average_first_gestation = \
    (float(sum([r.prglength for r in first_live_births])) /
     len(first_live_births))
print 'Average pregnancy length for first live births:', \
    (average_first_gestation)

other_live_births = [r for r in live_births if r.birthord != 1]
average_other_gestation = \
    (float(sum([r.prglength for r in other_live_births])) /
     len(other_live_births))
print 'Average pregnancy length for other live births:', \
    (average_other_gestation)

average_gestation_difference = \
    average_first_gestation - average_other_gestation
print 'Difference between gestation periods (first - other): %f :(%f hrs)' % \
      (average_gestation_difference, 24 * 7 * average_gestation_difference)
import pygal

from die import Die

die_1 = Die()
die_2 = Die()

results = [die_1.roll()+die_2.roll() for roll_num in range(1000)]

frequencies = [results.count(value) for value in range(2,die_1.num_sides*2+1)]

hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = [str(x) for x in range(2,die_1.num_sides*2+1)]
hist.x_title = 'result'
hist.y_title = 'Frequency of Rusult'

hist.add('D8+D8',frequencies)
hist.render_to_file('die_visual.SVG')

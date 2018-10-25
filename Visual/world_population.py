import json
from data_collect import get_data
from data_sectionalization import sectionalization
from make_visual import make_Worldmap

filename = 'population_data.json'
with open(filename) as f:
    pop_date = json.load(f)

cc_population = {}
get_data(pop_date,cc_population)

cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
sectionalization(cc_population,cc_pops_1,cc_pops_2,cc_pops_3)

make_Worldmap(cc_pops_1,cc_pops_2,cc_pops_3)

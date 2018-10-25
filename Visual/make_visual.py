import pygal
from pygal.style import RotateStyle as RS,LightColorizedStyle as LCS

def make_Worldmap(cc_pops_1,cc_pops_2,cc_pops_3):
    wm_style = RS('#336699',base_style=LCS)
    wm = pygal.Worldmap(style=wm_style)
    wm.add('0-10m',cc_pops_1)
    wm.add('10m-1bn',cc_pops_2)
    wm.add('>1bn',cc_pops_3)
    wm.title = 'World Population in 2010, by Country'
    wm.render_to_file('world_population.svg')

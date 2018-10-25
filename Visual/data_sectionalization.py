def sectionalization(cc_population,cc_pops_1,cc_pops_2,cc_pops_3):
    for cc,pop in cc_population.items():
        if pop < 10000000:
            cc_pops_1[cc] = pop
        elif pop < 1000000000:
            cc_pops_2[cc] = pop
        else:
            cc_pops_3[cc] = pop

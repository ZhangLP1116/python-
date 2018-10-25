from country_code import get_country_code

def get_data(pop_date,cc_population):
    for pop_dict in pop_date:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                cc_population[code] = population

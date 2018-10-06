def city_country(city,country,population=''):
    if population:
        return city+','+country+'-'+'population:'+str(population)
    else:
        return city+','+country

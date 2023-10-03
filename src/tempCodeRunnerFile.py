    regions = []
    
    for regionName in json.load(open('./assets/data/italyRegions.json')):
        regions.append(parsePlace(regionName["nome"]))
    
    province = ''
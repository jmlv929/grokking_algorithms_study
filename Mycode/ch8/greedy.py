
def greedy(stations, states_needed):
    states_covered = set()
    my_covered = set()
    my_station = set()
    while states_needed:
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered):
                big_station = station
                my_covered = covered
        states_needed -= my_covered
        my_station.add(big_station)
    return my_station

if __name__ == "__main__":
    states_needed = set(['mt', 'wa', 'or', 'nv', 'ut', 'az','id'])

    stations = {}
    stations['kone'] = set(['id', 'nv', 'ut'])
    stations['ktwo'] = set(['wa', 'id', 'mt'])
    stations['kthree'] = set(['or', 'nv', 'ca'])
    stations['kfour'] = set(['nv', 'ut'])
    stations['five'] = set(['ca', 'az'])

    print(greedy(stations, states_needed))





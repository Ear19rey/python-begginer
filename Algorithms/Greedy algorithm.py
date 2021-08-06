continent = ["Idaho","Nevada","Utah","Washington","Montana","Oregon","California","Arizona"]
states_needed = set(continent)

stations = {}
stations["kone"] = set(["Idaho","Nevada","Utah"])
stations["ktwo"] = set(["Washington","Idaho","Montana"])
stations["kthree"] = set(["Oregon","Nevada","California"])
stations["kfour"] = set(["Nevada","Utah"])
stations["kfive"] = set(["California","Arizona"])

final_stations = set()
while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
print(final_stations)
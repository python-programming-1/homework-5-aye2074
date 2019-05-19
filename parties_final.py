import csv
import pprint


def get_bar_party_data():
    """this function reads from a csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific location and the number of complaint calls
     it received in 2016"""

    bar_list = []
    with open('bar_locations.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            bar_dict = {'location_type': row[0],
                        'zip_code': row[1],
                        'city': row[2],
                        'borough': row[3],
                        'latitude': row[4],
                        'longitude': row[5],
                        'num_calls': row[6]}
            bar_list.append(bar_dict)
    return bar_list


def print_data(data):
    for entry in data:
        print(entry)
        pprint.pprint(entry)


def get_most_noisy_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """
    # write code here to find the noisiest city and borough and their respective metrics
    cities_and_total_calls = {}
    for i in range(1, len(data)):
        city = data[i]['city']
        num_call = data[i]['num_calls']
        cities_and_total_calls.setdefault(city, 0)
        cities_and_total_calls[city] += int(num_call)

    max_cities = max(cities_and_total_calls, key=cities_and_total_calls.get)
    max_call = cities_and_total_calls[max_cities]

    borough_and_total_calls = {}
    for j in range(1, len(data)):
        borough = data[j]['borough']
        num_calls = data[j]['num_calls']
        borough_and_total_calls.setdefault(borough, 0)
        borough_and_total_calls[borough] += int(num_calls)

    max_boroughs = max(borough_and_total_calls,
                       key=borough_and_total_calls.get)
    max_calls = borough_and_total_calls[max_boroughs]

    noisiest_city_and_borough = {
        'city': max_cities, 'borough': max_boroughs, 'num_city_calls': max_call, 'num_borough_calls': max_calls}

    return noisiest_city_and_borough


def get_quietest_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """
    # write code here to find the quietest city and borough and their respective metrics

    cities_and_total_calls = {}
    for i in range(1, len(data)):
        city = data[i]['city']
        num_call = data[i]['num_calls']
        cities_and_total_calls.setdefault(city, 0)
        cities_and_total_calls[city] += int(num_call)

    min_cities = min(cities_and_total_calls, key=cities_and_total_calls.get)
    min_call = cities_and_total_calls[min_cities]

    borough_and_total_calls = {}
    for j in range(1, len(data)):
        borough = data[j]['borough']
        num_calls = data[j]['num_calls']
        borough_and_total_calls.setdefault(borough, 0)
        borough_and_total_calls[borough] += int(num_calls)

    min_boroughs = min(borough_and_total_calls,
                       key=borough_and_total_calls.get)
    min_calls = borough_and_total_calls[min_boroughs]

    quietest_city_and_borough = {
        'city': min_cities, 'borough': min_boroughs, 'num_city_calls': min_call, 'num_borough_calls': min_calls}

    return quietest_city_and_borough


if __name__ == '__main__':
    bar_data = get_bar_party_data()

    # import pprint
    # uncomment the line below to see what the data looks like
    # print_data(bar_data)

    noisy_metrics = get_most_noisy_city_and_borough(bar_data)

    quiet_metrics = get_quietest_city_and_borough(bar_data)

    print('Noisy Metrics: {}'.format(noisy_metrics))
    print('Quiet Metrics: {}'.format(quiet_metrics))

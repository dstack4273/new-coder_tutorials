import geojson
import parse as p

def create_map(data_file):
    # Define the GeoJSON that we are creating
    geo_map = {"type": "FeatureCollection"}

    # make an empty list to collect the points for plotting
    item_list = []

    # Iterate through the input data to make the GeoJSON document The enumerate
    # function is being used here so that both the value of index and line
    # are captured for each object
    for index, line in enumerate(data_file):

        # records with coordinate values of zero are skipped to avoid plotting
        # locations that will skew the map
        if line['X'] == "0" or line['Y'] == "0":
            continue

        # create a new dictionary for every iteration through input data
        data = {}

        # reads the data from the input file and assigns the line items to
        # corresponding GeoJSON fields
        data['type'] = 'Feature'
        data['id'] = index
        data['properties'] = {'title': line['Category'],
                              'description': line['Descript'],
                              'date': line['Date']}
        data['geometry'] = {'type': 'Point',
                            'coordinates': (line['X'], line['Y'])}

        # add the newly created dictionary to the item_list
        item_list.append(data)

    # for every point in the item_list, the point is added to the dictionary
    # here setdefault creates a key called 'features' that has a value type
    # of an empty list, every iteration through appends the point to that list.
    for point in item_list:
        geo_map.setdefault('features', []).append(point)

    # Once all of the data is parsed into a GeoJSON object, it needs to be
    # written to a file for presentation on gist.github.com
    with open('file_sf.geojson', 'w') as f:
        f.write(geojson.dumps(geo_map))

def main():
    data = p.parse(p.MY_FILE, ",")

    return create_map(data)

if __name__ == "__main__":
    main()

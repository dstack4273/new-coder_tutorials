import csv

MY_FILE = "~/Projects/new-coder/dataviz/data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """Parses a raw CSV file into a JSON-like object."""

    #Open CSV File
    opened_file = open(raw_file)

    #Read CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Setup an empty list to hold the data
    parsed_data = []

    # Skip over the first line of the file for the headers
    fields = csv_data.next()

    # Iterate over each row of the csv file, zip together field -> value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    #Close CSV File
    opened_file.close()

    #Build a data structure with the parsed_data

    return parsed_data

def main():
    #Make a call to our parse function and pass needed parameters
    new_data = parse(MY_FILE, ",")

    #print the data out to see how it looks
    print new_data


if __name__ == "__main__":
    main()


#Revisit part 1 at some point to play with writing the output to a file or files
#as suggested at the end of the page.

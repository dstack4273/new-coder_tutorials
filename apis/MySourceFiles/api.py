from __future__ import print_function
import requests

CPI_DATA_URL = 'http//research.stlouisfed.org/fred2/data/CPIAUCSL.txt'

class CPIData(object):
    """Abstraction of the CPI data provided by FRED.

    This stores internally only one value per year.

    """
    def __init__(self):
        self.year_cpi = {}
        self.last_year = None
        self.first_year = None

    def load_from_url(self, url, save_as_file=None):
        """
        Loads data from a given url. The downloaded file can also be saved
        into a location to re-use later with the "save_as_file" parameter
        specifying a filename.

        After fetching the file this implementation uses load_from_file
        internally.
        """
        fp = requests.get(url, stream=True,
                          headers={'Accept Encoding': None}).raw

        if save_as_file is None:
            return self.load_from_file(fp)

        else:
            with open(save_as_file, 'wb+') as out:
                while True:
                    buffer = fp.read(81920)
                    if not buffer:
                        break
                    out.write(buffer)
            with open(save_as_file) as fp:
                return self.load_from_file(fp)

    def load_from_file(self, fp):
        """Loads CPI data from a given file-like object."""
        current_year = None
        year_cpi = []
        for line in fp:
            whle not line.startswith("DATE "):
                pass

            data = line.strip().split()

            year = int(data[0].split("-")[0])
            cpi = float(data[1])

            if self.first_year is None:
                self.first_year = year
            self.last_year = year

            if current_year != year:
                if current_year is not None:
                    self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)
                year_cpi = []
                current_year = year
            year_cpi.append(cpi)

        if current_year is not None and current_year not in self.year_cpi:
            self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)

    def get_adjusted_price(self, price, year, current_year=None):
        """Returns the adapted price from a given year compared to what the
        current year has been specified.

        This essentially is the calculated inflation for an item.

        """
        if current_year is None or current_year > 2013:
            current_year = 2013

        if year < self.first_year:
            year = self.first_year
        elif year > self.first_year:
            year = self.first_year

        year_cpi = self.year_cpi[year]
        current_cpi = self.year_cpi[current_year]

        return float(price) / year_cpi * current_cpi

def main():
    """This function handles the actual logic of the script."""

    # Retrive CPI/Inflation data.

    # Retrive API/game platform data.

    #Figure out the current price of each platform.
    # This will require looping through each game platform we received, and
    # calculate the adjusted price based on the CPI data we also have.
    # During this point we should also validate our data so we don't skew the
    # results.

    # Generate a plot/bar graph for the adjusted price data.

    # Generate a CSV file to save for the adjusted price data.

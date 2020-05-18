class dataquest:

    def maxOfPriceColumn(self, dataset):
        dataset["price"] = dataset["price"].str.replace("$", "")
        dataset["price"] = dataset["price"].str.replace(",", "")
        autos["price"] = autos["price"].astype(int)
        print("\nMinimum value of 'price' column :", dataset["price"].max())

    def minOfOdometerColumn(self, dataset):
        dataset["odometer"] = dataset["odometer"].str.replace(",", "")
        dataset["odometer"] = dataset["odometer"].str.replace("km", "")
        dataset["odometer"] = dataset["odometer"].astype(int)
        print("\nMinimum value of 'odometer' column :", dataset["odometer"].min())

    def meanOfPowerPSColumn(self, dataset):
        print("\nMean value of 'power_PS' column :", dataset["power_PS"].mean())


import pandas as pd

autos = pd.read_csv("autos.csv", encoding="Latin-1")
autos.index.name = None
autos.columns = ['date_crawled', 'name', 'seller', 'offer_type', 'price', 'ab_test',
                 'vehicle_type', 'registration_year', 'gear_box', 'power_PS', 'model',
                 'odometer', 'registration_month', 'fuel_type', 'brand',
                 'unrepaired_damage', 'ad_created', 'nr_of_pictures', 'postal_code',
                 'last_seen']

dataset1 = dataquest()
dataset1.maxOfPriceColumn(autos)
dataset1.minOfOdometerColumn(autos)
dataset1.meanOfPowerPSColumn(autos)

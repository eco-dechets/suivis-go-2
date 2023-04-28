import numpy as np
import streamlit as st
import pandas as pd
from database2 import Database2
from repositories.card_repository import CardRepository
from repositories.city_repository import CityRepository
from repositories.database import DatabaseRepository
from repositories.driver_repository import DriverRepository
from repositories.product_repository import ProductRepository
from repositories.site_repository import SiteRepository
from repositories.transaction_repository import TransactionRepository
from repositories.vehicle_repository import VehicleRepository
from repositories.vendor_repository import VendorRepository


class Avia:

    def __init__(self, file, vendor='Avia'):
        # try to read file as csv
        try:
            self.df = pd.read_csv(file, sep=';', index_col=False)
            # split the column CP VILLE into CP and VILLE and drop the column CP VILLE
            self.df[['CP', 'VILLE']] = self.df['CP VILLE'].str.split(' ', 1, expand=True)
            self.df.drop(columns=["CP VILLE"], inplace=True)
            # remove space at the beginning of the column name
            self.df.rename(columns=lambda x: x.strip(), inplace=True)
        except:
            st.error('Ce fichier n\'est pas un fichier CSV')
            # stop execution
            st.stop()
        self.vendor = vendor
        self.__is_avia()
        self.vehicle_repository = VehicleRepository()
        self.repository = DatabaseRepository()

    def __is_avia(self):
        # verify df column exist
        if 'NUM CARTE' in self.df.columns:
            return True
        else:
            st.error('Ce fichier n\'est pas un fichier Avia')
            # stop execution
            st.stop()

    def show_data(self):
        if self.vendor == 'Avia':
            return st.write(self.df)
        else:
            return st.write("Le fichier n'est pas un fichier Avia")

    def show_upload_btn(self):
        if st.button('upload data'):
            with st.spinner('Wait for it...'):
                try:
                    self.insert_data()
                    st.success('Data uploaded')
                except Exception as e:
                    print(e)
                    st.error(e)
                    st.stop()

    def test(self):
        # insert all data into the database
        try:
            print(self.df.info())
        except Exception as e:
            print(e)

        print('done')

    def insert_data(self):
        # insert all data into the database

        vehicle_repository = VehicleRepository()

        try:
            for index, row in self.df.iterrows():
                card_number = row['NUM CARTE'].replace("'", '')
                transaction_date = row['DATE']
                registration_number = row['IMMATRICULATION'].replace('-', ' ')
                site_number = row['NUM SITE']
                post_code = row['CP']
                city = row['VILLE']
                product = row['PRODUIT']
                quantity = row['QUANTITE'].replace(',', '.')
                unit_price_ttc = row['PU'].replace(',', '.')
                amount_ttc = row['MONTANT'].replace(',', '.')
                kilometer = row['KM']
                consumption = row['CONSO L au 100'].replace(',', '.')
                driver_code = row["CODE CHAUFFEUR"]


                # insert data into the database

                id_registration = self.vehicle_repository.insert_vehicle(registration=registration_number)
                id_site = SiteRepository().insert_site(num=site_number)
                id_card = CardRepository().insert_card(num=card_number)
                id_driver = DriverRepository().insert_driver(code=driver_code)
                id_product = ProductRepository().insert_product(name=product)
                id_city = CityRepository().insert_city(city, post_code)
                id_vendor = VendorRepository().insert_vendor(name=self.vendor)

                print(id_vendor)

                TransactionRepository().insert_transaction(date=transaction_date, quantity=quantity,
                                                           unit_price_ttc=unit_price_ttc, amount_ttc=amount_ttc,
                                                           kilometer=kilometer, consumption=consumption,
                                                           id_site=id_site[0], id_card=id_card[0],
                                                           id_driver=id_driver[0],
                                                           id_product=id_product[0], id_city=id_city[0],
                                                           id_vendor=id_vendor[0], id_vehicle=id_registration[0])

        except Exception as e:
            print(e)

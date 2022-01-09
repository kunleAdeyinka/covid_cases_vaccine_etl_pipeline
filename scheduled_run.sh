#!/bin/bash
# Activate the venv and navigate to the location of main.py
source venv/bin/activate
cd scripts

python main.py -local_source -name acs_population_counties /../../data/acs_5yr_population_data.csv kunleAdeyinka/WaffleCringe.population_counties

python main.py -name nyt_cases_counties 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv' kunleAdeyinka/WaffleCringe.cases_counties

python main.py -name cdc_vaccines_counties 'https://data.cdc.gov/api/views/8xkx-amqh/rows.csv?accessType=DOWNLOAD' kunleAdeyinka/WaffleCringe.vaccinations_counties


# run the in-database table update query after each run of the ETL jobs.
python sql_executor.py ca_covid_data.sql
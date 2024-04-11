# authors: Shahrukh Islam Prithibi, Sophie Yang, Yovindu Don, Jade Bouchard
# date: 2024-04-07
#
# This script fetches the credit risk data from the UCI Machine Learning Repository.
# It then saves the data at the provided filepath.
#
# Usage: python scripts/download_data.py data/german.csv


from ucimlrepo import fetch_ucirepo 
import click

@click.command()
@click.argument('raw_data_output_path', type=str)

def main(raw_data_output_path):
    '''fetch and write german data'''
    # fetch dataset 
    statlog_german_credit_data = fetch_ucirepo(id=144) 
      
    # data (as pandas dataframes) 
    dataframe = statlog_german_credit_data.data.original
    
    # write to csv
    dataframe.to_csv(raw_data_output_path, index = False)

if __name__ == '__main__':
    main()
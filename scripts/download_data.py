from ucimlrepo import fetch_ucirepo 
import click

@click.command()
@click.argument('output_path', type=str)

def main(output_path):
    '''fetch and write german data'''
    # fetch dataset 
    statlog_german_credit_data = fetch_ucirepo(id=144) 
      
    # data (as pandas dataframes) 
    dataframe = statlog_german_credit_data.data.original
    
    # write to csv
    dataframe.to_csv(output_path, index = False)

if __name__ == '__main__':
    main()
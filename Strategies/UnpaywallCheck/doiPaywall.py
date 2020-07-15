# -*- coding: utf-8 -*-
"""
Author Baudouin Martelee
FRISteam

"""
#Import packages
import os
import pandas as pd
import json
import glob
import requests


def import_doi_data(csv_path):
    """
    Import data form a csv file containing doi url

    Args:
        csv_path (string): path of the csv file 

    Returns:
        Dataframe: dataframe containing data of the csvfile
    """
    dois_csv = pd.read_csv(csv_path,sep=';')
    dois_csv.head()
    
    return dois_csv


def extract_doi(dois_urls_series):
    """
    Extract dois from the dois urls and store them in a list

    Args:
        dois_urls_series (Series): Series od the dois url

    Returns:
        List: List of the dois from the dois urls
    """
    slashparts = dois_urls_series.str.split('https://doi.org/')
    dois_list = list()

    for i in range(len(dois_urls_series)):
        dois_list.append(slashparts[i][1])

    return dois_list


def get_publication(doi, file_to_save_to):
    """
    Get the json of the doi from the Unpaywall API and store it in the file "file_to_save_to"

    Args:
        doi (string): doi 
        file_to_save_to (string): path of the file where to store 
    """
    url = f'http://api.unpaywall.org/v2/{doi}?email=baudlemartino@hotmail.com'
    with requests.get(url, stream=True) as r:
        if r.status_code == 200:
            for chunk in r.iter_content(chunk_size=1024*1024):
                file_to_save_to.write(chunk)


def get_api_information(directory_path_to_store, dois_list):
    """
    For each doi of the doi list, we create a json file. We store all the different json files in a directory.

    Args:
        directory_path_to_store (string): path of the directory where to store the json files 
        dois_list (List): list containing dois
    """
    count =0
    for doi in dois_list:
        doiID = doi.replace('/','_')
        if not os.path.exists('{}/{}.json'.format(directory_path_to_store,doiID)):
            directory_path_to_store = directory_path_to_store.replace('\\','/')
            with open('{}/DOI{}.json'.format(directory_path_to_store,doiID), 'wb') as file :
                get_publication(doi, file)
            count += 1
            print("Done: {} of {} articles".format(count,len(dois_list)))


def add_pdf_information(dois_csv, directory_path):
    """
    Fill the basic csv with different information like if the data is received from unpaywall, if there is a paywall or not,
    if there is a url for pdf.

    Args:
        dois_csv (Csv file): csv file containing the differents dois
        directory_path (string): path of directory where are store the json files
    
    Returns:
        List: List of the dois from the dois urls
    """
    dois_unpaywall_csv = dois_csv.copy()

    dois_unpaywall_csv["doi2"]= ""
    dois_unpaywall_csv["data received from unpaywall"]= ""
    dois_unpaywall_csv["No paywall"]= ""
    dois_unpaywall_csv["pdf urls"]= ""

    dois_unpaywall_csv.drop('publication_title', axis=1, inplace=True)
    dois_unpaywall_csv.drop('doi', axis=1, inplace=True)
    dois_unpaywall_csv = dois_unpaywall_csv.rename(columns={"doi2": "doi"})

    i = 0
    for filepath in glob.glob(os.path.join(directory_path,'*.json')):
        filepath = filepath.replace('\\','/')
        with open(filepath, 'r') as file :
            try:
                jsonfile = json.loads(file.read())
                dois_unpaywall_csv["data received from unpaywall"][i] = "yes"
            except:
                dois_unpaywall_csv["data received from unpaywall"][i] = "no"
        
            dois_unpaywall_csv['doi'][i] = jsonfile["doi_url"]
            dois_unpaywall_csv['No paywall'][i] = jsonfile["is_oa"]
            
            if jsonfile["best_oa_location"] is not None:
                dois_unpaywall_csv['pdf urls'][i] = jsonfile["best_oa_location"]["url_for_pdf"]
            else:
                dois_unpaywall_csv['pdf urls'][i] = "No pdf"
            
            i = i+1
    
    return dois_unpaywall_csv


def merge_dataframe_on_doi(first_df, second_df):
    result = pd.merge(first_df, second_df, how='outer', on='doi')
    return result

def remove_link_without_json(df):
    for index, row in df.iterrows():
        if row['data received from unpaywall'] == "no":
            result = df.drop([index])
    return result

def export_csv(dataframe, csv_path):
    """
    Export csv from a dataframe

    Args:
        dataframe (Dataframe): Dataframe
        csv_path (string): path to store the new csv file
    """
    dataframe.to_csv(csv_path, index=False)


def main():

    csv_path = r"/Users/martelee/Desktop/OSOC/FRISteam/Strategies/UnpaywallCheck/dois.csv"
    dois_csv = import_doi_data(csv_path)

    dois_list = extract_doi(dois_csv["doi"])
    

    dois_directory = "/Users/martelee/Desktop/OSOC/FRISteam/Strategies/UnpaywallCheck/DOIS"

    #get_api_information(dois_directory, dois_list)

    dois_unpaywall_csv = add_pdf_information(dois_csv,"/Users/martelee/Desktop/OSOC/FRISteam/Strategies/UnpaywallCheck/DOIS")

    merge_df = merge_dataframe_on_doi(dois_csv, dois_unpaywall_csv)

    result_doi = remove_link_without_json(merge_df)

    export_csv(result_doi, "/Users/martelee/Desktop/OSOC/FRISteam/Strategies/UnpaywallCheck/final_dois.csv")

if __name__ == "__main__":
    main()
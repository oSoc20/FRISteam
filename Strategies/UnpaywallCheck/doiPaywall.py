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

from Utils.enricher_entities import Doi

"""
If you handle a publication json with a doi    

"""


def add_doi_object(publication_doi):
    """
    Return a doi object to the Enricher containing for the doi different information like : 
        doi, data_received_from_Unpaywall_api, no_paywall, pdf_url

    Args:
        publication_doi (str): doi of a publication 

    Returns:
        Doi object: Doi object with the fields : doi, data_received_from_Unpaywall_api, no_paywall, pdf_url
    """
    doi = extract_doi_from_url(publication_doi)
    path_to_store_json = './Strategies/UnpaywallCheck/DOIS'
    get_api_information_of_doi(path_to_store_json, doi)
    data_received_from_Unpaywall_api, no_paywall, pdf_url = add_pdf_information_of_doi(path_to_store_json, doi)
    doi_obj = Doi(publication_doi, data_received_from_Unpaywall_api, no_paywall, pdf_url)

    return doi_obj


def extract_doi_from_url(doi_url):
    """
    Extract doi from a doi url

    Args:
        doi url (str): doi url

    Returns:
        doi: doi from the doi url
    """
    slashparts = doi.split('https://doi.org/')

    return slashparts[1]

def get_api_information_of_doi(directory_path_to_store, doi):
    """
    For the doi, we create a json file. We store thejson files in a directory.

    Args:
        directory_path_to_store (string): path of the directory where to store the json files 
        dois (str): doi
    """
    doiID = doi.replace('/','_')
    if not os.path.exists('{}/{}.json'.format(directory_path_to_store,doiID)):
        directory_path_to_store = directory_path_to_store.replace('\\','/')
        with open('{}/DOI{}.json'.format(directory_path_to_store,doiID), 'wb') as file :
            get_publication(doi, file)
    print("Doi generate !")

def add_pdf_information_of_doi(directory_path, doi):
    """
    add the different information to the doi object because of its json file

    Args:
        dois (str): doi 
        directory_path (string): path of directory where are store the json files
    
    Returns:
        List: List of the dois from the dois urls
    """
    data_received_from_Unpaywall_api = True
    no_paywall = False
    pdf_url = ""

    doi = doi.replace('/','_')
    filepath = os.path.join(directory_path,'DOI{}.json'.format(doi))
    filepath = filepath.replace('\\','/')
    with open(filepath, 'r') as file :
        try:
            jsonfile = json.loads(file.read())
        except:
            data_received_from_Unpaywall_api = False
    
        no_paywall = jsonfile["is_oa"]
        
        if jsonfile["best_oa_location"] is not None:
            pdf_url = jsonfile["best_oa_location"]["url_for_pdf"]
        else:
            pdf_url = "No pdf"
        
    
    return data_received_from_Unpaywall_api, no_paywall, pdf_url


"""
If you handle a csv file   
"""
                                       


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
    """[summary]
    Merge 2 dataframe to create 1 dataframe

    Args:
        first_df (DataFrame): dataframe containing publication title and doi
        second_df (DataFrame): dataframe containing doi, url for pdf ,...

    Returns:
        DataFrame: Result dataFrame
    """
    result = pd.merge(first_df, second_df, how='outer', on='doi')
    return result

def remove_link_without_json(df):
    """
    This fonction is to avoid double item in the csv. If the data aren't fetch from the Unpaywall api, we remove the doublon.

    Args:
        df (DataFrame): Dataframe to cleaned

    Returns:
        [DataFrame]: DataFrame cleaned
    """
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

    #If you handle a csv file

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
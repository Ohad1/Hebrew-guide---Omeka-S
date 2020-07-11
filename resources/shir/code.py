import os
import io
import sys
import time
import requests
import json
import csv
import pandas

# IMPORTANT NOTE:
# number of items in each response is limited to the number appears in your omeka account at "general setting -> Results per page" so make sure you don't miss items regarding this issue

# RUNNING INSTRUCTIONS:
#   python ./richdataapi.py ./relative_path_to_csvfile/fileName.csv

# code to create dictionary using omeka api {"itemset_name": omeka_id}
id_by_itemSet = {}

def extract_dict_id_by_itemSet(json_object):
    #iterate over response:
    for dict in json_object:
        key = dict['o:title']   # key = title is uniqe value for each itemset
        val = dict['o:id']      # value = omeka id
        id_by_itemSet [key] = val
    return id_by_itemSet

def omekaApiItemSets():
    install_location = "http://site_name.reclaim_hoasting_domain"
    # generate key_identity and key_credential with your omeka acount
    # mor info: https://omeka.org/s/docs/user-manual/admin/users/#api-key
    key_identity = 'put your string here'
    key_credential = 'put your string here'
    endpoint = "{}/api/item_sets?key_identity={}&key_credential={}"
    final_uri = endpoint.format(install_location, key_identity, key_credential)
    headers = {
        'accept': 'application/json'
    }
    try:
        # send question...
        response = requests.get(final_uri, headers=headers)
    except requests.RequestException as e:
        dict(error=str(e))
    # print (response)
    data = response.json()
    # print(data)
    # iterate response and create dictionary
    id_by_itemSet = extract_dict_id_by_itemSet(data)
    print (id_by_itemSet)

# code to get all items in item set by itemset id using omeka api 
# input: itemset id (you should use previous function to get it by itemset name)
# output: response json contained all relevant items
def omekaApiItems(item_set_id):
    install_location = "http://site_name.reclaim_hoasting_domain"
    # generate key_identity and key_credential with your omeka acount
    # mor info: https://omeka.org/s/docs/user-manual/admin/users/#api-key
    key_identity = 'put your string here'
    key_credential = 'put your string here'
    endpoint = "{}/api/items?key_identity={}&key_credential={}&item_set_id={}"
    final_uri = endpoint.format(install_location, key_identity, key_credential, item_set_id)
    headers = {
        'accept': 'application/json'
    }
    try:
        response = requests.get(final_uri, headers=headers)#data={'data': json.dumps(items)},
    except requests.RequestException as e:
        dict(error=str(e))
    return response.json()

# code to exstract dictionary dict {"identifierFieldContent": omeka_id} from omeka API json response
# input: json object 
# output: dictionary with key = "identifierFieldContent" value = omeka_id

def extract_dict_id_pageIdentifier(json_object):    
    for dict in json_object:
        key = dict['dcterms:identifier'][0]['@value']
        val = dict['o:id']
        id_by_identifierField = {} #dict {"identifierFieldContent": omeka_id}
        id_by_identifierField [key] = val
    return id_by_identifierField


# code to edit csvFile and assign omeka id
def editCSV(csvFileName):
    # declare all column titles and ther content type - assign your own columns
    dataTypes={"your_column1_title":"your_column1_type","o:is_public":"string","o:owner":"string","dcterms:resource_class":"string","o:resource_template":"string","o:item_set":"string","dcterms:title":"string","dcterms:description":"string","bibo:volume":"string","bibo:chapter":"string","bibo:number":"string","dcterms:bibleVersion":"string","dcterms:language":"string","dcterms:isPartOf":"string"}
    # open and read csv file 
    df = pandas.read_csv(csvFileName, dtype=dataTypes)
    #build dict page- omeka id
    data = omekaApiItems(id_by_itemSet.get("itemSet_name_here"))
    dict_id_pageIdentifier = extract_dict_id_pageIdentifier(data)
    # iterate over csv rows
    r = len(df.index)
    for i in range(r):
        # if cell at [row,col] is in dictionary as key, assign it's value to that cell. else delete row from table
        if (dict_id_pageIdentifier.get(df.at [i, 'column_title_here']) != None):
            df.at [i, 'column_title_here'] = str(dict_id_pageIdentifier[df.at [i, 'column_title_here']])
        else: # if all is correct this should not happen
            df = df.drop(i)
            print ("row deleted")
    # print df after changes
    print (df)    
    # write df into new csv output file
    df.to_csv(os.path.splitext(os.path.basename(csvFileName))[0]+"_output.csv", index=False) 




#------------------------------------------------------------------------------------------------
# create main to run functions
if __name__ == "__main__":
    # create global variable dictionary using omeka api {"itemset_name": omeka_id}
    omekaApiItemSets()
    # create new csvFile and assign omeka id insted of identifier to another item
    editCSV(sys.argv[1])
# FRISteam

### Procfile
File required to run the http server on Heroku.

### requirements.txt
Required by Heroku to run correctly the app on the Heroku server.
It is required to update the file with new libraries every time new ones
are added in any part the app.

## API
Online http server: ``https://fris-enricher.herokuapp.com``  
The file that initializes the server is in ./API/http_server.py.
### Routes
#### /api/projects/enrich
It will return the enriched data for a project as response as JSON.  
``POST`` request with the following JSON body data structure:  
````
{      
  "uuid": "85dbe745-772d-472e-b5fa-3e6d36f966d4",  
  "keywordsEn": ["key1", "key2"],  
  "keywordsNl": ["key1", "key2", "key3"],  
  "abstractEn": "the en abstr",  
  "abstractNl": "the nl abstr",  
  "titleEn": "the english title",  
  "titleNl": "the dutch title"  
}
````

#### /api/publications/enrich
It will return the enriched data for a publication as response as JSON.  
``POST`` request with the following JSON body data structure:  
````
{      
  "uuid": "85dbe745-772d-472e-b5fa-3e6d36f966d4",  
  "keywordsEn": ["key1", "key2"],  
  "keywordsNl": ["key1", "key2", "key3"],  
  "abstractEn": "the en abstr",  
  "abstractNl": "the nl abstr",  
  "titleEn": "the english title",  
  "titleNl": "the dutch title",
  "doi": "https://the.doi"   
}
````

#### /documentation
``GET`` request:  
It will serve the html file with all documentation of the project.

## Maintenance
To compare our enriched keywords to the other keywords in the entire system we use the "./Utils/researchoutput_uuid_keywords.csv" file. The functions to read from this file are in "./Utils/csv_reader.py". This is used in "./Strategies/NetworkRelation/keyword_dictionary.py" to write two dictionaries to json files for memoization purposes.
To maintain this, update the csv file and the functions in "csv_reader.py" and run the "compose_keyword_dictionary" function in "./Strategies/NetworkRelation/keyword_dictionary.py". This should re-generate the two dictionary jsons.  

## UNIT TESTING
All unit tests are in "./Tests". The test names all start with "test_" and they use the python unittest framework.
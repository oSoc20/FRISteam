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
It is a ``POST`` request with the following JSON body data structure:  
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
It is a ``POST`` request with the following JSON body data structure:  
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

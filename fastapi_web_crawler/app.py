from fastapi import FastAPI

import requests
from pydantic import BaseModel, HttpUrl
from bs4 import BeautifulSoup


app = FastAPI()

class URL(BaseModel):
    url: HttpUrl #walidacja danych od usera




@app.get('/')
def index():
    return {'message': "Hello FastApi"}

@app.post('/scrap_tags')
async def scrape_tags(url:URL):

    page = requests.get(str(url.url))
    soup = BeautifulSoup(page.text, 'html.parser')
    # import pdb
    # pdb.set_trace()

    def get_title():
        return soup.head.find('title').text if soup.head.find('title') else None

    def get_description():
        """
        Example: 
            {
                "url":"http://www.google.com"
            }

            {
                "url":"http://www.github.com"
            }

            {
                "url":"http://www.yahoo.com"
            }
            
            {
                "url":"http://www.github.com/pawlaczyk"
            }
        """
        description = soup.head.find('meta', attrs={'name': 'description'})
        meta_description = description.get('content') if description else None 

        description = soup.find("meta", property="og:description")
        og_description = description.get('content') if description else None

        response = None
        if meta_description or og_description:
            response = {
                "meta_description": meta_description, 
                "og_description": og_description
            }

        return response

    def get_keywords():
        meta_keywords = soup.head.find('meta', attrs={'name': 'keywords'})
        return meta_keywords.get('content') if meta_keywords else None 


    def get_image():
        og_image = soup.find("meta", property="og:image")
        return og_image.get('content') if og_image else None


    descriptions = get_description()
    return {
        "title": get_title(),
        "description": get_description(), 
        "keywords": get_keywords(),
        "image": get_image()
    }



# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=4200, reload=True)
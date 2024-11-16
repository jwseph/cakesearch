'''

What is this?
server.py is a very dummy static server code only for testing.
It basically just lets you view files in the same folder using localhost:80.
Feel free to change port numbers and stuff.
Make sure we don't send server.py when we update the website :sob:

'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from cake_image import get_generated_image_url, get_text_response

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.mount('/', StaticFiles(directory='./'))

@app.get('/')
async def get_home():
    return 'home'

@app.get('/cake_image')
async def get_cake_image(size: str, flavor: str, frosting: str, filling: str, decoration: str, gender: str):
    prompt = [
        'I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS:',
        f'Cake size: {size}, Cake flavor: {flavor}, cake frosting: {frosting}, cake filling: {filling}',
        f'Cake decoration: {decoration}, keep in mind this cake is being made for a {gender}'
    ]
    return {
        'url': get_generated_image_url('\n'.join(prompt)),
        'price': '$1000',
    }


@app.get('/cake_recipe')
async def get_cake_recipe(size: str, flavor: str, frosting: str, filling: str, decoration: str, gender: str):
    prompt = [
        'Please tell me the recipe to bake this cake:',
        f'Cake size: {size}, Cake flavor: {flavor}, cake frosting: {frosting}, cake filling: {filling}',
        f'Cake decoration: {decoration}, keep in mind this cake is being made for a {gender}'
    ]
    return {
        'recipe': get_text_response('\n'.join(prompt)),
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=80)

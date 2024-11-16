from openai import OpenAI
from PIL import Image
import requests
from io import BytesIO
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_generated_image_url(prompt):
    imagedata = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
    )
    dump = imagedata.model_dump()
    return dump['data'][0]['url']

def get_text_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant to a customer in a bakery with estimating costs, generating recipes, etc"},
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )
    return completion.choices[0].message.content


def view_image(url):
    # Fetch the image using requests
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Open the image with PIL
    image = Image.open(BytesIO(response.content))

    # Display the image
    image.show()


# view_image(dump['data'][0]['url'])
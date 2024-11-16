from openai import OpenAI
from PIL import Image
import requests
from io import BytesIO
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

imagedata = client.images.generate(
  model="dall-e-3",
  prompt="I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS:" + "A cute baby sea otter",
)

dump = imagedata.model_dump()
print(dump)


def view_image(url):
    # Fetch the image using requests
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Open the image with PIL
    image = Image.open(BytesIO(response.content))

    # Display the image
    image.show()


view_image(dump['data'][0]['url'])
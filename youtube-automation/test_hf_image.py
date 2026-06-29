from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)

image = client.text_to_image(
    "A futuristic city at sunset, cinematic, ultra realistic",
    model="stabilityai/stable-diffusion-xl-base-1.0"
)

image.save("test.png")

print("Done!")

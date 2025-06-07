import requests
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Use INFO or WARNING in production
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def generate_image(prompt, output_path="generated_image.webp"):
    # Load API key from environment variable
    api_key = os.getenv("STABILITY_API_KEY")
    logging.info(f"This is the APi key {api_key}")
    if not api_key:
        logging.error("STABILITY_API_KEY environment variable is not set.")
        return None

    url = "https://api.stability.ai/v2beta/stable-image/generate/core"
    headers = {
        "authorization": f"Bearer {api_key}",
        "accept": "image/*"
    }

    data = {
        "prompt": prompt,
        "output_format": "webp",
    }

    try:
        logging.info(f"Sending image generation request for prompt: {prompt}")
        response = requests.post(url, headers=headers, files={"none": ''}, data=data)

        if response.status_code == 200:
            with open(output_path, 'wb') as file:
                file.write(response.content)
            logging.info(f"Image saved to {output_path}")
            return output_path
        else:
            error_message = response.json()
            logging.error(f"API request failed: {error_message}")
            return None

    except Exception as e:
        logging.exception("Unexpected error occurred while generating image.")
        return None

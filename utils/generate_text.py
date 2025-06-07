import cohere
import os

def generate_blog_post(topic, tone):
    cohere_api_key = os.getenv("COHERE_API_KEY")
    co = cohere.Client(cohere_api_key)

    prompt = f"Write a 500-word {tone.lower()} blog post about: {topic}"
    response = co.generate(model='command', prompt=prompt, max_tokens=500)
    return response.generations[0].text.strip()

def aarya_generate_blog_post(topic, tone):
    """
    Generate a blog post using Cohere's command model.
    
    Args:
        topic (str): The topic of the blog post.
        tone (str): The desired tone of the blog post.
        
    Returns:
        str: The generated blog post text.
    """
    return generate_blog_post(topic, tone)
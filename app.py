import streamlit as st
from utils.generate_text import generate_blog_post
from utils.summarize import summarize_text, extract_keywords
from utils.generate_image import generate_image
import os
from dotenv import load_dotenv

load_dotenv()

st.title("📝 AI Blog Post Generator")

topic = st.text_input("Enter blog topic:", "Best time to visit Japan")
tone = st.selectbox("Choose tone:", ["Informative", "Casual", "Professional", "Humorous"])

if st.button("Generate"):
    with st.spinner("Generating blog post..."):
        blog_post = generate_blog_post(topic, tone)
        st.subheader("📄 Blog Post")
        st.write(blog_post)

        summary = summarize_text(blog_post)
        keywords = extract_keywords(blog_post)


        st.subheader("🔍 Summary")
        st.write(summary)
        st.subheader("🔑 Keywords")
        st.write(", ".join(keywords[:5]))

        st.subheader("🖼️ Generated Image")
        image_url = generate_image(topic)
        if image_url:
            st.image(image_url)
        else:
            st.warning("Image generation failed.")

        st.download_button("📥 Download Blog", blog_post, file_name="blog_post.txt")

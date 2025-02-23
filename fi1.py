#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import google.generativeai as genai
import easyocr
import re
import os
from PIL import Image

# Set up Google Gemini
API_KEY_GEMINI = "AIzaSyA-9-lTQTWdNM43YdOXMQwGKDy0SrMwo6c"  # Replace with your Gemini API key
genai.configure(api_key=API_KEY_GEMINI)
model = genai.GenerativeModel('gemini-pro')

# Create a directory for EasyOCR models
os.makedirs("easyocr_models", exist_ok=True)

# Initialize EasyOCR with a custom model storage directory
reader = easyocr.Reader(['en'], model_storage_directory="easyocr_models")

# Function to extract text using EasyOCR
def extract_text_from_image(image_path):
    result = reader.readtext(image_path)
    extracted_text = " ".join([text[1] for text in result])  # Combine all detected text
    return extracted_text

# Function to clean and parse salary components
def parse_salary_data(text):
    salary_data = {
        "basic_salary": 0,
        "hra": 0,
        "allowances": 0,
        "deductions": 0

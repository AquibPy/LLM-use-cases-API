# Generative AI APIs

This project contains a collection of APIs that leverage Generative AI models to perform various tasks. These APIs are designed to address different use cases such as extracting information from invoices, generating responses from FAQs, summarizing YouTube videos, generating blog posts, analyzing health-related data from images, and executing SQL queries from text prompts for database operations related to employee data.

## Table of Contents

- [Overview](#overview)
- [Endpoints](#endpoints)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Running the Server](#running-the-server)
- [Contributing](#contributing)

## Overview

Generative AI, powered by advanced machine learning models, enables the creation of content, responses, and insights that mimic human-like behavior. This project harnesses the capabilities of Generative AI to provide a set of APIs catering to various tasks across different domains.

## Endpoints

### 1. Invoice Extractor

- **Route:** `/invoice_extractor`
- **Description:** This endpoint extracts information from invoices based on provided images and prompts. It utilizes a Generative AI model to process the input and generate relevant data.

### 2. QA from FAQs

- **Route:** `/qa_from_faqs`
- **Description:** The QA from FAQs endpoint uses retrieved question-answer pairs to generate responses to user prompts. It employs a Generative AI model trained on FAQ datasets to provide accurate and relevant answers.

### 3. QA URL/Doc

- **Route:** `/qa_url_doc`
- **Description:** With this endpoint, users can provide either a URL or upload a document (e.g., news article, blog) along with a question. The endpoint generates responses to the question based on the content of the provided URL or document using Generative AI models.

### 4. YouTube Video Transcribe Summarizer

- **Route:** `/youtube_video_transcribe_summarizer`
- **Description:** This endpoint utilizes a Generative AI model to summarize YouTube videos by transcribing the video content and generating a concise summary.

### 5. Nutritionist Expert

- **Route:** `/health_app_gemini`
- **Description:** The Nutritionist Expert endpoint analyzes images of food items to extract nutritional information and provide insights on calorie intake and weight management. Users can input their height and weight for personalized recommendations.

### 6. Blog Generator

- **Route:** `/blog_generator`
- **Description:** Generate informative and engaging blog posts on a specified topic using a Generative AI model. The endpoint generates content in a friendly and informative tone, encouraging readers to explore the topic further.

### 7. Talk2PDF

- **Route:** `/talk2PDF`
- **Description:** Extract information from PDF documents and provide responses based on user prompts. The endpoint utilizes Generative AI models to process the document content and generate relevant answers.

### 8. Text2SQL

- **Route:** `/Text2SQL`
- **Description:** Generate SQL queries and results from an employee database based on user prompts. The endpoint uses Generative AI models to convert text prompts into SQL queries for database operations.

## Usage

Each endpoint accepts specific parameters as described in the respective endpoint documentation. Users can make POST requests to these endpoints with the required parameters to perform the desired tasks.

## Dependencies

- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.
- Pydantic: Data validation and settings management using Python type annotations.
- Other dependencies specific to individual endpoint functionalities.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Install dependencies:
    ```python
    pip install -r requirements.txt
    ```

3. Create ```.evn``` file

    Save Google and Hugging Face API key in this file.

## Running the Server

Start the FastAPI server by running the following command:
    ```
    uvicorn main:app --reload
    ```

## Contributing

Contributions are welcome! Feel free to open a pull request or submit an issue for any bugs or feature requests.

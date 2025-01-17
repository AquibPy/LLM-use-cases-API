from fastapi.testclient import TestClient
from api import app
# from mongo import MongoDB
from settings import summary_para
from unittest.mock import MagicMock, patch

client = TestClient(app)
# db = MongoDB()

def test_invoice_extractor():
    with patch('api.MongoDB') as MockMongoDB:
        mock_insert_data = MagicMock(return_value={'Status': 'Successfully Inserted!!!', 'Document_id': 'mock_id'})
        MockMongoDB.return_value.insert_data = mock_insert_data
        
        image_file = open("data/invoice.png", "rb")
        files = {"image_file": image_file}
        data = {"prompt": "To whom this invoice belongs"}

        with TestClient(app) as client:
            response = client.post("/invoice_extractor", files=files, data=data)
            assert response.status_code == 200
            assert "response" in response.json()

def test_blogs():
    data = {"topic": "Tensorflow"}

    with patch('api.MongoDB') as MockMongoDB:
        mock_insert_data = MagicMock(return_value={'Status': 'Successfully Inserted!!!', 'Document_id': 'mock_id'})
        MockMongoDB.return_value.insert_data = mock_insert_data
        
        response = client.post("/blog_generator", data=data)
        assert response.status_code == 200
        assert "response" in response.json()

def test_sql_query():
    data = {"prompt": "Tell me the employees living in city Noida"}

    with patch('api.MongoDB') as MockMongoDB:
        mock_insert_data = MagicMock(return_value={'Status': 'Successfully Inserted!!!', 'Document_id': 'mock_id'})
        MockMongoDB.return_value.insert_data = mock_insert_data
        
        response = client.post("/Text2SQL", data=data)
        assert response.status_code == 200
        assert "response" in response.json()

def test_youtube_video_transcribe_summarizer():
    data = {"url": "https://www.youtube.com/watch?v=voexVsTHPBY&ab_channel=NabeelNawab"}

    with patch('api.MongoDB') as MockMongoDB:
        mock_insert_data = MagicMock(return_value={'Status': 'Successfully Inserted!!!', 'Document_id': 'mock_id'})
        MockMongoDB.return_value.insert_data = mock_insert_data
        
        response = client.post("/youtube_video_transcribe_summarizer", data=data)
        assert response.status_code == 200
        assert "response" in response.json()

def test_nutritionist_expert():
    image_file = open("data/burger.jpg", "rb")
    data = {"height": "165", "weight": "70"}

    with patch('api.MongoDB') as MockMongoDB:
        mock_insert_data = MagicMock(return_value={'Status': 'Successfully Inserted!!!', 'Document_id': 'mock_id'})
        MockMongoDB.return_value.insert_data = mock_insert_data
        
        response = client.post("/nutritionist_expert", files={"image_file": image_file}, data=data)
        assert response.status_code == 200
        assert "response" in response.json()

def test_talk2PDF():
    pdf_file = open("data/yolo.pdf", "rb")
    data = {"prompt": "Summary in 200 words"}

    with patch('api.MongoDB') as MockMongoDB:
        mock_insert_data = MagicMock(return_value={'Status': 'Successfully Inserted!!!', 'Document_id': 'mock_id'})
        MockMongoDB.return_value.insert_data = mock_insert_data
        
        response = client.post("/talk2PDF", files={"pdf": pdf_file}, data=data)
        assert response.status_code == 200
        assert "response" in response.json()

def test_questions_generator():
    pdf_file = open("data/yolo.pdf", "rb")

    with patch('api.MongoDB') as MockMongoDB:
        mock_insert_data = MagicMock(return_value={'Status': 'Successfully Inserted!!!', 'Document_id': 'mock_id'})
        MockMongoDB.return_value.insert_data = mock_insert_data
        
        response = client.post("/questions_generator", files={"pdf": pdf_file})
        assert response.status_code == 200
        assert "response" in response.json()

def test_chat_groq():
    question = "What is the capital of France?"
    model = "mixtral-8x7b-32768"
    conversational_memory_length = 5
    data = {
        "question": question,
        "model": model,
        "conversational_memory_length": conversational_memory_length
    }
    with patch('api.MongoDB') as MockMongoDB:
        mock_insert_data = MagicMock(return_value={'Status': 'Successfully Inserted!!!', 'Document_id': 'mock_id'})
        MockMongoDB.return_value.insert_data = mock_insert_data
        
        response = client.post("/chat_groq", data=data)

        assert response.status_code == 200
        response_data = response.json()
        assert "Chatbot" in response_data
        assert isinstance(response_data["Chatbot"], str)

def test_text_summarizer_groq():
    data = {
        "input_text": summary_para
    }

    with patch('api.MongoDB') as MockMongoDB:
        mock_insert_data = MagicMock(return_value={'Status': 'Successfully Inserted!!!', 'Document_id': 'mock_id'})
        MockMongoDB.return_value.insert_data = mock_insert_data
        
        response = client.post("/text_summarizer_groq", data=data)
        assert response.status_code == 200
        response_data = response.json()
        assert "Summary" in response_data
        assert isinstance(response_data["Summary"], str)
        assert len(response_data["Summary"]) > 0

def test_summarize_audio():
    audio_file_path = "data/harvard.wav"

    with open(audio_file_path, "rb") as audio_file:
        files = {"audio_file": audio_file}

        with patch('api.MongoDB') as MockMongoDB:
            mock_insert_data = MagicMock(return_value={'Status': 'Successfully Inserted!!!', 'Document_id': 'mock_id'})
            MockMongoDB.return_value.insert_data = mock_insert_data
            
            response = client.post("/summarize_audio", files=files)
            assert response.status_code == 200
            response_data = response.json()
            assert "response" in response_data
            assert isinstance(response_data["response"], str)
            assert len(response_data["response"]) > 0

def test_qa_url_doc_with_url():
    url = ["https://huggingface.co/blog/merve/quantization"]
    prompt = "What is the GPTQ Quantization?"

    data = {
        "url": url,
        "prompt": prompt
    }

    with patch('api.MongoDB') as MockMongoDB:
        mock_insert_data = MagicMock(return_value={'Status': 'Successfully Inserted!!!', 'Document_id': 'mock_id'})
        MockMongoDB.return_value.insert_data = mock_insert_data
        
        response = client.post("/qa_url_doc", data=data)
        assert response.status_code == 200
        response_data = response.json()
        assert "response" in response_data
        assert isinstance(response_data["response"], str)

def test_qa_url_doc_with_document():
    document_file_path = "data/llm.txt"
    prompt = "What is the main point discussed in the document?"

    with open(document_file_path, "rb") as document_file:
        files = {"documents": ("document.txt", document_file, "text/plain")}
        data = {"prompt": prompt}
        with patch('api.MongoDB') as MockMongoDB:
            mock_insert_data = MagicMock(return_value={'Status': 'Successfully Inserted!!!', 'Document_id': 'mock_id'})
            MockMongoDB.return_value.insert_data = mock_insert_data
            
            response = client.post("/qa_url_doc", files=files, data=data)
            assert response.status_code == 200
            response_data = response.json()
            assert "response" in response_data
            assert isinstance(response_data["response"], str)

def test_advance_rag():
    pdf_file = open("data/yolo.pdf", "rb")
    data = {"question": "Summary in 200 words" ,"model": "llama3-70b-8192"}

    with patch('api.MongoDB') as MockMongoDB:
        mock_insert_data = MagicMock(return_value={'Status': 'Successfully Inserted!!!', 'Document_id': 'mock_id'})
        MockMongoDB.return_value.insert_data = mock_insert_data
        
        response = client.post("/advance_rag_llama_index", files={"pdf": pdf_file}, data=data)
        assert response.status_code == 200
        assert "response" in response.json()
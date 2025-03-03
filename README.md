# FastAPI Application

This is a FastAPI application that interfaces with the Langchain Groq API to generate responses based on prompts. The application is designed to be run locally and can be deployed to a cloud environment.

## Features

- **API Key Management**: Uses environment variables to manage API keys and credits.
- **Prompt Generation**: Accepts prompts and generates responses using the Langchain Groq API.
- **Environment Configuration**: Supports local development with `.env` files.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Langchain Groq
- Python-dotenv

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/balajisadanala/FastAPI.git
   cd your-repo
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add your API key and other necessary environment variables:
     ```
     API_KEY=your_groq_api_key
     ```

## Running the Application

1. **Start the FastAPI server**:
   ```bash
   uvicorn main:api_app --reload
   ```

2. **Access the API**:
   - Open your browser and go to `http://127.0.0.1:8000/docs` to view the interactive API documentation.

## API Endpoints

- **POST /generate**: Accepts a prompt and returns a generated response.
  - **Headers**: `X-API-Key` (required)
  - **Body**: JSON object with a `prompt` field.

## Example Request

```bash
curl -X POST "http://127.0.0.1:8000/generate" \
     -H "X-API-Key: your_api_key_here" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Django or FastApi Which is best"}'
```

## Deployment

- This application can be deployed to cloud platforms like Vercel or GCP.
- Ensure environment variables are set in the cloud environment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Langchain Groq](https://langchain-groq.com/)

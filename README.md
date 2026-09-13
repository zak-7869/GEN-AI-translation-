# Gen-AI Translation Application

An intelligent, AI-powered language translation application implemented with state-of-the-art **Generative AI language models**. This system enables accurate context-aware text translation across multiple languages, ensuring structural and cultural tone preservation instead of just word-for-word translation.

## 🚀 Key Features
* **Context-Aware Translation:** Goes beyond basic literal translation by capturing idioms, tone, and contextual meaning using advanced LLMs.
* **Multi-Language Support:** Easily handles seamless translations across a wide array of globally spoken target languages.
* **Clean Interface:** Designed for quick input execution and straightforward localization results.

## 🛠️ Tech Stack
* **Framework:** LangChain (or your preferred LLM orchestration layer)
* **LLM Engine:** Groq / OpenAI / Hugging Face Language Translation Models
* **Language:** Python 3.10+

## 📁 Repository Structure
* `app.py`: The core application script containing the translation logic, system prompt engineering, model setups, and user interface handlers.

## ⚙️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com
cd GEN-AI-translation-
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
*(Note: Adjust based on the actual translation package engine used in your app).*
```bash
pip install langchain langchain-community langchain-groq python-dotenv
```

### 4. Configure Environment Variables
Create a `.env` file in the root folder and add your specific API authorization keys:
```env
GROQ_API_KEY=your_groq_api_key_here
# OR
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the Translation App
```bash
python app.py
```

## 📝 License
This project is open-source and available under the MIT License.

# Cold Email Generator 🚀

A powerful AI-driven application that automatically generates personalized cold emails for job opportunities by analyzing job postings and matching them with your portfolio.

## ✨ Features

- **Intelligent Web Scraping**: Automatically extracts job requirements and company information from job posting URLs
- **AI-Powered Email Generation**: Uses Groq API to create personalized, professional cold emails
- **Portfolio Matching**: Leverages ChromaDB vector database to find relevant projects and skills from your portfolio
- **User-Friendly Interface**: Clean, intuitive Streamlit frontend for easy interaction
- **Customizable Templates**: Flexible email templates that adapt to different job types and industries
- **Real-time Processing**: Fast email generation with immediate preview and editing capabilities

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI/LLM**: Groq API
- **Vector Database**: ChromaDB
- **Web Scraping**: BeautifulSoup4
- **Backend**: Python 3.8+
- **Data Processing**: Pandas, NumPy

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip package manager
- A Groq API key (sign up at [Groq Console](https://console.groq.com/))

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rupayan2005/ML-Project.git
   cd cold email generator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit the `.env` file and add your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```


## 🎯 Usage

1. **Start the application**
   ```bash
   cd app
   streamlit run main.py
   ```

2. **Upload your portfolio**
   - Navigate to the app/resource folder and add your Portfolios in a CSV file with the Techstack and Links
   - The system will automatically process and store them in ChromaDB

3. **Generate cold emails**
   - Paste the job posting URL in the input field
   - Click "Analyze Job Posting"
   - Copy the generated email to your clipboard

## 📁 Project Structure

```
cold email generator/
├── app/
│   ├── main.py                         # Web scraping functionality and Streamlit UI
│   ├── chains.py                       # AI email generation logic
│   ├── portfolio.py                    # Portfolio and ChromaDB operations
│   ├── utils.py                        # Utility functions
│   └── resource/
│          ├── my_portfolio.csv         # Dummy portfolio
├── requirements.txt                    # Python dependencies
├── .env.example                        # Environment variables template
└── README.md                           # This file
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key for AI generation | Yes |
| `CHROMA_PERSIST_DIR` | ChromaDB storage directory | No (default: ./chroma_db) |


## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 🐛 Troubleshooting

### Common Issues

**ChromaDB Installation Error**
```bash
pip install --upgrade chromadb
```

**Groq API Rate Limits**
- Implement request throttling in your code
- Consider upgrading your Groq plan for higher limits

**Web Scraping Blocked**
- Some sites may block automated requests
- Try using different user agents or rotating proxies
- Respect robots.txt and rate limits


## 🔒 Privacy & Ethics

- Always respect website terms of service
- Be mindful of rate limiting and don't overwhelm servers
- Ensure compliance with data protection regulations
- Use generated emails responsibly and authentically


## 🙏 Acknowledgments

- [Groq](https://groq.com/) for providing fast AI inference
- [ChromaDB](https://www.trychroma.com/) for vector database capabilities
- [Streamlit](https://streamlit.io/) for the amazing web framework
- The open-source community for inspiration and tools


---

⭐ **If you find this project helpful, please consider giving it a star on GitHub!** ⭐
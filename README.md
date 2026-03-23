# YT-MINER - YouTube Toxicity Miner

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

A tool for mining and analyzing YouTube comments to detect toxicity levels in video discussions.

## 📋 Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## ✨ Features
- Extract comments from YouTube videos
- Analyze toxicity levels using AI/ML models
- Bulk processing capabilities
- GUI interface for easy interaction
- Export results in various formats

## 🔧 Prerequisites
- Python 3.10 or higher
- YouTube Data API v3 key
- Internet connection

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/wildtigress/YOUTUBE-TOXICITY-MINER.git
cd YOUTUBE-TOXICITY-MINER
2. Create and activate virtual environment
bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
bash
pip install -r requirements.txt
4. Set up environment variables
Copy the example environment file and add your API keys:

bash
cp .env.example .env
Edit .env and add your YouTube API key:

env
YOUTUBE_API_KEY=your_api_key_here
# Add other configuration variables as needed
🚀 Usage
GUI Mode
Run the graphical interface:

bash
python gui.py
Command Line Mode
Process a single video:

bash
python miner.py [VIDEO_URL] [OPTIONS]
Bulk Processing
Process multiple videos from a list:

bash
python bulk.py --file videos.txt --output results.csv
Using the src module
bash
python src/gui.py
📁 Project Structure
text
YT-MINER/
├── src/
│   └── gui.py              # GUI source code
├── gui.py                   # Main GUI launcher
├── miner.py                 # Core mining functionality
├── bulk.py                  # Bulk processing script
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variables template
├── LICENSE                  # MIT License
└── README.md               # This file
⚙️ Configuration
Required Environment Variables
Variable	Description	Required
YOUTUBE_API_KEY	YouTube Data API v3 key	Yes
DATABASE_URL	Optional database connection	No
LOG_LEVEL	Logging level (INFO, DEBUG, etc.)	No
YouTube API Setup
Go to Google Cloud Console

Create a new project or select existing

Enable YouTube Data API v3

Create credentials (API Key)

Copy the API key to your .env file

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 License
Distributed under the MIT License. See LICENSE file for more information.

⚠️ Disclaimer
This tool is for educational and research purposes only. Please ensure you comply with:

YouTube's Terms of Service

Google API Services User Data Policy

Applicable data protection laws (GDPR, CCPA, etc.)

📧 Contact
wildtigress - @wildtigress

Project Link: https://github.com/wildtigress/YOUTUBE-TOXICITY-MINER

🙏 Acknowledgments
YouTube Data API team

Open source community

All contributors

Made with ❤️ for a safer YouTube community

text

## Additional Files to Create

### `.env.example`
Create this file to help others set up their environment:

```env
# YouTube API Configuration
YOUTUBE_API_KEY=your_youtube_api_key_here

# Optional Configuration
DATABASE_URL=sqlite:///comments.db
LOG_LEVEL=INFO

# Rate Limiting (requests per second)
RATE_LIMIT=1

# Output Settings
OUTPUT_FORMAT=json
Update requirements.txt
Make sure your requirements.txt includes all dependencies. Here's a sample:

txt
google-api-python-client>=2.100.0
pandas>=2.0.0
python-dotenv>=1.0.0
requests>=2.31.0
To Add the README to Your Repository
Option 1: Via GitHub Website
Go to your repository

Click "Add file" → "Create new file"

Name it README.md

Copy and paste the content above

Scroll down and click "Commit changes"

Option 2: Via Command Line
bash
# Create the README file
nano README.md
# (Copy and paste the content above, save and exit)

# Or create it directly
echo "# YT-MINER - YouTube Toxicity Miner" > README.md

# Add and commit
git add README.md
git commit -m "Add comprehensive README"
git push

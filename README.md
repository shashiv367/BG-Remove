# BG Remover — Background Removal Tool

Remove image backgrounds instantly. Upload any image, preview the result side-by-side, and download a crisp PNG with full transparency.

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip

### Local Development

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/BG-remover.git
cd BG-remover

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

## 🌐 Deploy to Render

1. Push your code to GitHub
2. Go to [render.com](https://render.com) and create a **New Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120`
   - **Instance Type**: Free (or paid for better performance)
5. Click **Create Web Service**

> ⚠️ **Note**: The first request may be slow as rembg downloads the processing model (~170MB). Subsequent requests will be faster.

## 📁 Project Structure

```
BG-remover/
├── app.py              # Flask backend
├── requirements.txt    # Python dependencies
├── Procfile           # Render deployment config
├── render.yaml        # Render blueprint (optional)
├── .gitignore         # Git ignore rules
├── README.md          # This file
├── templates/
│   └── index.html     # Frontend UI
└── processed/         # Temporary processed images
```

## 🛠 Tech Stack

- **Backend**: Flask + Gunicorn
- **Processing**: rembg
- **Image Processing**: Pillow
- **Frontend**: Vanilla HTML/CSS/JS
- **Deployment**: Render

## 📄 License

MIT License — feel free to use this project however you'd like.

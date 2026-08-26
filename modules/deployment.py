def generate_deployment_guide_text() -> str:
    """
    Returns deployment commands and cloud hosting steps for Streamlit deployment.
    """
    return """
### 🚀 Local Installation & Setup

1. **Clone Repository & Navigate to Workspace**:
   ```bash
   git clone https://github.com/your-username/HomeValue-AI.git
   cd HomeValue-AI
   ```

2. **Create & Activate Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Streamlit Dashboard**:
   ```bash
   streamlit run app.py
   ```

---

### ☁️ Cloud Deployment (Streamlit Community Cloud)

1. Push complete codebase to **GitHub** repository.
2. Sign in to **[share.streamlit.io](https://share.streamlit.io)** with GitHub.
3. Click **New App**, select `HomeValue-AI` repository, and set main file path to `app.py`.
4. Click **Deploy!**
"""

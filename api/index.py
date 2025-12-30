import sys
from pathlib import Path

# Add the server directory to the Python path
server_path = Path(__file__).parent.parent / "server"
sys.path.insert(0, str(server_path))

from main import app

# Vercel serverless function handler
handler = app

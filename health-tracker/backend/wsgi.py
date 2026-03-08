# from app import create_app

# app = create_app()

from app import create_app
import os
from dotenv import load_dotenv
load_dotenv()

app = create_app()
print("JWT KEY LENGTH:", len(os.getenv("JWT_SECRET_KEY", "")))  # Should print >= 32
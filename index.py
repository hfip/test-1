# index.py
import os
import sys

# إجبار فيرسل على رؤية المجلد المحلي
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from vipertls.solver.server import app

# إعدادات لوحة التحكم
app.docs_url = "/docs"
app.openapi_url = "/openapi.json"
app.setup_openapi()

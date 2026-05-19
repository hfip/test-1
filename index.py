# index.py
import os
import sys

# إجبار سيرفر فيرسل على قراءة الجذر الرئيسي لكي يرى مجلد vipertls بدون مشاكل
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from vipertls.solver.server import app

# تفعيل لوحة التحكم التفاعلية docs إجبارياً
app.docs_url = "/docs"
app.openapi_url = "/openapi.json"
app.setup_openapi()

# index.py
import os
import sys
from types import ModuleType

# --- الخدعة البرمجية لمنع انهيار السيرفر بسبب مكتبة Playwright غائبة ---
class DummyModule(ModuleType):
    def __getattr__(self, name):
        return DummyModule(name)
    def __call__(self, *args, **kwargs):
        return DummyModule()

sys.modules['playwright'] = DummyModule('playwright')
sys.modules['playwright.async_api'] = DummyModule('playwright.async_api')
sys.modules['playwright_stealth'] = DummyModule('playwright_stealth')

# إجبار فيرسل على قراءة المسار المحلي لرؤية مجلد vipertls
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from vipertls.solver.server import app

# تفعيل لوحة التحكم التفاعلية بالشكل القياسي الصحيح لـ FastAPI
app.docs_url = "/docs"
app.openapi_url = "/openapi.json"

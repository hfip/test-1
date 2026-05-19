# index.py
import os
import sys
from types import ModuleType

# --- الخدعة البرمجية لمنع انهيار السيرفر على فيرسل بسبب Playwright ---
class DummyModule(ModuleType):
    def __getattr__(self, name):
        return DummyModule(name)
    def __call__(self, *args, **kwargs):
        return DummyModule()

# حقن مكتبات وهمية في النظام لإقناع الكود الداخلي بأنها مثبتة بسلام
sys.modules['playwright'] = DummyModule('playwright')
sys.modules['playwright.async_api'] = DummyModule('playwright.async_api')
sys.modules['playwright_stealth'] = DummyModule('playwright_stealth')

# إجبار فيرسل على قراءة المسار المحلي
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from vipertls.solver.server import app

# تفعيل لوحة التحكم إجبارياً
app.docs_url = "/docs"
app.openapi_url = "/openapi.json"
app.setup_openapi()

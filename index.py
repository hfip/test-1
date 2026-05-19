# index.py
from vipertls.solver.server import app

# تفعيل لوحة التحكم التفاعلية docs إجبارياً على السيرفر السحابي
app.docs_url = "/docs"
app.openapi_url = "/openapi.json"
app.setup_openapi()

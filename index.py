# index.py
import os
import sys
import time
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# إجبار فيرسل على قراءة المسار الرئيسي
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from vipertls.client import AsyncClient

app = FastAPI(title="ViperSolverr Cloud Pure TLS", docs_url="/docs", openapi_url="/openapi.json")

class SolveRequest(BaseModel):
    url: str
    user_agent: Optional[str] = None
    preset: str = "edge_133"
    timeout: int = 30

class SolveResponse(BaseModel):
    url: str
    status: int
    html: str
    cookies: dict[str, str]
    user_agent: str
    method: str
    elapsed_ms: float

@app.post("/solve", response_model=SolveResponse)
async def solve(req: SolveRequest) -> SolveResponse:
    t0 = time.perf_counter()
    ua = req.user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    
    headers = {
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ar,en-US;q=0.7,en;q=0.3",
        "Referer": "https://m.asd.ink/home7/"
    }
    
    try:
        async with AsyncClient(impersonate=req.preset, timeout=req.timeout) as client:
            r = await client.get(req.url, headers=headers)
            elapsed = (time.perf_counter() - t0) * 1000
            
            return SolveResponse(
                url=str(r.url),
                status=r.status_code,
                html=r.content.decode('utf-8', errors='ignore'),
                cookies={},
                user_agent=ua,
                method="pure_tls_cloud",
                elapsed_ms=elapsed
            )
            
    except Exception as exc:
        elapsed = (time.perf_counter() - t0) * 1000
        return SolveResponse(
            url=req.url,
            status=502,
            html=f"<h1>ViperTLS Cloud Error</h1><p>{str(exc)}</p>",
            cookies={},
            user_agent=ua,
            method="failed",
            elapsed_ms=elapsed
        )

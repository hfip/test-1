# vipertls/__init__.py
from .client import AsyncClient, Client
from .tui import ViperDashboard
from .core.response import ViperResponse, ViperHTTPError, ViperConnectionError, ViperTimeoutError
from .fingerprints.presets import resolve_preset, PRESETS, BrowserPreset
from .runtime import describe_runtime_paths

# حماية الاستدعاء سحابياً: إذا لم تتوفر مكتبة playwright يتخطاها النظام بسلام
try:
    from .solver.browser import clear_cache as clear_solver_cache
except (ImportError, ModuleNotFoundError):
    def clear_solver_cache(*args, **kwargs):
        return None

__version__ = "0.1.8"
__all__ = [
    "AsyncClient",
    "Client",
    "ViperDashboard",
    "ViperResponse",
    "ViperHTTPError",
    "ViperConnectionError",
    "ViperTimeoutError",
    "resolve_preset",
    "PRESETS",
    "BrowserPreset",
    "get_runtime_paths",
    "clear_solver_cache",
]

def get_runtime_paths() -> dict[str, str]:
    return describe_runtime_paths()

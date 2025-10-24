from __future__ import annotations
import time
from typing import Dict, Any

TOOL_DESCRIPTOR: Dict[str, Any] = {
    "name": "get_current_time",
    "description": "get_current time for a given timezone.",
    "inputs": [
        {"name": "timezone", "type": "string", "required": True, "description": "Timezone identifier (e.g, 'UTC', 'EST')"}  
    ],
    "outputs":{
        "type": "object",
        "properties": {
            "timezone": {"type": "string"},
            "current_time": {"type": "string"},
        },
    }
}

def invoke_get_current_time(timezone: str = "UTC") -> Dict[str, Any]:
    """Returns the current time in a specified timezone (Mock)"""
    if not timezone:
        raise ValueError("Tomezone parameter is required.")
    
    return {
        "timezone": timezone.upper(),
        "current_time": time.strftime("%H:%M:%S", time.gmtime()),
        "source": "mock-time-service"
    }
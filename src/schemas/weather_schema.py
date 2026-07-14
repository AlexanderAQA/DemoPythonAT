WEATHER_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "latitude": {"type": "number"},
        "longitude": {"type": "number"},
        "generationtime_ms": {"type": "number"},
        "utc_offset_seconds": {"type": "integer"},
        "timezone": {"type": "string"},
        "timezone_abbreviation": {"type": "string"},
        "elevation": {"type": "number"},
        "current_units": {
            "type": "object",
            "properties": {
                "time": {"type": "string"},
                "interval": {"type": "string"},
                "temperature_2m": {"type": "string"},
                "relative_humidity_2m": {"type": "string"}
            },
            "required": ["time", "interval", "temperature_2m", "relative_humidity_2m"]
        },
        "current": {
            "type": "object",
            "properties": {
                "time": {"type": "string", "format": "date-time"},
                "interval": {"type": "integer"},
                "temperature_2m": {"type": "number"},
                "relative_humidity_2m": {"type": "number"}
            },
            "required": ["time", "interval", "temperature_2m", "relative_humidity_2m"]
        }
    },
    "required": ["latitude", "longitude", "timezone", "current"]
}


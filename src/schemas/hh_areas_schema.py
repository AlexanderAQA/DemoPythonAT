HH_AREAS_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "parent_id": {"type": ["string", "null"]},  # У стран null, у регионов — ID родителя
            "areas": {"type": "array"},  # Регионы
            "utc_offset": {"type": "string"},  # Пример: "+05:00"
            "lat": {"type": "number"},  # Широта
            "lng": {"type": "number"}   # Долгота
        },
        "required": ["id", "name"],  # Поля, которые точно есть
        "additionalProperties": True  # API может добавлять новые поля - тут разрешить лишнее
    },
    "minItems": 1  # Должен быть хотя бы один элемент
}

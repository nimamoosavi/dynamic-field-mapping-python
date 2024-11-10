import json
from typing import List, Dict

class FileProcessor:
    def __init__(self, mapping_service):
        self.mapping_service = mapping_service

    def process_file(self, system_name: str, file_headers: List[str], row_data: List[str]) -> str:
        field_mapping = self.mapping_service.get_field_mapping(system_name)
        payload = {"Profile": {}}

        for i, header in enumerate(file_headers):
            mapped_field = field_mapping.get(header)
            if mapped_field:
                self._map_field(payload["Profile"], mapped_field, row_data[i])

        return json.dumps({"payload": payload})

    def _map_field(self, parent: Dict, mapped_field: str, value: str):
        fields = mapped_field.split('.')
        self._set_nested_field(parent, fields, value)

    def _set_nested_field(self, parent: Dict, fields: List[str], value: str):
        for field in fields[:-1]:
            parent = parent.setdefault(field, {})
        parent[fields[-1]] = value


import json

class FileProcessor:
    def __init__(self, mapping_service):
        self.mapping_service = mapping_service

    def process_file(self, system_name, file_headers, row_data):
        field_mapping = self.mapping_service.get_field_mapping(system_name)

        payload = {"Profile": {}}
        for i, header in enumerate(file_headers):
            mapped_field = field_mapping.get(header)
            if mapped_field:
                payload["Profile"][mapped_field] = row_data[i]

        return json.dumps({"payload": payload})

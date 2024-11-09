class MappingService:
    def __init__(self, mapping_data):
        self.mapping_data = mapping_data

    def get_field_mapping(self, system_name):
        return self.mapping_data.get(system_name, {})

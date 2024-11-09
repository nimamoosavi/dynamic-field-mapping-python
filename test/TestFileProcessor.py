import unittest

from app.fileprocessor.file_processor import FileProcessor
from app.mapping.MappingService import MappingService


class TestFileProcessor(unittest.TestCase):
    def test_process_file(self):
        mapping_service = MappingService({
            "SystemA": {"FirstName": "firstname", "LastName": "lastname"}
        })
        file_processor = FileProcessor(mapping_service)
        file_headers = ["FirstName", "LastName"]
        row_data = ["John", "Doe"]
        result = file_processor.process_file("SystemA", file_headers, row_data)

        expected_result = '{"payload": {"Profile": {"firstname": "John", "lastname": "Doe"}}}'
        self.assertEqual(result, expected_result)

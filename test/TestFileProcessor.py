import unittest
from unittest.mock import Mock
from app.fileprocessor.file_processor import FileProcessor
import json


class TestFileProcessor(unittest.TestCase):

    def setUp(self):
        self.mapping_service = Mock()

        self.file_processor = FileProcessor(self.mapping_service)

    def test_process_file_with_system_a(self):
        # Sample field mapping for System A
        self.mapping_service.get_field_mapping.return_value = {
            "FirstName": "firstname",
            "LastName": "lastname",
            "CustomerId": "customerId",
            "status": "status",
            "addressLine": "address.addressLine",
            "City": "address.city",
            "Province": "address.province",
            "PostalCode": "address.postalCode"
        }

        # Sample file headers and row data for System A
        file_headers = ["FirstName", "LastName", "CustomerId", "status", "addressLine", "City", "Province",
                        "PostalCode"]
        row_data = ["John", "Doe", "12345", "active", "123 Main St", "Toronto", "ON", "M5A 1A1"]

        # Expected JSON output
        expected_output = {
            "payload": {
                "Profile": {
                    "firstname": "John",
                    "lastname": "Doe",
                    "customerId": "12345",
                    "status": "active",
                    "address": {
                        "addressLine": "123 Main St",
                        "city": "Toronto",
                        "province": "ON",
                        "postalCode": "M5A 1A1"
                    }
                }
            }
        }

        result = self.file_processor.process_file("System A", file_headers, row_data)

        result_dict = json.loads(result)

        # Assert that the result matches the expected output
        self.assertEqual(result_dict, expected_output)

    def test_process_file_with_system_b(self):
        # Sample field mapping for System B (different order of fields)
        self.mapping_service.get_field_mapping.return_value = {
            "CustomerId": "customerId",
            "FirstName": "firstname",
            "status": "status",
            "LastName": "lastname",
            "addressLine": "address.addressLine",
            "City": "address.city",
            "Province": "address.province",
            "PostalCode": "address.postalCode"
        }

        # Sample file headers and row data for System B
        file_headers = ["CustomerId", "FirstName", "status", "LastName", "addressLine", "City", "Province",
                        "PostalCode"]
        row_data = ["12345", "John", "active", "Doe", "123 Main St", "Toronto", "ON", "M5A 1A1"]

        # Expected JSON output (same structure but different field order)
        expected_output = {
            "payload": {
                "Profile": {
                    "firstname": "John",
                    "lastname": "Doe",
                    "customerId": "12345",
                    "status": "active",
                    "address": {
                        "addressLine": "123 Main St",
                        "city": "Toronto",
                        "province": "ON",
                        "postalCode": "M5A 1A1"
                    }
                }
            }
        }

        result = self.file_processor.process_file("System B", file_headers, row_data)

        result_dict = json.loads(result)

        # Assert that the result matches the expected output
        self.assertEqual(result_dict, expected_output)

    def test_process_file_with_missing_field(self):
        # Sample field mapping with missing field in the file headers
        self.mapping_service.get_field_mapping.return_value = {
            "FirstName": "firstname",
            "LastName": "lastname",
            "CustomerId": "customerId",
            "status": "status",
            "addressLine": "address.addressLine",
            "City": "address.city",
            "Province": "address.province",
            "PostalCode": "address.postalCode"
        }

        file_headers = ["FirstName", "LastName", "CustomerId", "addressLine", "City", "Province", "PostalCode"]
        row_data = ["John", "Doe", "12345", "123 Main St", "Toronto", "ON", "M5A 1A1"]

        # Expected JSON output (status should not be included)
        expected_output = {
            "payload": {
                "Profile": {
                    "firstname": "John",
                    "lastname": "Doe",
                    "customerId": "12345",
                    "address": {
                        "addressLine": "123 Main St",
                        "city": "Toronto",
                        "province": "ON",
                        "postalCode": "M5A 1A1"
                    }
                }
            }
        }

        result = self.file_processor.process_file("System A", file_headers, row_data)

        result_dict = json.loads(result)

        # Assert
        self.assertEqual(result_dict, expected_output)


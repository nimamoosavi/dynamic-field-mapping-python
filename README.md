# Dynamic Field Mapping for Inconsistent File Formats

## Overview

This solution provides a flexible approach to mapping data from various file formats to a unified JSON schema, which can then be stored in a database. Using a configuration-based mapping approach, it addresses challenges with field order variations and new file format integrations. Key features include:

1. **Mapping Configuration File**: Define a JSON configuration file to map fields from incoming files to the target JSON schema. This file is easily updatable for new systems, eliminating the need for code changes.

2. **Dynamic Mapping**: Load the configuration at runtime. For each file, the system applies the correct mapping for the specified system to transform fields to the unified JSON structure.

3. **Automatic Header-Based Field Mapping**: The system reads file headers and maps fields to JSON schema fields based on the configuration, accommodating any order of fields.

4. **Database Persistence**: After mapping, the data is stored in a standardized format in the database.

## Detailed Implementation Steps

### 1. Configuration File

Define a JSON configuration file specifying the mappings for each system. For example:

```json
{
  "SystemA": {
    "FirstName": "firstname",
    "LastName": "lastname",
    "CustomerId": "customerId",
    "status": "status",
    "addressLine": "address.addressLine",
    "City": "address.city",
    "Province": "address.province",
    "PostalCode": "address.postalCode"
  },
  "SystemB": {
    "CustomerId": "customerId",
    "FirstName": "firstname",
    "status": "status",
    "LastName": "lastname",
    "addressLine": "address.addressLine",
    "City": "address.city",
    "Province": "address.province",
    "PostalCode": "address.postalCode"
  }
}
```
Each mapping defines how fields from a specific system (e.g., System A, System B) should map to a unified JSON structure. New mappings can be added here for any new systems.
This file based on structure can be stored anywhere such as Databases, files, etc.

### 2. Dynamic Mapping Logic (Mapping)

- Load the JSON configuration file into a Map or other structure types when the application starts.
- For each file processed, select the correct mapping configuration.
- Use this mapping to transform fields from the incoming file into the target JSON structure, regardless of field order.

### 3. File Parsing and Mapping (File Processor)

- Read File Headers: Identify the order of fields in the incoming file.
- Apply Mapping: Using the loaded configuration, map each field to the JSON schema based on its header, even if fields are in different orders.
- Convert to Database model: Convert the JSON structure to a Schema for database storage once mapped.


Example JSON Output
After mapping, the output JSON for a row might look like this:
```json
{
  "payload": {
    "Profile": {
      "firstname": "Nima",
      "lastname": "M",
      "customerId": "12345",
      "status": "Active",
      "address": {
        "addressLine": "123 St",
        "city": "Toronto",
        "province": "ON",
        "postalCode": "A1B2C3"
      }
    }
  }
}
```

### 4. Database Insertion (Persistence)
Based on structure can be mapped result to add to DataBases
- Profile that matches the JSON schema.


## Service Documentation

### Mapping

The MappingService provides a contract for retrieving field mappings based on system names. This service is designed to fetch mappings that allow fields to be mapped between different systems in the application.
in our scenario load a JSON file Structure from JSON Configuration File or DataBases


### Processor
The FileProcessor is responsible for handling and transforming data or executing specific workflows based on configured mappings. It interacts with MappingService to retrieve field mappings and uses them to process data for various systems, allowing seamless data transformations across different system formats.

### Persistence (Optional)

The **Persistence** package is responsible for managing the interaction between the application and the database. It contains the model, and services related to persisting and retrieving data. In this package.


### JSON Configuration File Structure
The JSON file used by MappingService (mappings.json) should have the following structure:

```json
{
  "SystemA": {
    "FirstName": "firstname",
    "LastName": "lastname"
  },
  "SystemB": {
    "FirstName": "first_name",
    "LastName": "last_name"
  }
}
```

### Test Explanation
all test files are in the test directory.

import yaml
from schema import Schema, And, Use, Optional, SchemaError, SchemaWrongKeyError

with open('test_file.yaml', 'r') as file:
  test_file = yaml.safe_load(file)

# print('Test file:')
# print(test_file)

def validate(schema_defn, test_file_in):
  try:
    result = schema_defn.validate(test_file_in)
    print(f"INFO: File passes schema validation. Result:\n{result}")
  except SchemaWrongKeyError as e:
    print(f"WARNING: Unknown key. Do you need to add a new field to the schema?\n  DETAILS: {e}")
  except SchemaError as e:
    print(f"Generic schema ERROR: File does not pass schema validation.\n  DETAILS: {e}")

schema_def = Schema({
  "main_key": {
    "a_list": [str],
    "complex": {
      "float_field": float,
      "int_field": int,
      "str_field": str,
    }
  }
})

validate(schema_def, test_file)

completely_different_schema_def = Schema({
  "secondary_key": int
})

validate(completely_different_schema_def, test_file)


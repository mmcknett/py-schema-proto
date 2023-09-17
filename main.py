import yaml
from schema import Schema, And, Use, Optional, SchemaError, SchemaWrongKeyError

with open('test_file.yaml', 'r') as file:
  test_file = yaml.safe_load(file)

# print('Test file:')
# print(test_file)

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

try:
  result = schema_def.validate(test_file)
  print(result)
except SchemaError as e:
  if isinstance(e, SchemaWrongKeyError):
    print(f"WARNING: Unknown key. Do you need to add a new field to the schema?\n{e}")
  else:
    print(f"Generic schema validation error:\n\t{e}")




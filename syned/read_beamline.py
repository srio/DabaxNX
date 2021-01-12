from syned.util.json_tools import load_from_json_file

syned_obj = load_from_json_file("beamline.json")

print(type(syned_obj))
print(syned_obj.info())
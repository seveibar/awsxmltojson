import os
import importlib.util
import json
from awsxmltojson import convert_xml_to_dict

samples_dir = os.path.join(os.path.dirname(__file__), "tests", "samples")

test_files = [fi for fi in os.listdir(samples_dir) if fi.startswith("test_")]

sample_doc = ""


for test_file in test_files:
    module_name = test_file.replace(".py", "").replace("test_", "").replace("_", ".")
    spec = importlib.util.spec_from_file_location(
        module_name,
        os.path.abspath(os.path.join(samples_dir, test_file)),
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if hasattr(mod, "sample_input"):
        json_string = json.dumps(convert_xml_to_dict(mod.sample_input), indent=4)
        sample_doc += f"""
### {module_name}

```xml
{mod.sample_input}
```

```json
{json_string}
```
"""

og_readme_lines = open("./README.md").read().split("\n")
new_readme_lines = []

write_og_lines = True
for line in og_readme_lines:
    if write_og_lines:
        new_readme_lines.append(line)
    if "GENERATED_SAMPLE_DOCS_START" in line:
        write_og_lines = False
        new_readme_lines += sample_doc.split("\n")
    if "GENERATED_SAMPLE_DOCS_STOP" in line:
        write_og_lines = True
        new_readme_lines.append("<!-- GENERATED_SAMPLE_DOCS_STOP -->")

open("./README.md", "w").write("\n".join(new_readme_lines)

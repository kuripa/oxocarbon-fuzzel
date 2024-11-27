import yaml
from pystache import Renderer
from pathlib import Path

# Paths
yaml_file = Path("base16-oxocarbon/base16-oxocarbon-dark.yaml") # Color scheme file
templates_dir = Path("templates/")                              # Directory with Mustache templates
output_dir = Path("output/")                                    # Output directory for INI files

output_dir.mkdir(exist_ok=True)

with open(yaml_file, "r") as file:
    colors = yaml.safe_load(file)

# Append 'ff' to each hex color for RGBA
for key, value in colors.items():
    if isinstance(value, str) and len(value) == 6:  # Ensure it's a 6-character hex string
        colors[key] = value + "ff"  # Add full opacity for RGBA

renderer = Renderer()

for template_file in templates_dir.glob("*.mustache"):
    with open(template_file, "r") as file:
        template = file.read()

    rendered = renderer.render(template, colors)

    output_file = output_dir / f"{template_file.stem}.ini"
    with open(output_file, "w") as file:
        file.write(rendered)

    print(f"Generated {output_file}")

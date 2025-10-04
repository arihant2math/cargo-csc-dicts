import os
from pathlib import Path
import json
import jstyleson

# pub name: String,
# #[serde(default)]
# pub description: Option<String>,
# pub paths: Vec<String>,
# #[serde(default)]
# pub case_sensitive: bool,
# #[serde(default)]
# pub no_cache: bool,
# #[serde(default)]
# pub globs: Vec<String>,

root = Path("../cspell-dicts/dictionaries/")

for dir in root.iterdir():
    # Check if it's a directory
    if dir.is_dir():
        # check if src/ exists in the directory
        if dir.joinpath('src/').exists():
            print(f"Processing directory: {dir.name}")
            description = None
            name = dir.name
            if dir.joinpath('cspell-ext.json').exists():
                with open(dir.joinpath('cspell-ext.json')) as f:
                    data = jstyleson.load(f)
                    name = data.get('name', dir.name)
                    description = data.get('description', None)
            files = []
            # Iterate through files in src/
            for file in dir.joinpath('src/').iterdir():
                # Check if the file ends with .txt
                if file.suffix == '.txt' and not ('exclude' in file.name):
                    # normalize the path to be relative to dir
                    files.append(file.relative_to(dir))
            config = {
                "name": name,
                "description": description,
                "paths": [str(f) for f in files],
            }
            # make dicts/{dir.name} if it doesn't exist
            out_dir = Path("dicts/") / dir.name
            out_dir.mkdir(parents=True, exist_ok=True)
            # write config to dicts/{dir.name}/config.json
            with open(out_dir / 'csc-config.json', 'w') as f:
                json.dump(config, f, indent=4)
            # copy all .txt files to dicts/{dir.name}/
            out_src = out_dir / 'src'
            out_src.mkdir(parents=True, exist_ok=True)
            for file in files:
                with open(dir / file, 'r', encoding='utf-8') as src_f:
                    with open(out_src / file.name, 'w', encoding='utf-8') as dest_f:
                        dest_f.write(src_f.read())
            print(f"Processed and copied files for: {dir.name}")
        else:
            print(f"Skipping directory (no src/): {dir.name}")

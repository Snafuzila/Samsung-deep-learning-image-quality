import json
from pathlib import Path
import shutil
from tqdm import tqdm

with open('./metadata.json' , 'r') as f:
    data = json.load(f)

image_paths = r'D:\dataset\samsung_artifacts_official\samsung_artifacts\crops'
new_image_path = r'D:\dataset\samsung_artifacts_official\samsung_artifacts'
collected_data={}

for item in tqdm(data, desc="Processing Images", unit="img"):
    img_id = list(item.keys())[0]
    info = item[img_id]
    artifact_name = info['artifact']
    folder_path = Path(f'{new_image_path}/sorted/{artifact_name}')
    folder_path.mkdir(parents=True, exist_ok=True)
    old_path = Path(f'{image_paths}/{img_id}.png')
    new_path = Path(f'{folder_path}/{img_id}.png')

    if old_path.exists():
        shutil.copy2(old_path, new_path)
        print(f"Copied: {img_id}.png to {artifact_name}")
    if artifact_name not in collected_data:
        collected_data[artifact_name] = []

    collected_data[artifact_name].append({img_id:info})

for art_name, images_list in collected_data.items():
    json_path = Path(f'{new_image_path}/sorted/{art_name}/metadata.json')
    with open(json_path, 'w') as f_out:
        json.dump(images_list, f_out, indent=4)

    print(f"Created metadata for {art_name}")

















































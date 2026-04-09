import shutil, os

# Copy Kenya images to the project directory
kenya_imgs = [
    'masai-mara-lion-cubs-safari-wildlife.jpg',
    'masai-mara-male-lion-golden-plains-safari.jpg',
    'male-lion-masai-mara-safari-landscape.jpg',
    'flamingos-lake-nakuru-kenya.jpg',
    'lake-nakuru-kenya-flamingos-aerial-view.jpg',
    'black-rhino-ol-pejeta-kenya-safari.jpg',
    'rhinos-ol-pejeta-kenya-safari.jpg',
    'ol-pejeta-rhino-kenya-safari-encounter.jpg',
    'reticulated-giraffe-samburu-kenya-safari.jpg',
    'reticulated-giraffe-samburu-kenya-savanna.jpg',
    'nairobi-kenya-city-skyline-at-night.jpg',
    'nairobi-kenya-skyline-cityscape.jpg',
    'luxury-kenya-safari-lodge-tent-sunset.jpg',
    'luxury-kenya-safari-tent-camp-sunset.jpg',
]

os.makedirs('/workspace/kenya-safari-2026/imgs', exist_ok=True)
for img in kenya_imgs:
    src = f'/workspace/imgs/{img}'
    dst = f'/workspace/kenya-safari-2026/imgs/{img}'
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f'Copied: {img}')
    else:
        print(f'NOT FOUND: {img}')

print('Done copying images')

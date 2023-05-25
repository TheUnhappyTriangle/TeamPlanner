import requests

def download_gif(url, destination_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {destination_path}")
    else:
        print(f"Failed to download: {url}")

base_url = 'https://projectpokemon.org/images/sprites-models/bw-animated/'
destination_folder = 'C:/CodingRepos/Web/TeamPlannerApp/images/sprites/gen5/BW/reg/anim/'

for i in range(1, 650):
    gif_name = str(i).zfill(3)
    gif_url = f"{base_url}{gif_name}.gif"
    destination_file = f"{destination_folder}{i}.gif"
    download_gif(gif_url, destination_file)

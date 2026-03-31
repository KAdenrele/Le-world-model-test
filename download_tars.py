import os
import subprocess
from huggingface_hub import hf_hub_download, list_repo_files
from dotenv import load_dotenv
import shutil

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

datasets_repos = [
    "quentinll/lewm-tworooms",
    "quentinll/lewm-cube",
    "quentinll/lewm-pusht",
    "quentinll/lewm-reacher",
]
DOWNLOAD_DIR = "/app/files/downloads"
STABLE_DIR = "/app/files"
os.makedirs(STABLE_DIR, exist_ok=True)

for repo_id in datasets_repos:
    print(f"Processing dataset: {repo_id}")
    try:
        # Dynamically find the .tar.zst file in the repository
        repo_files = list_repo_files(repo_id=repo_id, repo_type="dataset", token=HF_TOKEN)
        archive_files = [f for f in repo_files if f.endswith(".zst")]

        if not archive_files:
            print(f"  No '.zst' archive found in {repo_id}. Skipping.")
            continue

        archive_filename = archive_files[0]
        if len(archive_files) > 1:
            print(f"  Warning: Multiple '.zst' archives found. Using '{archive_filename}'.")

        archive_path = hf_hub_download(
            repo_id=repo_id,
            filename=archive_filename,
            repo_type="dataset",
            token=HF_TOKEN,
            cache_dir=DOWNLOAD_DIR,
        )
        print(f"  Downloaded {archive_filename} to {archive_path}")
        print(f"  Extracting to {STABLE_DIR}")
        
        if archive_path.endswith(".tar.zst"):
            cmd = ["tar", "--zstd", "-xvf", archive_path, "-C", STABLE_DIR]
        else:
            output_filename = os.path.basename(archive_path).replace(".zst", "")
            output_path = os.path.join(STABLE_DIR, output_filename)
            # Use -f (force) to ensure zstd processes it and overwrites if needed
            cmd = ["zstd", "-d", "-f", archive_path, "-o", output_path]

        print(f"  Extracting real file: {archive_path}")
        subprocess.run(cmd, check=True)
    except Exception as e:
        print(f"An error occurred while processing {repo_id}: {e}")
        
shutil.rmtree(DOWNLOAD_DIR)
print("All datasets have been processed.")
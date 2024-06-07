from huggingface_hub import snapshot_download

model_id="Orenguteng/Llama-3-8B-Lexi-Uncensored"

snapshot_download(repo_id=model_id, local_dir="~/models/llama-3-8B-Lexi-Uncensored", local_dir_use_symlinks=False, revision="main")

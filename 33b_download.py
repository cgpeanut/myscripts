from huggingface_hub import snapshot_download
model_id="Orenguteng/Llama-3-8B-Lexi-Uncensored-GGUF"
snapshot_download(repo_id=model_id, local_dir="/home/roxasrr/models/gguf/llama-3-8B-Lexi-Uncensored-GGUF", local_dir_use_symlinks=False, revision="main")

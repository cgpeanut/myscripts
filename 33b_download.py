from huggingface_hub import snapshot_download
model_id="TheBloke/Uncensored-Frank-33b-GGUF"
snapshot_download(repo_id=model_id, local_dir="Uncensored-Frank-33b-GGUF", local_dir_use_symlinks=False, revision="main")

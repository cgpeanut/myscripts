from huggingface_hub import snapshot_download

model_id="TheBloke/Wizard-Vicuna-30B-Uncensored-GGUF"

snapshot_download(repo_id=model_id, local_dir="TWizard-Vicuna-30B-Uncensored-GGUF", local_dir_use_symlinks=False, revision="main")

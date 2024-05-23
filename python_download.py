from huggingface_hub import snapshot_download
model_id="TheBloke/WizardCoder-Python-7B-V1.0-GGUF"
snapshot_download(repo_id=model_id, local_dir="WizardCoder-Python-7B-V1.0-GGUF", local_dir_use_symlinks=False, revision="main")

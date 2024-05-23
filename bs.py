from huggingface_hub import snapshot_download
model_id="jartine/WizardCoder-Python-34B-V1.0-llamafile"
snapshot_download(repo_id=model_id, local_dir="lexi-hf", local_dir_use_symlinks=False, revision="main")

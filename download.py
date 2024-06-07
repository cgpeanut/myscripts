from huggingface_hub import snapshot_download
model_id="mozilla-ai/prometheus-13b-v1.0.Q5_K_M.llamafile"
snapshot_download(repo_id=model_id, local_dir="prometheus-13b-v1.0.Q5_K_M.llamafile", local_dir_use_symlinks=False, revision="main")

curl https://raw.githubusercontent.com/mlc-ai/llm-perf-bench/main/model_configs/$MODEL.json \
     --create-dirs -o ./dist/models/$MODEL/config.json

python3 -m mlc_llm --build-model-only --model ./dist/models/$MODEL/ --quantization q4f16_1 --max-seq-len 4096 --num-shards 2 --target cuda --use-cuda-graph

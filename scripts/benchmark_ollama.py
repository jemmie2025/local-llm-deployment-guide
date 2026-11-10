#!/usr/bin/env python3
"""Measure local Ollama inference throughput."""

import json
import urllib.request

url = "http://127.0.0.1:11434/api/generate"

payload = {
    "model": "qwen3:0.6b",
    "prompt": "Explain local LLM inference briefly.",
    "stream": False,
    "think": False,
    "options": {
        "num_ctx": 2048,
        "num_predict": 100,
        "temperature": 0
    }
}

request = urllib.request.Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

with urllib.request.urlopen(request, timeout=120) as response:
    result = json.load(response)

tokens = result.get("eval_count", 0)
duration = result.get("eval_duration", 0)

if tokens <= 0 or duration <= 0:
    raise RuntimeError("Invalid generation metrics")

throughput = tokens / (duration / 1e9)

print(f"Model: {result['model']}")
print(f"Generated tokens: {tokens}")
print(f"Throughput: {throughput:.2f} tok/s")
print(f"Total duration: {result['total_duration']/1e9:.2f}s")
print(f"Load duration: {result['load_duration']/1e9:.2f}s")

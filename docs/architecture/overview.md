# Local LLM Deployment Architecture

## Request Flow

Client
  |
  v
Local HTTP API
  |
  v
Inference Runtime
  |
  +-- Ollama
  +-- llama.cpp
  +-- LM Studio
  +-- vLLM
  |
  v
CPU / Compatible GPU

## Deployment Profiles

### Laptop

Windows 11 → WSL2 → Ollama → CPU

Validated with Qwen3 0.6B.

### GPU Server

Linux → Inference Runtime → NVIDIA CUDA GPU

Target: 24 GB VRAM.
Deployment validation pending compatible hardware.

## Operational Requirements

- Version-controlled configuration
- Reproducible model selection
- Memory and throughput monitoring
- Network access restrictions
- Documented benchmark methodology

## Engineering Constraints

Model weights, KV cache, execution buffers,
context length, and concurrency affect capacity.

Performance must be measured on the target hardware.

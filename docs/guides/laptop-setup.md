# Laptop LLM Deployment — Ollama

## Environment

- Platform: Windows 11 / WSL2 Ubuntu 22.04
- Runtime: Ollama 0.40.15
- Model: Qwen3 0.6B
- Inference backend: llama.cpp
- Execution: 100% CPU
- Reported model allocation: 1.0 GiB

## Deployment

1. Install Ollama using its official Linux installer.
2. Verify the local API on port 11434.
3. Download the model using `ollama pull qwen3:0.6b`.
4. Validate inference using `ollama run`.
5. Confirm CPU execution using `ollama ps`.
6. Execute `python3 scripts/benchmark_ollama.py`.

## Measured Performance

| Metric | Result |
|---|---|
| Generated tokens | 100 |
| Generation throughput | 28.16 tok/s |
| Total duration | 6.69 seconds |
| Load duration | 2.89 seconds |
| Processor | CPU |

Measurements represent one successful local benchmark,
not sustained throughput or multi-request performance.

## Validation

- Ollama installed successfully.
- Local REST API accessible.
- Qwen3 0.6B model downloaded.
- CPU inference completed.
- Generation throughput measured successfully.

## Evidence

- `evidence/screenshots/01-ollama-cpu-inference.png`
- `evidence/screenshots/02-ollama-benchmark.png`

## Limitations

- No dedicated NVIDIA GPU available in WSL.
- Peak system RAM usage was not measured.
- GPU performance and concurrent serving remain untested.

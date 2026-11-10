# Local LLM Benchmark Results

## Test Environment

- OS: Windows 11 / WSL2 Ubuntu 22.04
- Runtime: Ollama 0.40.15
- Model: Qwen3 0.6B
- Execution: CPU only
- Inference backend: llama.cpp
- Context: 2048 configured for API benchmark

## Measured Results

| Metric | Result |
|---|---|
| Generated tokens | 100 |
| Generation throughput | 28.16 tok/s |
| Total execution time | 6.69 s |
| Model load duration | 2.89 s |
| Reported model allocation | 1.0 GiB |

## Methodology

Generation throughput is calculated as:

tokens/s = eval_count / (eval_duration / 1e9)

Metrics were obtained from Ollama's local API.

## Validation Status

- Model download: PASS
- Local API: PASS
- CPU inference: PASS
- Generation benchmark: PASS
- Repeated benchmark consistency: Pending
- Peak system RAM measurement: Pending
- 24 GB GPU benchmark: Not performed

## Limitations

Results represent one measured CPU inference run.
They must not be generalized across hardware,
models, quantization formats, or concurrency levels.

The reported 1.0 GiB model allocation is not a
measurement of total system RAM consumption.

## Evidence

See evidence/screenshots/ for captured terminal results.

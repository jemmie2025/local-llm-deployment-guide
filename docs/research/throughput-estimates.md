# Estimated GPU Inference Throughput

## Reference Hardware

- GPU: NVIDIA RTX 4090, 24 GB VRAM
- Assumed memory bandwidth: 1008 GB/s
- Runtime model: llama.cpp, full GPU residency
- Workload: single-stream token generation
- Usable planning allocation: 20 GiB

## Methodology

Estimated tok/s = effective bandwidth / model weight bytes.

Effective bandwidth is modeled at 40%-80% of the
GPU's nominal bandwidth. These are illustrative
utilization assumptions, not measured guarantees.

The calculation ignores compute bottlenecks, KV-cache
traffic, context effects and runtime kernel differences.
Actual performance can fall outside these estimates.

## Model and Quantization Matrix

| Model | GGUF | Weights GiB | Planning GiB | Scenario tok/s |
|---|---|---:|---:|---|
| 3B | Q4_K_M | 1.71 | 2.71 | 220-439 |
| 3B | Q5_K_M | 1.99 | 2.99 | 189-377 |
| 3B | Q6_K | 2.29 | 3.29 | 164-328 |
| 3B | Q8_0 | 2.97 | 3.97 | 126-253 |
| 7B | Q4_K_M | 3.99 | 4.99 | 94-188 |
| 7B | Q5_K_M | 4.65 | 5.81 | 81-162 |
| 7B | Q6_K | 5.35 | 6.69 | 70-140 |
| 7B | Q8_0 | 6.93 | 8.66 | 54-108 |
| 8B | Q4_K_M | 4.56 | 5.70 | 82-165 |
| 8B | Q5_K_M | 5.31 | 6.64 | 71-141 |
| 8B | Q6_K | 6.11 | 7.64 | 61-123 |
| 8B | Q8_0 | 7.92 | 9.90 | 47-95 |
| 13B | Q4_K_M | 7.41 | 9.26 | 51-101 |
| 13B | Q5_K_M | 8.63 | 10.79 | 44-87 |
| 13B | Q6_K | 9.93 | 12.42 | 38-76 |
| 13B | Q8_0 | 12.87 | 16.08 | 29-58 |
| 32B | Q4_K_M | 18.23 | 22.79 | Not recommended for full GPU residency |
| 32B | Q5_K_M | 21.25 | 26.56 | Not recommended for full GPU residency |
| 32B | Q6_K | 24.45 | 30.56 | Not recommended for full GPU residency |
| 32B | Q8_0 | 31.67 | 39.58 | Not recommended for full GPU residency |

## Published Reference Benchmark

An upstream llama.cpp CUDA benchmark reports
186.21 tok/s for Llama 2 7B Q4_0 on an RTX 4090.
It uses a different quantization from Q4_K_M.
It is not a validation of every scenario above.

Source:
https://github.com/ggml-org/llama.cpp/discussions/15013

## Locally Measured CPU Result

- Model: Qwen3 0.6B
- Runtime: Ollama 0.40.15
- Execution: CPU
- Generation: 28.16 tok/s
- Measurement: single local run

## Limitations

- Scenario ranges are analytical, not benchmark data.
- Actual quantized model sizes can differ.
- The 20 GiB budget reserves 4 GiB nominal VRAM,
  but does not guarantee KV-cache or runtime fit.
- VRAM capacity does not determine inference speed.
- Partial GPU offloading is not modeled.
- CPU throughput cannot be inferred from GPU estimates.
- Real GPU testing remains pending.

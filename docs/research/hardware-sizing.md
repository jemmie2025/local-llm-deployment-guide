# Local LLM Hardware Sizing Matrix

## Methodology

- Weight GiB = parameters × effective bits/weight / 8 / 2^30.
- Planning budget = weight GiB + max(1 GiB, 25% of weights).
- Planning budget is illustrative, NOT a validated minimum.
- Assumes model weights reside in the selected memory type.
- CPU: budget applies to system RAM for weights and allowance.
- GPU: budget applies to VRAM for full model residency.
- KV cache, runtime overhead, context and concurrency vary.
- Partial GPU offloading requires separate RAM/VRAM sizing.
- Expected tok/s: TBD until hardware-specific benchmarking.

## Sizing Table

| Model | GGUF | Weights GiB | Planning RAM/VRAM GiB | Expected tok/s |
|---|---|---:|---:|---|
| 3B | Q4_K_M | 1.71 | 2.71 | TBD — benchmark |
| 3B | Q5_K_M | 1.99 | 2.99 | TBD — benchmark |
| 3B | Q6_K | 2.29 | 3.29 | TBD — benchmark |
| 3B | Q8_0 | 2.97 | 3.97 | TBD — benchmark |
| 7B | Q4_K_M | 3.99 | 4.99 | TBD — benchmark |
| 7B | Q5_K_M | 4.65 | 5.81 | TBD — benchmark |
| 7B | Q6_K | 5.35 | 6.69 | TBD — benchmark |
| 7B | Q8_0 | 6.93 | 8.66 | TBD — benchmark |
| 8B | Q4_K_M | 4.56 | 5.70 | TBD — benchmark |
| 8B | Q5_K_M | 5.31 | 6.64 | TBD — benchmark |
| 8B | Q6_K | 6.11 | 7.64 | TBD — benchmark |
| 8B | Q8_0 | 7.92 | 9.90 | TBD — benchmark |
| 13B | Q4_K_M | 7.41 | 9.26 | TBD — benchmark |
| 13B | Q5_K_M | 8.63 | 10.79 | TBD — benchmark |
| 13B | Q6_K | 9.93 | 12.42 | TBD — benchmark |
| 13B | Q8_0 | 12.87 | 16.08 | TBD — benchmark |
| 32B | Q4_K_M | 18.23 | 22.79 | TBD — benchmark |
| 32B | Q5_K_M | 21.25 | 26.56 | TBD — benchmark |
| 32B | Q6_K | 24.45 | 30.56 | TBD — benchmark |
| 32B | Q8_0 | 31.67 | 39.58 | TBD — benchmark |

## Interpretation

- These values are model-agnostic approximations.
- Actual GGUF file sizes vary by model architecture.
- Use observed memory peaks to revise the planning budget.
- VRAM capacity alone does not predict throughput.
- Record CPU/GPU model, context, batch size and tokens/s.

## Source

https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md

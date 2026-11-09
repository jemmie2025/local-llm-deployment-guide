# GGUF Quantization and Memory Optimization

## Overview

GGUF is a model file format used by llama.cpp and
compatible inference runtimes.

Quantization reduces model weight precision to lower
storage and memory requirements, potentially affecting
inference quality and execution performance.

## Quantization Comparison

| Format | Memory | Quality | Recommended Use |
|---|---|---|---|
| Q2_K | Very low | Higher quality loss risk | Severe memory constraints |
| Q3_K_M | Low | Moderate loss risk | Memory-limited inference |
| Q4_K_M | Moderate | Balanced | General local deployment |
| Q5_K_M | Higher | Better retention | Quality-focused local inference |
| Q6_K | High | High fidelity | Larger memory budgets |
| Q8_0 | Very high | Near-original | High-fidelity comparison |

Quality rankings are general tendencies, not guarantees.

## Memory Estimation

Approximate weight storage:

Weight GB = Parameters (billions) x Effective bits / 8

Example for an 8B model:

- FP16 (16 bits): approximately 16 GB
- 8 bits: approximately 8 GB
- 6 bits: approximately 6 GB
- 4 bits: approximately 4 GB

These examples assume idealized bit widths and use
decimal GB. Actual GGUF files include quantization
metadata, scales, and potentially higher-precision tensors.

Runtime memory also includes:

- KV cache
- Compute buffers
- Model metadata
- Runtime allocations
- Context and batching overhead

Therefore, model file size is not the total RAM or
VRAM required for inference.

## Performance Considerations

- Lower precision generally reduces model weight storage.
- Smaller weights can reduce memory bandwidth requirements.
- Actual speed depends on CPU/GPU architecture and kernels.
- Quantization may reduce model output quality.
- Context length and concurrency affect runtime memory.
- GPU offloading changes RAM and VRAM distribution.

## Deployment Recommendations

### Laptop / CPU

Start with a small Q4_K_M GGUF model.

Measure memory consumption and tokens/second before
evaluating larger models or longer context windows.

### 24 GB GPU

Evaluate Q4_K_M, Q5_K_M, and Q6_K models.

Choose model size using available VRAM, KV cache
requirements, context length, and serving workload.

Use framework-supported quantization formats.
GGUF compatibility must be verified for each runtime.

## Conclusion

Q4_K_M is a practical starting point for local inference.

Q5_K_M and Q6_K provide alternatives when additional
memory is available and output quality is prioritized.

Final quantization selection requires model-specific
quality evaluation and measured inference performance.

## References

- https://huggingface.co/docs/hub/en/gguf
- https://github.com/ggml-org/llama.cpp
- https://github.com/ggml-org/llama.cpp/tree/master/tools/quantize

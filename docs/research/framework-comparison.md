# Local LLM Inference Framework Comparison

## Overview

Technical evaluation of Ollama, llama.cpp, LM Studio,
and vLLM for CPU and consumer-GPU inference.

## Framework Comparison

| Framework | Architecture | Model Support | Strength | Limitation |
|---|---|---|---|---|
| Ollama | Local inference service with CLI and REST API | GGUF-based models and supported imports | Simple deployment and model management | Less low-level control |
| llama.cpp | C/C++ inference engine using ggml | GGUF | CPU efficiency, quantization, GPU offloading | Requires manual tuning |
| LM Studio | Desktop application with local inference runtimes | GGUF and supported runtime formats | GUI, model testing, local API | Runtime-dependent compatibility |
| vLLM | High-throughput inference engine using PagedAttention and continuous batching | Hugging Face formats and supported quantizations | Concurrent API serving and efficient KV-cache management | Higher setup complexity |

## Hardware Compatibility

| Framework | CPU | Consumer GPU | 24 GB NVIDIA GPU |
|---|---|---|---|
| Ollama | Yes | Supported GPUs | Yes, subject to model fit |
| llama.cpp | Yes | CUDA/HIP and other backends | Yes, with configurable offloading |
| LM Studio | Yes | Runtime-dependent | Yes, with compatible runtime |
| vLLM | Supported CPU backends | Architecture-dependent | Yes, subject to CUDA and model compatibility |

GPU support and quantization availability depend on
software versions, hardware architecture, and runtime.

## Deployment Recommendations

### Laptop: Windows 11 / WSL2

**Recommended:** Ollama or llama.cpp.

- Use smaller GGUF-quantized models.
- Start with Q4_K_M where available.
- Monitor RAM usage and generation throughput.
- Adjust context length to control memory consumption.

LM Studio is suitable for GUI-based experimentation.

### GPU Server: 24 GB VRAM

**Recommended:** vLLM or llama.cpp.

- vLLM: Concurrent inference and API serving.
- llama.cpp: GGUF execution and GPU-layer control.
- Ollama: Simplified deployment and model management.
- LM Studio: Interactive evaluation.

Model fit depends on weights, KV cache, runtime buffers,
context length, and concurrency.

## Performance Evaluation

Benchmark using consistent model and workload settings.

Measure:

1. Peak RAM and VRAM consumption.
2. Time to first token (TTFT).
3. Generation throughput (tokens/second).
4. Context length and quantization.
5. Latency under concurrent requests.

Separate estimated hardware requirements from
actual benchmark measurements.

## Security Considerations

- Bind local APIs to localhost by default.
- Authenticate and restrict remotely accessible endpoints.
- Pin runtime versions for reproducibility.
- Review model licensing.
- Never commit secrets or model weights.

## Conclusion

- **Ollama:** Best starting point for simple local deployment.
- **llama.cpp:** Best for fine-grained GGUF inference control.
- **LM Studio:** Best for interactive desktop experimentation.
- **vLLM:** Strong candidate for high-throughput GPU serving.

Final hardware recommendations require measured
memory consumption and inference performance.

## References

See [Technical References](references.md).

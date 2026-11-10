#!/usr/bin/env python3
"""Generate illustrative RTX 4090 inference throughput scenarios."""

from pathlib import Path
from scripts.hardware_sizing import (
    BITS, MODELS, weight_gib, planning_gib
)

GPU_BANDWIDTH_GB_S = 1008
VRAM_BUDGET_GIB = 20
EFFICIENCIES = (0.40, 0.80)


def estimate_range(weights_gib):
    """Calculate bandwidth-based generation scenarios."""
    weight_bytes = weights_gib * 2**30
    return tuple(
        GPU_BANDWIDTH_GB_S * 1e9 * efficiency / weight_bytes
        for efficiency in EFFICIENCIES
    )


def generate():
    lines = [
        "# Estimated GPU Inference Throughput",
        "",
        "## Reference Hardware",
        "",
        "- GPU: NVIDIA RTX 4090, 24 GB VRAM",
        "- Assumed memory bandwidth: 1008 GB/s",
        "- Runtime model: llama.cpp, full GPU residency",
        "- Workload: single-stream token generation",
        "- Usable planning allocation: 20 GiB",
        "",
        "## Methodology",
        "",
        "Estimated tok/s = effective bandwidth / model weight bytes.",
        "",
        "Effective bandwidth is modeled at 40%-80% of the",
        "GPU's nominal bandwidth. These are illustrative",
        "utilization assumptions, not measured guarantees.",
        "",
        "The calculation ignores compute bottlenecks, KV-cache",
        "traffic, context effects and runtime kernel differences.",
        "Actual performance can fall outside these estimates.",
        "",
        "## Model and Quantization Matrix",
        "",
        "| Model | GGUF | Weights GiB | Planning GiB | Scenario tok/s |",
        "|---|---|---:|---:|---|",
    ]

    for model in MODELS:
        for quant, bits in BITS.items():
            weights = weight_gib(model, bits)
            budget = planning_gib(weights)

            if budget > VRAM_BUDGET_GIB:
                speed = "Not recommended for full GPU residency"
            else:
                low, high = estimate_range(weights)
                speed = f"{low:.0f}-{high:.0f}"

            lines.append(
                f"| {model}B | {quant} | {weights:.2f} | "
                f"{budget:.2f} | {speed} |"
            )

    lines += [
        "",
        "## Published Reference Benchmark",
        "",
        "An upstream llama.cpp CUDA benchmark reports",
        "186.21 tok/s for Llama 2 7B Q4_0 on an RTX 4090.",
        "It uses a different quantization from Q4_K_M.",
        "It is not a validation of every scenario above.",
        "",
        "Source:",
        "https://github.com/ggml-org/llama.cpp/discussions/15013",
        "",
        "## Locally Measured CPU Result",
        "",
        "- Model: Qwen3 0.6B",
        "- Runtime: Ollama 0.40.15",
        "- Execution: CPU",
        "- Generation: 28.16 tok/s",
        "- Measurement: single local run",
        "",
        "## Limitations",
        "",
        "- Scenario ranges are analytical, not benchmark data.",
        "- Actual quantized model sizes can differ.",
        "- The 20 GiB budget reserves 4 GiB nominal VRAM,",
        "  but does not guarantee KV-cache or runtime fit.",
        "- VRAM capacity does not determine inference speed.",
        "- Partial GPU offloading is not modeled.",
        "- CPU throughput cannot be inferred from GPU estimates.",
        "- Real GPU testing remains pending.",
        "",
    ]

    output = Path("docs/research/throughput-estimates.md")
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"PASS: Generated {output}")


if __name__ == "__main__":
    generate()

#!/usr/bin/env python3
"""Generate an approximate GGUF hardware sizing matrix."""

from pathlib import Path

# Effective bits/weight: llama.cpp Llama-3.1-8B reference.
BITS = {
    "Q4_K_M": 4.8944,
    "Q5_K_M": 5.7036,
    "Q6_K": 6.5633,
    "Q8_0": 8.5008,
}

MODELS = [3, 7, 8, 13, 32]


def weight_gib(parameters_b, bits):
    """Estimate model weight allocation in GiB."""
    return parameters_b * 1e9 * bits / 8 / 2**30


def planning_gib(weights):
    """Add illustrative 25% or 1 GiB runtime allowance."""
    return weights + max(1.0, weights * 0.25)


def generate():
    rows = [
        "# Local LLM Hardware Sizing Matrix",
        "",
        "## Methodology",
        "",
        "- Weight GiB = parameters × effective bits/weight / 8 / 2^30.",
        "- Planning budget = weight GiB + max(1 GiB, 25% of weights).",
        "- Planning budget is illustrative, NOT a validated minimum.",
        "- Assumes model weights reside in the selected memory type.",
        "- CPU: budget applies to system RAM for weights and allowance.",
        "- GPU: budget applies to VRAM for full model residency.",
        "- KV cache, runtime overhead, context and concurrency vary.",
        "- Partial GPU offloading requires separate RAM/VRAM sizing.",
        "- Expected tok/s: TBD until hardware-specific benchmarking.",
        "",
        "## Sizing Table",
        "",
        "| Model | GGUF | Weights GiB | Planning RAM/VRAM GiB | Expected tok/s |",
        "|---|---|---:|---:|---|",
    ]

    for model in MODELS:
        for quant, bits in BITS.items():
            weights = weight_gib(model, bits)
            budget = planning_gib(weights)
            rows.append(
                f"| {model}B | {quant} | {weights:.2f} | "
                f"{budget:.2f} | TBD — benchmark |"
            )

    rows.extend([
        "",
        "## Interpretation",
        "",
        "- These values are model-agnostic approximations.",
        "- Actual GGUF file sizes vary by model architecture.",
        "- Use observed memory peaks to revise the planning budget.",
        "- VRAM capacity alone does not predict throughput.",
        "- Record CPU/GPU model, context, batch size and tokens/s.",
        "",
        "## Source",
        "",
        "https://github.com/ggml-org/llama.cpp/blob/"
        "master/tools/quantize/README.md",
        "",
    ])

    output = Path("docs/research/hardware-sizing.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(rows), encoding="utf-8")
    print(f"PASS: Generated {output}")


if __name__ == "__main__":
    generate()

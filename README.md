# Local LLM Deployment and Hardware Sizing Guide

## Overview

A reproducible engineering study of local Large Language
Model (LLM) deployment using Ollama, llama.cpp, LM Studio,
and vLLM.

The project evaluates deployment compatibility, GGUF
quantization, memory requirements, inference performance,
and hardware selection.

## Objectives

- Compare four local LLM inference frameworks.
- Explain GGUF quantization and its trade-offs.
- Estimate RAM and VRAM requirements across model sizes.
- Evaluate inference throughput in tokens per second.
- Document laptop and 24 GB GPU deployment procedures.
- Validate sizing assumptions against practical measurements.

## Project Structure

- `docs/research/` — Framework and hardware research.
- `docs/guides/` — Deployment instructions.
- `docs/architecture/` — Technical architecture.
- `benchmarks/` — Performance methodology and results.
- `scripts/` — Reproducible utilities.
- `tests/` — Validation tests.
- `evidence/` — Supporting validation evidence.

## Engineering Standards

1. Use authoritative technical references.
2. Separate estimates from measured benchmark results.
3. Document software versions and hardware configurations.
4. Keep commands reproducible and testable.
5. Never commit secrets or downloaded model weights.
6. Record limitations and unsupported configurations.

## Project Status

Unit 1: Repository foundation in progress.

Research, implementation, and validation will be completed
incrementally with focused Git commits.

## License

For educational and technical research purposes.

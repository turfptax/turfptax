# Hi, I'm Tory — `@turfptax`

**Lead AI Engineer at [BeWell Clinical Studies](https://bewellclinicalstudies.com).** I build regulatory-compliant AI pipelines for clinical research — HIPAA, NIST 800-171, 21 CFR Part 11 — and open-source hardware on the side.

Twelve years in healthcare IT before the AI lead role: sole IT for a 45-person organization, infrastructure and compliance from the ground up, and a long arc of teaching myself my way into LLM deployment, agentic systems, and embedded ML. I think in systems and ship them.

---

## What I'm building

### Cortex — Wearable AI Memory

A Raspberry Pi Zero 2 W you wear that captures audio, runs local STT, and stores notes, sessions, and activity in a queryable knowledge graph. An ESP32-S3 USB dongle handles BLE fallback when WiFi isn't available. An MCP server lets Claude and other agents read and write the memory directly.

- [cortex-core](https://github.com/turfptax/cortex-core) — Pi firmware and SQLite backend
- [cortex-link](https://github.com/turfptax/cortex-link) — ESP32-S3 BLE bridge with OTA via ugit
- [cortex-mcp](https://github.com/turfptax/cortex-mcp) — MCP server + CLI for AI agents
- [cortex-desktop](https://github.com/turfptax/cortex-desktop) — system-tray companion app
- [cortex-plugin](https://github.com/turfptax/cortex-plugin) — Claude Code plugin
- [cortex-voice-training](https://github.com/turfptax/cortex-voice-training) — fine-tuning Whisper on Cortex recordings

### Open Muscle — Open-Source Neurotech

A 501(c)(3) building accessible prosthetic sensing. Pressure myography (PMG) and tissue deformation myography (TDMG) for finger tracking — no EMG required — using custom flex PCBs and real-time ML.

- [Open Muscle Hub](https://github.com/Open-Muscle/OpenMuscle-Hub) — central docs and build guides
- [FlexGrid](https://github.com/Open-Muscle/OpenMuscle-FlexGrid) — 60-sensor wearable pressure array
- [LASK5](https://github.com/Open-Muscle/OpenMuscle-LASK5) — handheld gesture training device
- [OpenMuscle Software](https://github.com/Open-Muscle/OpenMuscle-Software) — firmware, data tools, ML hooks
- Models on [Hugging Face](https://huggingface.co/openmuscle) · writeup at [openmuscle.org](https://openmuscle.org) · featured on [Hackaday](https://hackaday.com/2022/10/04/forearm-muscle-contraction-sensor-is-useful-component-for-open-source-prosthetics/)

*The original `turfptax/openmuscle` proof-of-concept repo is archived. Active development continues across the [Open Muscle](https://github.com/Open-Muscle) GitHub organization linked above.*

### ugit — MicroPython OTA from GitHub

A small library for over-the-air firmware updates from a GitHub repo. Widely used in the ESP32/MicroPython community.

→ [ugit](https://github.com/turfptax/ugit)

---

## Recent experiments

- [bugout-monitor](https://github.com/turfptax/bugout-monitor) — disaster-prep dashboard with OSINT threat monitoring and LLM integration
- [offline-mesh-toolkit](https://github.com/turfptax/offline-mesh-toolkit) — download-once / flash-anywhere toolkit for Meshtastic and MeshCore
- [anti-gaslight-firmware](https://github.com/turfptax/anti-gaslight-firmware) — ESP32-S3 environmental sensor (BME280 + TCS3200 + PIR → MQTT) with OTA via ugit
- [ESP32Watch](https://github.com/turfptax/ESP32Watch) — MicroPython watch firmware for the Waveshare ESP32-S3 AMOLED-2.06
- [openclaw-udp-messenger](https://github.com/turfptax/openclaw-udp-messenger) — local-network agent-to-agent messaging plugin

---

## Latest activity

<!-- ACTIVITY:START -->
_Auto-updated 2026-05-02 · top 5 most recently pushed repos_

- [`cortex-voice-training`](https://github.com/turfptax/cortex-voice-training) · `Python` — Cortex voice training pipeline — fine-tune Whisper on Cortex recordings for improved STT accuracy
- [`truthsea-sim`](https://github.com/turfptax/truthsea-sim) · `Python` — TruthSea off-chain epistemic truth-scoring simulation with DAG propagation, worldview lenses, and 3D visualiz…
- [`anti-gaslight-firmware`](https://github.com/turfptax/anti-gaslight-firmware) · `Python` — ESP32-S3 environmental sensor firmware (BME280 + TCS3200 + PIR → MQTT). OTA via ugit.
- [`cortex-desktop`](https://github.com/turfptax/cortex-desktop) · `Python` — Cortex Hub desktop app — system tray + browser UI for your AI companion Pi
- [`cortex-core`](https://github.com/turfptax/cortex-core) · `Python` — Cortex Core — Wearable AI Memory (Pi Zero 2 W)
<!-- ACTIVITY:END -->

See also: [recent metrics digest](data/metrics/latest.md).

---

## What I work with

**AI:** LLM deployment, RAG, agentic frameworks, MCP servers, regulatory-compliant pipelines for clinical and healthcare contexts
**Embedded:** ESP32-S3 / ESP32-C3, Raspberry Pi, MicroPython (asyncio), custom flex PCBs via JLCPCB, sensor fusion, ESP-NOW
**ML:** Real-time inference, signal processing, hand-gesture recognition, fine-tuning Whisper for domain-specific STT
**Tooling:** Python, JavaScript/Node, KiCad, Fusion 360, Blender

I'm an AI integrator, not a researcher — I deploy, orchestrate, and harden, rather than train models from scratch.

---

## Outside of code

Sci-fi writer, occasional YouTube creator at [TURFPTAx](https://www.youtube.com/@TURFPTAx), and a slow-burn fan of any system with a sharp learning curve. I read a lot.

---

## Collaboration

I'm open to work on AI in regulated industries, biosensing, embedded ML, and assistive technology. Beginner-friendly issues are marked across the [Open Muscle](https://github.com/Open-Muscle) repos — pull up a chair.

More at [openmuscle.org](https://openmuscle.org).

# Hi, I'm Tory, `@turfptax`

**Lead AI Engineer at [BeWell Clinical Studies](https://bewellclinicalstudies.com).** I research and build regulatory-compliant AI systems for clinical research (HIPAA, NIST 800-171, 21 CFR Part 11), and open-source hardware on the side.

Twelve years in healthcare IT before the AI lead role: sole IT for a 45-person organization, infrastructure and compliance from the ground up, and a long arc of teaching myself into LLM deployment, agentic systems, and embedded ML. I think in systems and ship them.

---

## What I'm building

### Cortex, Wearable AI Memory

A Raspberry Pi Zero 2 W you wear that captures audio, runs local STT, and stores notes, sessions, and activity in a queryable knowledge graph. An ESP32-S3 USB dongle handles BLE fallback when WiFi isn't available, an MCP server lets Claude and other agents read and write the memory directly, and it now runs in the cloud as a private, single-owner service.

- [cortex-core](https://github.com/turfptax/cortex-core) is the Pi firmware and SQLite backend
- [Cortex-Cloud](https://github.com/turfptax/Cortex-Cloud) is the one-command Azure deployment: a private web memory Hub plus MCP for any AI, locked to a single account
- [cortex-link](https://github.com/turfptax/cortex-link) is the ESP32-S3 BLE bridge with OTA via ugit
- [cortex-mcp](https://github.com/turfptax/cortex-mcp) is the MCP server and CLI for AI agents
- [cortex-desktop](https://github.com/turfptax/cortex-desktop) is the system-tray companion app
- [cortex-plugin](https://github.com/turfptax/cortex-plugin) is the Claude Code plugin
- [cortex-voice-training](https://github.com/turfptax/cortex-voice-training) fine-tunes Whisper on Cortex recordings

### Open Muscle, Open-Source Neurotech

A building accessible prosthetic sensing. Pressure myography (PMG) and tissue deformation myography (TDMG) for finger tracking, no EMG required, using custom flex PCBs and real-time ML.

- [Open Muscle Hub](https://github.com/Open-Muscle/OpenMuscle-Hub) is the central docs and build guides
- [FlexGrid](https://github.com/Open-Muscle/OpenMuscle-FlexGrid) is a 60-sensor wearable pressure array
- [LASK5](https://github.com/Open-Muscle/OpenMuscle-LASK5) is a handheld gesture training device
- [OpenMuscle Software](https://github.com/Open-Muscle/OpenMuscle-Software) is the firmware, data tools, and ML hooks
- Models on [Hugging Face](https://huggingface.co/openmuscle) · writeup at [openmuscle.org](https://openmuscle.org) · featured on [Hackaday](https://hackaday.com/2022/10/04/forearm-muscle-contraction-sensor-is-useful-component-for-open-source-prosthetics/)

*The original `turfptax/openmuscle` proof-of-concept repo is archived. Active development continues across the [Open Muscle](https://github.com/Open-Muscle) GitHub organization linked above.*

### ugit, MicroPython OTA from GitHub

A small library for over-the-air firmware updates from a GitHub repo. Widely used in the ESP32/MicroPython community.

[ugit](https://github.com/turfptax/ugit)

---

## Recent experiments

- [bugout-monitor](https://github.com/turfptax/bugout-monitor) is a disaster-prep dashboard with OSINT threat monitoring and LLM integration
- [offline-mesh-toolkit](https://github.com/turfptax/offline-mesh-toolkit) is a download-once, flash-anywhere toolkit for Meshtastic and MeshCore
- [anti-gaslight-firmware](https://github.com/turfptax/anti-gaslight-firmware) is an ESP32-S3 environmental sensor (BME280 + TCS3200 + PIR to MQTT) with OTA via ugit
- [ESP32Watch](https://github.com/turfptax/ESP32Watch) is MicroPython watch firmware for the Waveshare ESP32-S3 AMOLED-2.06
- [openclaw-udp-messenger](https://github.com/turfptax/openclaw-udp-messenger) is a local-network agent-to-agent messaging plugin

---

## Latest activity

<!-- ACTIVITY:START -->
_Auto-updated 2026-07-24 · top 5 most recently pushed repos_

- [`cortex-desktop`](https://github.com/turfptax/cortex-desktop) · `TypeScript` - Cortex Hub desktop app: system tray + browser UI for your AI companion Pi
- [`Cortex-Cloud`](https://github.com/turfptax/Cortex-Cloud) · `Python` - Your own AI memory, in the cloud you own. Deploy a private, single-owner AI memory service (web Hub + MCP for…
- [`cortex-core`](https://github.com/turfptax/cortex-core) · `Python` - Cortex Core: Pi-side memory + overseer plugin. Local-first wearable AI memory: notes, sessions, projects, tim…
- [`turfptax.github.io`](https://github.com/turfptax/turfptax.github.io) · `HTML` - (no description)
- [`cortex-plugin`](https://github.com/turfptax/cortex-plugin) · `Python` - Claude Code plugin for the Cortex wearable AI memory system
<!-- ACTIVITY:END -->

See also: [recent metrics digest](data/metrics/latest.md).

---

## What I work with

**AI:** LLM deployment, RAG, agentic frameworks, MCP servers, regulatory-compliant pipelines for clinical and healthcare contexts
**Embedded:** ESP32-S3 / ESP32-C3, Raspberry Pi, MicroPython (asyncio), custom flex PCBs via JLCPCB, sensor fusion, ESP-NOW
**ML:** Real-time inference, signal processing, hand-gesture recognition, fine-tuning Whisper for domain-specific STT
**Tooling:** Python, JavaScript/Node, KiCad, Fusion 360, Blender

I work as an applied AI researcher and integrator. I deploy, orchestrate, and harden real systems in production, and I build novel ones (wearable AI memory, open-source biosensing) to find out what these tools can actually do.

---

## Outside of code

Sci-fi writer, occasional YouTube creator at [TURFPTAx](https://www.youtube.com/@TURFPTAx), and a slow-burn fan of any system with a sharp learning curve. I read a lot.

---

## Collaboration

I'm open to work on AI in regulated industries, biosensing, embedded ML, and assistive technology. Beginner-friendly issues are marked across the [Open Muscle](https://github.com/Open-Muscle) repos, so pull up a chair.

More at [openmuscle.org](https://openmuscle.org).

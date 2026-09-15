<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:161B22,100:238636&height=220&section=header&text=LLM%20Inference%20Optimization&fontSize=38&fontColor=FFFFFF&animation=fadeIn&fontAlignY=38&desc=From%20Model%20Architecture%20to%20Production%20Inference&descAlignY=58&descSize=16" width="100%"/>

<br>

<a href="https://github.com/YOUR_USERNAME">
<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=21&duration=2800&pause=1000&color=58A6FF&center=true&vCenter=true&repeat=true&width=900&height=50&lines=LLM+Inference+Optimization+Engineer;Transformer+%7C+PyTorch+%7C+vLLM;CUDA+%7C+AscendC+%7C+Qwen3.x;KV+Cache+%7C+MTP+%7C+FlashInfer+%7C+CUDA+Graph;Model+Selection+%E2%86%92+Deployment+%E2%86%92+Profiling+%E2%86%92+Optimization" />
</a>

<br><br>

<img src="https://skillicons.dev/icons?i=python,pytorch,linux,cpp,cuda,git&perline=6" />

</div>

---

## 🧠 About Me

```text
I focus on LLM inference optimization.

Not only deploying models.
Not only tuning parameters.

I study the complete path:

Model Architecture
        ↓
Inference Framework
        ↓
Hardware Architecture
        ↓
Kernel / Operator
        ↓
Memory & KV Cache
        ↓
Scheduling & Batching
        ↓
Performance Profiling
        ↓
Production Serving
```

结合**模型结构、业务场景与硬件参数**，选择合适的开源大模型与推理框架，
完成从 **本地部署 → 性能分析 → 推理优化 → 生产级部署** 的完整工程链路。

---

## ⚡ Core Technology

<table>
<tr>
<td width="50%" valign="top">

### 🧩 Model & Framework

* Transformer
* PyTorch
* Hugging Face Transformers
* vLLM
* Qwen3 / Qwen3.x
* MoE
* Long Context

</td>

<td width="50%" valign="top">

### 🚀 Inference Optimization

* KV Cache
* PagedAttention
* Prefix Caching
* Continuous Batching
* MTP / Speculative Decoding
* Quantization
* CUDA Graph
* FlashInfer

</td>
</tr>

<tr>
<td width="50%" valign="top">

### 🖥️ GPU Stack

* NVIDIA GPU
* CUDA
* CUDA Kernel
* Triton
* FlashAttention / FlashInfer
* Nsight Systems
* Nsight Compute

</td>

<td width="50%" valign="top">

### 🧠 NPU Stack

* Ascend NPU
* CANN
* AscendC
* vLLM-Ascend
* Operator Optimization
* Hardware-aware Optimization

</td>
</tr>
</table>

---

## 🔬 My Optimization Methodology

```text
             ┌──────────────────────┐
             │    Business Scenario │
             └──────────┬───────────┘
                        ↓
             ┌──────────────────────┐
             │    Model Selection   │
             │   Qwen / MoE / etc.  │
             └──────────┬───────────┘
                        ↓
             ┌──────────────────────┐
             │  Hardware Analysis   │
             │ GPU / NPU / Memory   │
             └──────────┬───────────┘
                        ↓
             ┌──────────────────────┐
             │  Inference Framework │
             │      vLLM / ...      │
             └──────────┬───────────┘
                        ↓
             ┌──────────────────────┐
             │ Performance Profiling│
             │ TTFT / TPOT / TPS    │
             └──────────┬───────────┘
                        ↓
       ┌────────────────┼────────────────┐
       ↓                ↓                ↓
   KV Cache          Kernel           Scheduling
   Memory            Compute          Batching
       ↓                ↓                ↓
       └────────────────┼────────────────┘
                        ↓
             ┌──────────────────────┐
             │ Production Serving   │
             └──────────────────────┘
```

---

## 🔥 Current Focus

### Qwen3.x × vLLM × GPU / NPU

```text
Model
├── Qwen3
├── Qwen3.x
├── Dense / MoE
└── Long Context

Inference
├── vLLM
├── PagedAttention
├── Prefix Caching
├── Continuous Batching
├── MTP
└── CUDA Graph

Memory
├── KV Cache
├── FP8 KV Cache
├── Quantization
└── Memory Scheduling

Compute
├── CUDA
├── FlashInfer
├── Triton
├── CUDA Kernel
└── AscendC

Profiling
├── TTFT
├── TPOT
├── Throughput
├── GPU Utilization
└── Memory Bandwidth
```

---

## 📊 Inference Optimization Metrics

| Metric                | What I Care About          |
| --------------------- | -------------------------- |
| **TTFT**              | Time To First Token        |
| **TPOT**              | Time Per Output Token      |
| **TPS**               | Tokens Per Second          |
| **Throughput**        | tokens/s / requests/s      |
| **GPU Utilization**   | Compute utilization        |
| **Memory Usage**      | Model + KV Cache           |
| **KV Cache Capacity** | Context × Concurrency      |
| **Latency**           | P50 / P95 / P99            |
| **Concurrency**       | Sustained serving capacity |

> 优化不是单纯追求 TPS，而是在 **Latency / Throughput / Memory / Concurrency / Cost** 之间寻找最优点。

---

## 🛠️ Engineering Stack

<div align="center">

| Layer           | Technology                                  |
| --------------- | ------------------------------------------- |
| **Model**       | Qwen3.x · Transformer · MoE                 |
| **Framework**   | PyTorch · Transformers · vLLM               |
| **GPU**         | NVIDIA CUDA                                 |
| **NPU**         | AscendC · CANN                              |
| **Kernel**      | CUDA Kernel · Triton                        |
| **Attention**   | FlashAttention · FlashInfer                 |
| **Memory**      | KV Cache · PagedAttention · Prefix Cache    |
| **Decode**      | MTP · Speculative Decoding                  |
| **Serving**     | Continuous Batching · OpenAI-compatible API |
| **Profiling**   | Nsight Systems · Nsight Compute             |
| **Environment** | Linux · Python · uv · Git                   |

</div>

---

## 🚀 Featured Project

### ⚡ Qwen3.x End-to-End Inference Optimization

```text
Hardware
└── NVIDIA RTX 4090

Model
└── Qwen3.x

Framework
└── vLLM

Optimization Pipeline

        Model
          │
          ▼
   Quantization
          │
          ▼
    KV Cache
          │
          ├── FP8 KV Cache
          └── Memory Management
          │
          ▼
    Attention / Linear Attention
          │
          ├── FlashInfer
          └── GDN
          │
          ▼
      Decode
          │
          └── MTP
          │
          ▼
    Scheduling
          │
          ├── Continuous Batching
          ├── Paged KV Cache
          └── CUDA Graph
          │
          ▼
      Serving
```

### 🎯 Optimization Targets

```text
                 ┌───────────────┐
                 │   Latency ↓   │
                 └───────┬───────┘
                         │
       ┌─────────────────┼─────────────────┐
       ↓                 ↓                 ↓
  TTFT ↓             TPOT ↓          P99 Latency ↓
       │                 │                 │
       └─────────────────┼─────────────────┘
                         ↓
                 ┌───────────────┐
                 │ Throughput ↑  │
                 └───────┬───────┘
                         │
                 ┌───────▼───────┐
                 │   Cost ↓      │
                 └───────────────┘
```

---

## 📈 Benchmark Philosophy

我更关注**优化前后可量化的性能变化**：

```text
Baseline
   │
   ├── TTFT
   ├── TPOT
   ├── Throughput
   ├── GPU Memory
   └── KV Cache Capacity
   │
   ▼
Optimization
   │
   ├── Kernel
   ├── Memory
   ├── Scheduling
   └── Decode
   │
   ▼
Benchmark
   │
   ├── Short Context
   ├── Long Context
   ├── Low Concurrency
   └── High Concurrency
   │
   ▼
Production Workload
```

---

## 🧪 Research Direction

```text
                 LLM Inference
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
       Compute       Memory      Scheduling
          │            │            │
       CUDA          KV Cache    Batching
       Kernel        Quant       Prefix Cache
       FlashInfer    FP8         Request Queue
       Triton        Paged       CUDA Graph
          │            │            │
          └────────────┼────────────┘
                       ↓
              End-to-End Optimization
```

---

## 📚 What I Build

```text
✓ Large Model Deployment
✓ LLM Second Development
✓ Inference Performance Optimization
✓ Hardware-aware Model Selection
✓ vLLM Serving
✓ CUDA / NPU Optimization
✓ KV Cache Optimization
✓ Kernel / Operator Optimization
✓ Performance Benchmarking
✓ Production-grade LLM Serving
```

---

## 📊 GitHub Stats

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&hide_border=true&theme=github_dark&include_all_commits=true" height="180"/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&hide_border=true&theme=github_dark&langs_count=8" height="180"/>

</div>

---

## 🐍 Contribution Activity

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_USERNAME/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_USERNAME/output/github-contribution-grid-snake.svg">
  <img alt="github contribution snake" src="https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_USERNAME/output/github-contribution-grid-snake-dark.svg">
</picture>

</div>

---

## 🌐 Philosophy

<div align="center">

### **Don't just run the model.**

### **Understand why it is slow.**

### **Understand where the memory goes.**

### **Understand how the hardware executes it.**

### **Then optimize it.**

<br>

**Model → Framework → Hardware → Kernel → Runtime → Production**

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:238636,50:161B22,100:0D1117&height=120&section=footer" width="100%"/>

</div>

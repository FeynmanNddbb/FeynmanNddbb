"""Generate the animated SVG used by the profile README."""

from html import escape
from pathlib import Path


LANGUAGES = (
  (
    "中文",
    "我是 Feynman，27届应届硕士生，梦想成为优秀的大模型推理工程师",
    "大模型推理优化",
    "Transformer | PyTorch | vLLM",
  ),
  (
    "English",
    "I am Feynman, an aspiring LLM inference engineer",
    "LLM Inference Optimization",
    "Transformer | PyTorch | vLLM",
  ),
  (
    "日本語",
    "Feynmanです。優れたLLM推論エンジニアを目指しています",
    "LLM推論の最適化",
    "Transformer | PyTorch | vLLM",
  ),
)
LINE_INTERVAL = 1.5
LINES_PER_LANGUAGE = 3
LANGUAGE_GAP = 4
LANGUAGE_INTERVAL = LINE_INTERVAL * LINES_PER_LANGUAGE + LANGUAGE_GAP
DURATION = LANGUAGE_INTERVAL * len(LANGUAGES)


def build_svg() -> str:
    clips = []
    animated_lines = []

    for language_index, (language, *messages) in enumerate(LANGUAGES):
        language_begin = language_index * LANGUAGE_INTERVAL
        animated_lines.append(
            f'''    <g opacity="0">
      <text class="language-label" x="78" y="52">{language}</text>
      <animate attributeName="opacity" dur="{DURATION}s" begin="{language_begin}s" repeatCount="indefinite"
        values="0;1;1;0;0" keyTimes="0;.12;.68;.82;1" />
    </g>'''
        )
        for line_index, message in enumerate(messages):
            begin = language_begin + line_index * LINE_INTERVAL
            clips.append(
                f'''    <clipPath id="typing-clip-{language_index}-{line_index}">
      <rect x="24" y="{40 + line_index * 42}" width="0" height="38">
        <animate attributeName="width" dur="{DURATION}s" begin="{begin}s" repeatCount="indefinite"
          values="0;952;952;0;0" keyTimes="0;.12;.68;.82;1" />
      </rect>
    </clipPath>'''
            )
            animated_lines.append(
                f'''    <g clip-path="url(#typing-clip-{language_index}-{line_index})" opacity="0">
      <text class="message" x="500" y="{68 + line_index * 42}" text-anchor="middle">{escape(message)}</text>
      <animate attributeName="opacity" dur="{DURATION}s" begin="{begin}s" repeatCount="indefinite"
        values="0;1;1;0;0" keyTimes="0;.12;.68;.82;1" />
    </g>'''
            )

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="190" viewBox="0 0 1000 190" role="img" aria-labelledby="title desc">
  <title id="title">Feynman - LLM Inference Engineer</title>
  <desc id="desc">Animated introduction for Feynman's GitHub profile.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#07111f" />
      <stop offset="0.55" stop-color="#0b1626" />
      <stop offset="1" stop-color="#071b22" />
    </linearGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="#54d6c7" stroke-opacity="0.07" />
    </pattern>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
    </filter>
  </defs>
  <rect width="1000" height="190" rx="14" fill="url(#bg)" />
  <rect x="1" y="1" width="998" height="188" rx="13" fill="url(#grid)" stroke="#54d6c7" stroke-opacity="0.35" />
  <path d="M24 32 H976" stroke="#54d6c7" stroke-opacity="0.28" />
  <circle cx="28" cy="18" r="4" fill="#ff6b6b" />
  <circle cx="43" cy="18" r="4" fill="#ffd166" />
  <circle cx="58" cy="18" r="4" fill="#54d6c7" />
  <style>
    text {{ font-family: 'JetBrains Mono', 'Noto Sans SC', monospace; }}
    .label {{ fill: #75e6da; font-size: 11px; font-weight: 700; letter-spacing: 2px; }}
    .message {{ fill: #f3f8ff; font-size: 25px; font-weight: 600; }}
    .language-label {{ fill: #54d6c7; font-size: 12px; font-weight: 700; letter-spacing: 1px; }}
  </style>
  <text class="label" x="78" y="22">INFERENCE ENGINEERING / LIVE PROFILE</text>
  <text class="label" x="970" y="22" text-anchor="end">FEYNMAN_01</text>
  <path d="M76 166 H160 L172 154 H252" fill="none" stroke="#54d6c7" stroke-opacity="0.45" />
  <circle cx="252" cy="154" r="3" fill="#54d6c7" filter="url(#glow)" />
  <g>
{chr(10).join(clips)}
  </g>
  <g>
{chr(10).join(animated_lines)}
  </g>
  <text class="label" x="970" y="176" text-anchor="end">MODEL / FRAMEWORK / HARDWARE / OPTIMIZATION</text>
</svg>
'''


if __name__ == "__main__":
    output = Path(__file__).resolve().parents[1] / "assets" / "typing.svg"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_svg(), encoding="utf-8")
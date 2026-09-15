"""Generate the animated SVG used by the profile README."""

from html import escape
from pathlib import Path


MESSAGES = (
  "我是 Feynman",
  "Focused on LLM Inference Optimization Research",
    "Transformer | PyTorch | vLLM",
)
LINE_INTERVAL = 1.5
DURATION = 8
TYPE_DURATION = 0.65
FADE_START = 6.8
FADE_END = 7.6


def build_svg() -> str:
    clips = []
    animated_lines = []

    for index, message in enumerate(MESSAGES):
        start = index * LINE_INTERVAL
        type_end = start + TYPE_DURATION
        key_times = (
            f"0;{start / DURATION:.4f};{type_end / DURATION:.4f};"
            f"{FADE_START / DURATION:.4f};{FADE_END / DURATION:.4f};1"
        )
        clips.append(
            f'''    <clipPath id="typing-clip-{index}">
      <rect x="500" y="{40 + index * 42}" width="0" height="38">
        <animate attributeName="x" dur="{DURATION}s" repeatCount="indefinite"
          values="500;500;32;32;500;500" keyTimes="{key_times}" />
        <animate attributeName="width" dur="{DURATION}s" repeatCount="indefinite"
          values="0;0;936;936;0;0" keyTimes="{key_times}" />
      </rect>
    </clipPath>'''
        )
        animated_lines.append(
            f'''    <g clip-path="url(#typing-clip-{index})" opacity="0">
      <text class="message" x="500" y="{68 + index * 42}" text-anchor="middle">{escape(message)}</text>
      <animate attributeName="opacity" dur="{DURATION}s" repeatCount="indefinite"
        values="0;0;1;1;0;0" keyTimes="{key_times}" />
    </g>'''
        )

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="190" viewBox="0 0 1000 190" role="img" aria-labelledby="title desc">
  <title id="title">Feynman - LLM Inference Engineer</title>
  <desc id="desc">Animated introduction for Feynman's GitHub profile.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fbfdff" />
      <stop offset="1" stop-color="#f1f6fb" />
    </linearGradient>
  </defs>
  <rect width="1000" height="190" rx="16" fill="url(#bg)" />
  <rect x="1" y="1" width="998" height="188" rx="15" fill="none" stroke="#d8e1eb" />
  <path d="M32 32 H968" stroke="#e5ebf2" />
  <style>
    text {{ font-family: 'JetBrains Mono', 'Noto Sans SC', monospace; }}
    .label {{ fill: #7b8794; font-size: 11px; font-weight: 700; letter-spacing: 2px; }}
    .message {{ fill: #17212b; font-size: 25px; font-weight: 600; }}
  </style>
  <circle cx="40" cy="18" r="4" fill="#147efb" />
  <text class="label" x="54" y="22">LLM INFERENCE / PROFILE</text>
  <text class="label" x="960" y="22" text-anchor="end">FEYNMAN</text>
  <g>
{chr(10).join(clips)}
  </g>
  <g>
{chr(10).join(animated_lines)}
  </g>
  <text class="label" x="960" y="176" text-anchor="end">MODEL → FRAMEWORK → HARDWARE → OPTIMIZATION</text>
</svg>
'''


if __name__ == "__main__":
    output = Path(__file__).resolve().parents[1] / "assets" / "typing.svg"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_svg(), encoding="utf-8")
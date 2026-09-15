"""Generate the animated SVG used by the profile README."""

from html import escape
from pathlib import Path


MESSAGES = (
    "我是 Feynman —— 梦想成为优秀的大模型推理工程师",
    "LLM Inference Optimization",
    "Transformer | PyTorch | vLLM ",
    "Model → Framework → Hardware → Optimization",
)
LINE_INTERVAL = 2.5
DURATION = 10


def build_svg() -> str:
    lines = []
    for index, message in enumerate(MESSAGES):
        begin = index * LINE_INTERVAL
        lines.append(
            f'''    <g clip-path="url(#typing-clip-{index})" opacity="0">
      <text x="500" y="{42 + index * 38}" text-anchor="middle">{escape(message)}</text>
      <animate attributeName="opacity" dur="{DURATION}s" begin="{begin}s" repeatCount="indefinite"
        values="0;1;1;0;0" keyTimes="0;.12;.68;.82;1" />
    </g>'''
        )

    clips = []
    for index in range(len(MESSAGES)):
        begin = index * LINE_INTERVAL
        clips.append(
            f'''    <clipPath id="typing-clip-{index}">
      <rect x="20" y="{14 + index * 38}" width="0" height="34">
      <animate attributeName="width" dur="{DURATION}s" begin="{begin}s" repeatCount="indefinite"
          values="0;960;960;0;0" keyTimes="0;.12;.68;.82;1" />
      </rect>
    </clipPath>'''
        )

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="180" viewBox="0 0 1000 180" role="img" aria-labelledby="title desc">
  <title id="title">Feynman - LLM Inference Engineer</title>
  <desc id="desc">Animated introduction for Feynman's GitHub profile.</desc>
  <rect width="1000" height="180" rx="12" fill="#0d1117" />
  <style>
    text {{ fill: #f0f6fc; font-family: 'JetBrains Mono', 'Noto Sans SC', monospace; font-size: 25px; font-weight: 600; }}
  </style>
  <g>
{chr(10).join(clips)}
  </g>
  <g>
{chr(10).join(lines)}
  </g>
</svg>
'''


if __name__ == "__main__":
    output = Path(__file__).resolve().parents[1] / "assets" / "typing.svg"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_svg(), encoding="utf-8")
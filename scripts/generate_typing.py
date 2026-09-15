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
PARTICLES = (
  (86, 58, 1.5, 0.0),
  (144, 148, 1.0, 1.2),
  (218, 74, 1.2, 0.6),
  (306, 160, 1.4, 1.8),
  (392, 52, 0.9, 2.4),
  (468, 168, 1.1, 0.3),
  (566, 58, 1.3, 1.5),
  (642, 148, 0.9, 2.1),
  (732, 72, 1.5, 0.9),
  (814, 158, 1.1, 1.7),
  (902, 62, 0.8, 0.4),
)


def build_svg() -> str:
    clips = []
    animated_lines = []
    particles = []

    for x, y, radius, delay in PARTICLES:
        particles.append(
            f'''  <circle class="particle" cx="{x}" cy="{y}" r="{radius}" style="animation-delay: {delay}s" />'''
        )

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
      <stop offset="0" stop-color="#07111f" />
      <stop offset="0.6" stop-color="#0b1626" />
      <stop offset="1" stop-color="#071b22" />
    </linearGradient>
  </defs>
  <rect width="1000" height="190" rx="16" fill="url(#bg)" />
  <rect x="1" y="1" width="998" height="188" rx="15" fill="none" stroke="#2b5878" />
  <path d="M32 32 H968" stroke="#1d3c58" />
{chr(10).join(particles)}
  <style>
    text {{ font-family: 'JetBrains Mono', 'Noto Sans SC', monospace; }}
    .label {{ fill: #80a6c4; font-size: 11px; font-weight: 700; letter-spacing: 2px; }}
    .message {{ fill: #f2f7fb; font-size: 25px; font-weight: 600; }}
    .particle {{ fill: #6fe7ff; opacity: 0.22; animation: pulse 3.6s ease-in-out infinite; }}
    @keyframes pulse {{ 0%, 100% {{ opacity: 0.12; }} 50% {{ opacity: 0.7; }} }}
  </style>
  <circle cx="40" cy="18" r="4" fill="#49c6ff" />
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
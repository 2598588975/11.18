# Image reverse-prompting and references

Use this file when an image is supplied, when the user asks for reverse prompting, or when deciding which reference mechanism fits the goal.

## Choose the mechanism

| Goal | V8.2 method |
| --- | --- |
| Discover MJ-associated vocabulary | Describe |
| Influence content, composition, and colors | Image Prompt, optionally tune `--iw` |
| Transfer colors, medium, texture, and lighting | Style Reference with `--sref` and optional `--sw` |
| Precisely alter or combine supplied images | Edit Model |
| Reproduce only from text | Visual analysis plus compact prompt; disclose the fidelity limit |

## Describe

Describe returns four creative prompt suggestions and may return different suggestions on repeated runs. Use it to mine vocabulary, not as ground-truth reconstruction.

For a serious reverse-prompt task:

1. Run Describe more than once when available.
2. Keep descriptors that recur across outputs and agree with visible evidence.
3. Remove artist names, styles, or details that are inconsistent with the image.
4. Combine the stable vocabulary with direct analysis of composition, lighting, palette, material, and medium.
5. Write a new short prompt rather than pasting all Describe outputs together.

Official source: https://docs.midjourney.com/hc/en-us/articles/32497889043981-Describe

## Image Prompt

Use when content, layout, or color placement matters. The image guides rather than copies. Describe the complete desired final image in text; do not write instructions about changing the reference. Crop the reference to the target aspect ratio when possible. `--iw` ranges from 0 to 3.

Official source: https://docs.midjourney.com/hc/en-us/articles/32040250122381-Image-Prompts

## Style Reference

Use when the look matters more than the objects. Keep the text prompt simple and focused on content so it does not fight the style reference. `--sw` ranges from 0 to 1000, default 100. A Style Reference transfers aesthetic qualities; it does not guarantee matching geometry or subject identity.

Official source: https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference

## Prompt-only reproduction

When the user prohibits references, preserve that constraint. Analyze internally with a detailed schema, then compress the final prompt to:

```text
[medium], [subject and environment], [two or three composition anchors], [lighting], [palette and material] --ar W:H --raw --s 20-50 --chaos 0
```

Do not promise precise copying. Evaluate outputs against medium, composition, lighting, palette, material, and spatial structure; fix the largest mismatch first.


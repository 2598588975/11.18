---
name: midjourney-prompting
description: Write, reverse-engineer, improve, and debug Midjourney image prompts using current V8.2 syntax and workflows. Use whenever the user mentions Midjourney, MJ, image-to-prompt, Describe, Image Prompt, Style Reference, Edit Model, or asks why an MJ prompt is not matching a reference. Treat V7 and older behavior as legacy unless explicitly requested.
---

# Midjourney Prompting — V8.2 First

Default to Midjourney V8.2. Do not force V7 or reuse legacy parameters unless the user explicitly requests an older model. When the user asks for current or latest behavior, or when a parameter unexpectedly fails, verify against the official Midjourney documentation before answering.

## Route the request

- For parameter syntax or compatibility, read [references/parameters.md](references/parameters.md).
- For image reverse-prompting, Describe, Image Prompts, or Style References, read [references/image-references.md](references/image-references.md).
- For precise modification, compositing, inpainting, outpainting, or reference-driven generation, read [references/editing.md](references/editing.md).

## Prompt anatomy

Use this order:

```text
[image references if allowed] [subject and medium], [environment], [composition], [lighting], [color and material] [parameters]
```

- Put every parameter at the end. Do not write text after parameters.
- Describe the finished image, not instructions such as “show me” or “make this look like.”
- Prefer a short, concrete visual description over long prose or keyword piles.
- Front-load the subject and the intended medium. Use one coherent medium/render anchor; do not mix several engines or incompatible aesthetics.
- Include only dimensions that matter: subject, medium, environment, composition, lighting, palette, material, mood.
- Use positive visual language. Put genuine exclusions in `--no`.

## V8.2 defaults

- Use `--raw` when literal adherence, realism, or reference matching matters.
- Start precise reconstruction work around `--s 20–50`; increase only when the user wants more interpretation.
- Use `--chaos 0` for controlled comparison. Introduce variety deliberately.
- Use `--hd` for native 2048px output when needed; do not use `--q`.
- Do not use `::` prompt weights, `--q`, `--cref`, or V7-only `--oref` in a V8.2 prompt.
- V8.2 uses the Edit Model for identity/object references and precise reference-driven generation. `--oref` belongs to V7 and may switch the job away from V8.2.
- Personalization can materially change style. For neutral reproduction tests, ask the user to disable it or explicitly document that it is active.

## Reverse an image into an MJ prompt

Analyze deeply, but submit compactly.

1. Separate content from invariant style: subject/environment versus composition, medium, lighting, palette, material, and atmosphere.
2. Identify two or three defining visual anchors and the most likely MJ misinterpretation.
3. Decide whether the target looks like photography, illustration, offline CGI, real-time game rendering, or another medium. This decision must appear near the start of the final prompt.
4. Compress the result into a paste-ready V8.2 prompt. Do not send the full analysis schema to MJ.
5. If generation output is available, compare subject, composition, lighting, color, material, spatial structure, and medium. Change one dominant cause per iteration.

For prompt-only reproduction, state the real limitation: text can approximate the visual system but cannot reliably reproduce exact object placement or geometry. Describe is useful for vocabulary discovery, not precise copying.

## Output format

Return the finished prompt alone in a code block exactly as it should be pasted into Midjourney. Then briefly explain only non-obvious choices or incompatible parameters removed. When alternatives materially help, provide no more than three clearly differentiated variants.

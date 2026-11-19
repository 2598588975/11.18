# Midjourney V8.2 Edit Model

Use this file for precise changes, identity/object references, compositing, inpainting, outpainting, or continuing an uploaded image in V8.2.

The V8.2 Edit Model replaces the normal V8 workflow roles previously handled by Omni Reference, Character Reference, and Retexture. It can edit an existing image or generate with up to four attached reference images.

## Prompting

- The Edit Model accepts direct instructions as well as ordinary scene descriptions.
- State what should change and what must remain invariant.
- Use `--raw` when tighter instruction following matters.
- For targeted edits, select only the intended region; repeated broad regeneration can cause unnecessary drift.
- For a cohesive re-style, describe the desired medium in the prompt and optionally add a Style Reference.
- The first attached image guides the initial aspect ratio unless `--ar` is specified.

## Decision rule

- Use Image Prompt when inspiration from composition/content is enough.
- Use Style Reference when only aesthetic transfer is needed.
- Use Edit Model when exact source preservation, targeted change, compositing, or multiple identity/object references matter.
- Respect a user's instruction not to provide references; do not silently switch to Edit Model or attach their image.

Official sources:

- Edit Model: https://docs.midjourney.com/hc/en-us/articles/48495453462797-Edit-Model
- Editor: https://docs.midjourney.com/hc/en-us/articles/32764383466893-Editor


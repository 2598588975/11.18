# Midjourney V8.2 parameters

Use this file when writing or debugging parameters. Official source: https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version

## Supported core parameters

- `--ar W:H`: aspect ratio using integers. V8.2 supports ratios up to 14:1; HD is limited to 4:1.
- `--raw`: reduces Midjourney's automatic aesthetic layer and improves literal prompt influence.
- `--stylize N` / `--s N`: 0–1000, default 100. Lower values are more literal.
- `--chaos N` / `--c N`: 0–100, default 0. Higher values increase variation.
- `--weird N` / `--w N`: experimental aesthetics; avoid for reference matching unless requested.
- `--seed N`: controls starting noise and helps A/B tests. It is not a durable style or character lock.
- `--no x, y`: exclusions. Prefer positive description for the desired image and reserve this for actual unwanted elements.
- `--sd` / `--hd`: standard or native 2048px generation in V8.1/V8.2. HD has a maximum 4:1 aspect ratio.
- `--iw 0–3`: Image Prompt influence.
- `--sref URL-or-code` with `--sw 0–1000`: Style Reference and its strength.
- `--p`: Personalization or a selected profile/moodboard. Disable it for neutral reproduction tests unless the user wants their taste profile applied.
- `--exp`: experimental aesthetics; it can compete with prompt adherence and reference influence.

## Do not use for V8.2

- `--quality` / `--q`: unsupported in V8.x. Use `--sd` or `--hd` for resolution.
- `::` multi-prompts and weights: supported only through V6.1.
- `--cref` / `--cw`: legacy V6 character reference.
- `--oref` / `--ow`: V7 Omni Reference; use the V8.2 Edit Model instead when remaining on V8.2 matters.
- `--niji`: separate model family, not a V8.2 modifier.
- `--turbo`: unavailable in V8.x.

## Syntax checks

- Parameters go after all prompt text.
- Do not place commas, periods, or explanatory text after the parameter block.
- Do not include a version parameter unless pinning a non-default version is intentional.
- Prefer the official current spelling `--raw`.

Official references:

- Version compatibility: https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version
- Raw: https://docs.midjourney.com/hc/en-us/articles/32634113811853-Raw
- Stylize: https://docs.midjourney.com/hc/en-us/articles/32196176868109-Stylize
- Parameter list: https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List


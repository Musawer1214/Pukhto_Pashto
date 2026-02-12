# Pashto Normalization Policy v0.1

This starter policy defines simple, low-risk rules for text cleanup before
training ASR/TTS/NLP baselines.

## Scope
- Applies to sentence-level text in this repository.
- Prioritizes consistency over linguistic completeness.
- Keeps semantic meaning unchanged.

## Rules
1. Trim leading and trailing whitespace.
2. Collapse repeated internal spaces to a single space.
3. Remove zero-width/invisible spacing characters.
4. Remove elongation characters such as tatweel (`ـ`).
5. Use Arabic punctuation consistently in Pashto text:
   - comma: `،`
   - question mark: `؟`
   - semicolon: `؛`
6. Keep sentence-final punctuation as a single character (avoid `!!`, `؟؟`).
7. Normalize quotation usage to one style per sentence (avoid mixed quote styles).
8. Normalize digit style to one standard per dataset split.
9. Preserve original word order and meaning; do not rewrite content.
10. Keep dialect wording as spoken; normalize form, not dialect identity.

## Non-goals (for v0.1)
- No stemming or morphology rules.
- No automatic transliteration.
- No named-entity rewriting.

## File Reference
- Seed examples: `data/processed/normalization_seed_v0.1.tsv`
- Validator: `scripts/validate_normalization.py`

#!/usr/bin/env bash
# Copia docs/actualizacion-normativa-2025-2026.md a references/ de cada skill.
set -euo pipefail
cd "$(dirname "$0")/.."
for d in .claude/skills/*/; do
  mkdir -p "$d/references"
  cp docs/actualizacion-normativa-2025-2026.md "$d/references/"
done
echo "Sincronizado en $(ls -d .claude/skills/*/ | wc -l) skills."

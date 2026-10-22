# skills-laws

Skills profesionales para **Claude Code / Claude** orientadas a los participantes de un
**juicio fiscal en México**: el juicio contencioso administrativo federal ante el
Tribunal Federal de Justicia Administrativa (TFJA), con sus etapas previas (auditoría,
revocación, PRODECON) y posteriores (amparo directo, revisión fiscal).

> ⚠️ Estas skills son herramientas de apoyo para profesionales. No sustituyen la revisión
> de un abogado con cédula. Las leyes y la jurisprudencia cambian: cada skill obliga a
> verificar la vigencia de los artículos y plazos y a marcar `[VERIFICAR]` en lugar de
> inventar tesis.

## Skills por puesto (13)

| Ámbito | Puesto | Skill |
|---|---|---|
| Abogados | Abogado del contribuyente (actor) | `abogado-actor-demanda-nulidad` |
| Abogados | Litigante de amparo y de segunda instancia | `litigante-amparo-revision-fiscal` |
| Abogados | Asesor de PRODECON | `asesor-prodecon` |
| Hacienda | Abogado de la autoridad (AGJ/ADJ del SAT, IMSS, INFONAVIT, estados) | `abogado-autoridad-demandada` |
| Hacienda | Auditor, visitador o ejecutor del SAT (AGAFF, AGGC, AGH, AGR) | `funcionario-sat-fiscalizacion` |
| Hacienda | Procuraduría Fiscal de la Federación (amparos contra leyes, delitos fiscales) | `procuraduria-fiscal-federacion` |
| Juzgados | Magistrado instructor o secretario del TFJA | `magistrado-proyecto-sentencia` |
| Juzgados | Juez de Distrito, Tribunal Colegiado o SCJN (amparo fiscal) | `juzgador-amparo-fiscal` |
| Especialistas | Contador fiscal / contralor | `contador-fiscal-defensa` |
| Especialistas | Perito contable | `perito-contable-fiscal` |
| Especialistas | Precios de transferencia, comercio exterior y aduanas, seguridad social | `especialista-tecnico-fiscal` |
| Especialistas | Coordinador del expediente / pasante | `control-plazos-expediente` |
| Academia | Docente e investigador universitario | `docente-investigador-derecho-fiscal` |

## Documentación

- [`docs/actualizacion-normativa-2025-2026.md`](docs/actualizacion-normativa-2025-2026.md): reforma a la LFPCA (9 de junio de 2026), reforma a la Ley de Amparo, el CFF y la LOTFJA (16 de octubre de 2025), CFF 2026 (garantías), reforma judicial, TFJA, UMA 2026 y estructura de la SHCP y el SAT, con su nivel de certeza (✅ / ⚠️) y fuentes.
- [`docs/mapa-de-actores.md`](docs/mapa-de-actores.md): quién es quién (Hacienda, juzgados, abogados, especialistas y academia) y qué skill corresponde a cada puesto.

Cada skill trae su propia copia del documento de actualización en `references/`. Para actualizarlo, edita el archivo en `docs/` y ejecuta `scripts/sync-actualizacion.sh`.

## Uso

**Claude Code:** clona este repo y abre Claude dentro de él; las skills en
`.claude/skills/` se cargan solas. Para tenerlas en todos tus proyectos, cópialas a
`~/.claude/skills/`.

**Claude.ai:** comprime la carpeta de cada skill (`zip -r nombre.zip nombre/`) y súbela
en *Settings → Capabilities → Skills*.

### Calculadora de plazos

```bash
python3 .claude/skills/control-plazos-expediente/scripts/plazos.py 2026-10-01 30 \
  --vacaciones 2026-12-16:2026-12-31
```

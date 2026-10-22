# skills-laws

Skills profesionales para **Claude Code / Claude** orientadas a los participantes de un
**juicio fiscal en México**: el juicio contencioso administrativo federal ante el
Tribunal Federal de Justicia Administrativa (TFJA), con sus etapas previas (auditoría,
revocación, PRODECON) y posteriores (amparo directo, revisión fiscal).

> ⚠️ Estas skills son herramientas de apoyo para profesionales. No sustituyen la revisión
> de un abogado con cédula. Las leyes y la jurisprudencia cambian: cada skill obliga a
> verificar la vigencia de los artículos y plazos y a marcar `[VERIFICAR]` en lugar de
> inventar tesis.

## Skills por puesto

| Puesto | Skill | Para qué |
|---|---|---|
| Abogado del contribuyente (actor) | `abogado-actor-demanda-nulidad` | Diagnóstico, demanda de nulidad, conceptos de impugnación, ampliación y alegatos |
| Abogado de la autoridad (SAT/IMSS/INFONAVIT) | `abogado-autoridad-demandada` | Contestación, improcedencia y sobreseimiento, refutación, allanamiento |
| Magistrado Instructor / Secretario de Estudio y Cuenta | `magistrado-proyecto-sentencia` | Acuerdos, interlocutorias, proyecto de sentencia y efectos del art. 52 |
| Perito contable | `perito-contable-fiscal` | Dictamen pericial, revisión del dictamen contrario y repreguntas |
| Contador fiscal / contralor | `contador-fiscal-defensa` | Materialidad, mapa de observaciones, cédulas y cuantificación |
| Asesor de PRODECON | `asesor-prodecon` | Quejas, acuerdos conclusivos y representación gratuita |
| Litigante de segunda instancia | `litigante-amparo-revision-fiscal` | Amparo directo, adhesivo, revisión fiscal, reclamación y queja |
| Coordinador del expediente / pasante | `control-plazos-expediente` | Cómputo de plazos (script), agenda, índice del expediente y reportes |

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

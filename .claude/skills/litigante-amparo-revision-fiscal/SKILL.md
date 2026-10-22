---
name: litigante-amparo-revision-fiscal
description: Actúa como litigante de segunda instancia contra sentencias del TFJA en materia fiscal: amparo directo (contribuyente) y recurso de revisión fiscal (autoridad) ante Tribunales Colegiados de Circuito, incluyendo amparo adhesivo, recurso de revisión en amparo directo ante la SCJN, recurso de reclamación y queja por incumplimiento ante el TFJA. Usa esta skill siempre que el usuario pierda o gane parcialmente un juicio fiscal y pregunte qué sigue, quiera redactar una demanda de amparo directo, conceptos de violación, agravios de revisión fiscal, un amparo adhesivo, o analizar la procedencia de la revisión del art. 63 LFPCA.
---

# Litigio posterior a la sentencia del TFJA: amparo directo y revisión fiscal

La sentencia del TFJA no es el final. El contribuyente acude al **amparo directo** y la autoridad a la **revisión fiscal**, ambos ante el Tribunal Colegiado de Circuito. El cambio de foro cambia la técnica: ya no atacas el acto administrativo, atacas **la sentencia**, y debes combatir **todas** sus consideraciones torales o el planteamiento será inoperante.


## Actualización 2025–2026 (aplica siempre)

Lee `references/actualizacion-normativa-2025-2026.md` antes de citar plazos o artículos; los puntos marcados ⚠️ deben cotejarse con el DOF.

- **Reforma a la Ley de Amparo (DOF, 16 de octubre de 2025)**: **interés legítimo** solo con una afectación real, actual y diferenciada y un beneficio cierto. **Suspensión** a petición de parte, ponderada, con nuevas causales de improcedencia (créditos fiscales firmes, operaciones vinculadas con la UIF y otras) y, en materia fiscal, **eficaz solo con la garantía del interés fiscal** (billete de depósito u otros medios legales, ⚠️ redacción final). Debes acreditar el **interés suspensional**.
- **Reforma judicial**: la **SCJN sesiona solo en Pleno** (no hay Salas desde el 1 de septiembre de 2025). Al invocar jurisprudencia de la **Segunda Sala** (integración anterior), verifica que no se haya interrumpido o superado.
- **Revisión fiscal (art. 63 LFPCA, reforma de 2026)**: se reporta que ahora procede **también contra nulidades por vicios de forma o de procedimiento** (⚠️). Si representas al contribuyente, ya no asumas que una nulidad formal queda firme.
- **Queja ante el TFJA**: con la reforma de 2026 hay multas de 300 a 1,000 UMA por incumplimiento (⚠️). Úsalas en el escrito de queja.

## Marco normativo

- **Ley de Amparo**: arts. 17 (plazo de 15 días), 107, fr. III (procedencia del amparo directo), 170 a 191 (amparo directo y adhesivo), 175 (requisitos de la demanda), 182 (adhesivo), 81, fr. II, y 96 (revisión ante la SCJN: tema de constitucionalidad o de interpretación directa, importancia y trascendencia).
- **LFPCA**: art. 63 (revisión fiscal: 15 días; supuestos de procedencia por cuantía o materia), arts. 57 y 58 (cumplimiento y queja), art. 59 (reclamación contra acuerdos del Magistrado Instructor).
- **Constitución**, art. 104, fr. III, y art. 107.

**Verifica la vigencia de los artículos y plazos, y el cómputo exacto** (desde que surte efectos la notificación). En caso de duda, usa la skill `control-plazos-expediente`.

## Árbol de decisión

```
¿Quién perdió?
├── Contribuyente (validez total o nulidad para efectos insatisfactoria)
│   └── AMPARO DIRECTO (15 días hábiles) → Tribunal Colegiado
│       └── ¿Tema constitucional relevante? → posible revisión ante la SCJN
├── Autoridad (nulidad)
│   └── REVISIÓN FISCAL (art. 63, 15 días) → Tribunal Colegiado
│       └── Revisar la procedencia: cuantía (>3,500 veces UMA, verificar), importancia
│           y trascendencia razonada, o la materia de las fracciones del art. 63
└── Ganancia parcial / el contrario impugna
    └── AMPARO ADHESIVO (art. 182 LA) del ganancioso para fortalecer
        consideraciones o hacer valer violaciones procesales
```

Cuando la autoridad interpone revisión fiscal y el contribuyente promueve amparo, ambos asuntos suelen resolverse en la misma sesión del Colegiado. Toma en cuenta esa interacción en la estrategia.

## Amparo directo: estructura (art. 175 LA)

1. Quejoso, tercero interesado (la autoridad demandada en el juicio) y autoridad responsable (la Sala del TFJA).
2. **Acto reclamado**: la sentencia definitiva, con su fecha y número de expediente.
3. Fecha de notificación.
4. Preceptos constitucionales violados (arts. 14, 16 y 17; 31, fr. IV, si hay tema tributario sustantivo).
5. **Conceptos de violación**:
   - **Violaciones procesales** (art. 172 LA) que trascendieron al resultado, siempre que se hayan preparado en el juicio cuando era exigible.
   - **Violaciones en la sentencia**: incongruencia, falta de exhaustividad, valoración indebida de pruebas, interpretación errónea de la norma o aplicación de una jurisprudencia inexacta.
   - Cada concepto debe identificar la **consideración de la Sala** que se ataca (con la página de la sentencia), por qué es ilegal y qué debió resolverse.
6. Si hay inconstitucionalidad de la norma aplicada, plantéala de forma autónoma.
7. Se presenta **por conducto de la Sala responsable**.

## Revisión fiscal: agravios

1. **Capítulo de procedencia** (fundamental, porque la falta de procedencia lleva al desechamiento): razona expresamente la fracción del art. 63 que se actualiza. Si invocas "importancia y trascendencia", argumenta por qué el asunto es excepcional; no lo afirmes de forma genérica.
2. **Agravios**: combate cada consideración que sustenta la nulidad. Un agravio que no ataca una consideración que por sí sola sostiene el fallo es **inoperante**.
3. No introduzcas argumentos que no se hicieron valer en la contestación (serían novedosos), salvo los que surjan de la propia sentencia.

## Otros medios ante el TFJA

- **Reclamación** (art. 59): contra acuerdos que admiten, desechan o tienen por no presentada la demanda, la contestación o las pruebas; contra las que deciden incidentes y contra el sobreseimiento antes del cierre de instrucción. Plazo: 5 días.
- **Queja** (art. 58): por incumplimiento, repetición del acto, exceso o defecto en el cumplimiento de la sentencia, u omisión de dar cumplimiento.

## Estilo

Técnica de amparo: precisión, sin transcripciones innecesarias y con la sentencia reclamada como eje. Las tesis se citan con rubro y registro digital; si no tienes certeza de ellas, marca `[VERIFICAR]`.

## Lo que no debes hacer

- Repetir los conceptos de impugnación del juicio de nulidad sin vincularlos con la sentencia: es la causa más común de inoperancia.
- Omitir el análisis de procedencia de la revisión fiscal.
- Calcular el plazo sin considerar cuándo surte efectos la notificación ni los días inhábiles del Poder Judicial de la Federación.

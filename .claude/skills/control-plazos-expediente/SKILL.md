---
name: control-plazos-expediente
description: Actúa como coordinador del expediente / pasante / secretario del despacho que controla términos procesales en el juicio fiscal ante el TFJA y en el amparo. Usa esta skill siempre que el usuario pregunte "¿cuándo vence?", necesite computar un plazo en días hábiles (demanda de nulidad, contestación, ampliación, alegatos, reclamación, revisión fiscal, amparo directo, revocación), armar una agenda de vencimientos, organizar o indexar un expediente, o hacer un reporte de estatus del caso para el cliente o el socio.
---

# Control de plazos y gestión del expediente

En el litigio fiscal, un plazo vencido es una pérdida irreparable: la demanda extemporánea se desecha sin estudiar el fondo. Por eso esta skill calcula los plazos con un script determinista, en lugar de contar "de cabeza", y siempre muestra cómo llegó al resultado.


## Actualización 2025–2026 (aplica siempre)

Lee `references/actualizacion-normativa-2025-2026.md` antes de citar plazos o artículos; los puntos marcados ⚠️ deben cotejarse con el DOF.

- **Reforma a la LFPCA (DOF, 9 de junio de 2026)**: los **plazos máximos** del Tribunal y de las partes entran en vigor a los **240 días naturales (≈ 4 de febrero de 2027)**, y la actuación electrónica de autoridades y terceros a los 180 (≈ 6 de diciembre de 2026). En cada expediente, anota **qué régimen aplica** según su fecha de inicio y los transitorios.
- **Boletín Jurisdiccional (art. 65)**: la notificación surte efectos al **2.º día hábil** (⚠️), no al día siguiente. Para una notificación por boletín, usa `--surte-efectos-dia 2` en el script.
- **Ampliación (art. 17)**: el plazo es dudoso, entre **10 y 20 días** ⚠️. **Agenda siempre el menor** hasta verificarlo.
- **Garantía en la revocación**: 6 meses desde la interposición del recurso (transitorio de la LIF 2026, ⚠️). Agéndalo como un vencimiento.

## Cálculo de plazos

Usa siempre el script:

```bash
python3 <ruta-de-esta-skill>/scripts/plazos.py <fecha_notificacion AAAA-MM-DD> <dias> \
    [--calendario tfja|amparo] [--inhabil AAAA-MM-DD ...] [--vacaciones INICIO:FIN ...] \
    [--surte-efectos-dia N] [--surte-efectos-mismo-dia]
```

El script aplica la regla general: la notificación surte efectos el día hábil siguiente y el plazo corre a partir del día hábil siguiente a ese. Descuenta sábados, domingos y los días inhábiles fijos por ley (art. 12 CFF / art. 74 LFT para el TFJA; art. 19 de la Ley de Amparo para el PJF).

**Lo que el script no sabe y debes pedir o investigar:**
- **Periodos vacacionales** del TFJA y del PJF del año en curso (se publican por acuerdo; suelen caer en la segunda quincena de julio y la segunda de diciembre, pero **confírmalo**).
- **Suspensiones de labores** extraordinarias (acuerdos del Pleno o de la Junta de Gobierno del TFJA, o del CJF).
- **Notificaciones por buzón tributario o boletín**, cuya regla de surtimiento puede variar; pregunta cómo se notificó.

Si no tienes esa información, entrega el resultado con la advertencia expresa: **"vencimiento calculado sin considerar vacaciones ni suspensiones; verificar"**, y sugiere presentar con días de anticipación.

## Plazos frecuentes (verificar la vigencia)

| Actuación | Plazo | Fundamento |
|---|---|---|
| Recurso de revocación | 30 días hábiles | art. 121 CFF |
| Demanda de nulidad, vía ordinaria | 30 días hábiles | art. 13 LFPCA |
| Demanda, vía sumaria (hasta 30 UMA anuales tras la reforma de 2026 ⚠️) | verificar el texto vigente | arts. 58-2 y 58-3 LFPCA |
| Contestación de la demanda | 30 días hábiles | art. 19 LFPCA |
| Ampliación de la demanda | **10 o 20 días ⚠️**: agenda el menor | art. 17 LFPCA |
| Desahogo de una prevención | 5 días | arts. 14 y 15 LFPCA |
| Alegatos | 5 días | art. 47 LFPCA |
| Recurso de reclamación | 5 días | art. 59 LFPCA |
| Revisión fiscal (autoridad) | 15 días | art. 63 LFPCA |
| Amparo directo | 15 días | art. 17 Ley de Amparo |
| Amparo adhesivo | 15 días desde que se notifica la admisión del principal | art. 181 Ley de Amparo |
| Cumplimiento de la sentencia (autoridad) | 4 meses (vía sumaria: 1 mes ⚠️) | art. 52 LFPCA |
| Acuerdos del TFJA sobre promociones | 5 días (plazos máximos vigentes ≈ 4 de febrero de 2027) | reforma LFPCA 2026 |

Esta tabla es una guía. **Antes de dar un vencimiento como definitivo, confirma el artículo vigente.**

## Agenda de vencimientos

Cuando el usuario maneje varios asuntos, entrega una tabla ordenada por fecha:

| Vence | Expediente | Cliente | Actuación | Notificado | Días | Responsable | Estatus |

Marca en **negritas** lo que vence en los próximos 5 días hábiles. Propón **fechas internas** con 3 días hábiles de anticipación para revisión.

## Índice del expediente

Para organizar un expediente, usa carpetas numeradas:

```
00_Control (agenda, bitácora, reporte de estatus)
01_Acto_impugnado_y_notificacion
02_Procedimiento_administrativo (orden, actas, oficio de observaciones)
03_Recurso_revocacion (si hubo)
04_Demanda_y_anexos
05_Contestacion_y_ampliacion
06_Pruebas (periciales, documentales)
07_Acuerdos_y_notificaciones_TFJA
08_Alegatos
09_Sentencia
10_Amparo_o_revision
11_Cumplimiento
```

Cada documento lleva el prefijo `AAAA-MM-DD_` con la fecha del documento.

## Reporte de estatus para el cliente

Una página, en lenguaje no técnico:
1. Dónde estamos (etapa procesal).
2. Qué pasó desde el último reporte.
3. Próximo paso y su fecha.
4. Qué necesitamos del cliente.
5. Riesgos o cambios en el pronóstico (si los hay; el pronóstico es responsabilidad del abogado).

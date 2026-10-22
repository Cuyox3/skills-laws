# Mapa de actores del juicio fiscal en México

Quién es quién en el ciclo completo: fiscalización → recurso → juicio de nulidad →
amparo o revisión, y qué skill del repo atiende a cada puesto.

## A. Hacienda y autoridades fiscales (la parte que emite o defiende el acto)

| Institución | Puestos clave | Papel en el conflicto | Skill |
|---|---|---|---|
| **SAT**: Administración General de Auditoría Fiscal Federal (AGAFF) y sus Administraciones Desconcentradas de Auditoría Fiscal | Administrador, subadministrador, jefe de departamento, **auditor / visitador**, supervisor | Ordena y practica visitas, revisiones de gabinete y electrónicas; emite **liquidaciones** | `funcionario-sat-fiscalizacion` |
| SAT: Administración General de **Grandes Contribuyentes** (AGGC) | Administradores centrales de fiscalización (sector financiero, empresas, precios de transferencia, internacional) | Fiscaliza a los grandes contribuyentes y a los grupos multinacionales | `funcionario-sat-fiscalizacion` y `especialista-tecnico-fiscal` |
| SAT: Administración General de **Hidrocarburos** (AGH) | Fiscalizadores del sector energético | Fiscaliza contratistas y asignatarios | `funcionario-sat-fiscalizacion` |
| SAT: Administración General de Auditoría de **Comercio Exterior** (AGACE) | Auditores de comercio exterior | Revisa operaciones de importación y exportación, IMMEX y certificaciones | `especialista-tecnico-fiscal` |
| SAT: Administración General **Jurídica** (AGJ) y **Administraciones Desconcentradas Jurídicas** (ADJ) | Administrador jurídico, **abogado tributario / litigante de la autoridad** | Resuelve **recursos de revocación**; representa al SAT ante el TFJA y en amparo; **contesta demandas** | `abogado-autoridad-demandada` |
| SAT: Administración General de **Recaudación** (AGR) | Ejecutores, notificadores | **Procedimiento administrativo de ejecución** (PAE), embargos, garantías del art. 141 | `funcionario-sat-fiscalizacion` |
| SAT: Administración General de **Servicios al Contribuyente** (AGSC) | Orientadores | Devoluciones y trámites; aclaraciones de CSD | `asesor-prodecon` (cuando hay conflicto) |
| **SHCP – Procuraduría Fiscal de la Federación (PFF)** | Procurador fiscal; Subprocuradurías de **Legislación y Consulta**, **Amparos**, **Asuntos Financieros** e **Investigaciones** | Defiende la constitucionalidad de las leyes fiscales en el **amparo contra leyes**; formula **querellas por delitos fiscales**; emite opiniones jurídicas | `procuraduria-fiscal-federacion` |
| **ANAM** (Agencia Nacional de Aduanas de México) | Administradores de aduana | PAMA, resoluciones en materia aduanera | `especialista-tecnico-fiscal` |
| **IMSS / INFONAVIT** | Subdelegaciones, jefaturas de servicios jurídicos | Capitales constitutivos, cuotas obrero-patronales y su defensa ante el TFJA | `abogado-autoridad-demandada`, `especialista-tecnico-fiscal` |
| Autoridades fiscales **estatales coordinadas** (Convenio de Colaboración Administrativa) | Secretarías de Finanzas estatales | Fiscalizan impuestos federales en ingresos coordinados; son demandadas ante el TFJA | `abogado-autoridad-demandada` |

## B. Órganos jurisdiccionales (quienes resuelven)

| Órgano | Puestos | Qué resuelve | Skill |
|---|---|---|---|
| **TFJA – Salas Regionales** (ordinarias, auxiliares y especializadas; las de comercio exterior se suprimieron en 2024) | **Magistrado(a) instructor(a)**, magistrados integrantes, **secretario(a) de acuerdos**, actuario(a), oficial jurisdiccional | Juicio de nulidad en primera instancia (ordinario, sumario, en línea) | `magistrado-proyecto-sentencia` |
| TFJA – **Sala Superior** (Pleno jurisdiccional y Secciones) | Magistrados de Sala Superior; secretarios de **estudio y cuenta** | Facultad de atracción, contradicción de criterios, **jurisprudencia del TFJA** | `magistrado-proyecto-sentencia` |
| **Juzgados de Distrito** en materia administrativa (PJF) | Juez(a) de Distrito, secretario(a) proyectista | **Amparo indirecto** contra leyes fiscales (autoaplicativas o heteroaplicativas) y contra actos fuera de juicio | `juzgador-amparo-fiscal` |
| **Tribunales Colegiados de Circuito** en materia administrativa | Magistrados de circuito; secretarios proyectistas | **Amparo directo** contra sentencias del TFJA; **revisión fiscal**; revisión en amparo indirecto | `juzgador-amparo-fiscal`, `litigante-amparo-revision-fiscal` |
| **SCJN** (Pleno; sin Salas desde septiembre de 2025) | Ministras y ministros; secretarios de estudio y cuenta | Revisión en amparo directo e indirecto con tema constitucional; contradicciones de criterios | `juzgador-amparo-fiscal` |
| OAJ / Tribunal de Disciplina Judicial | — | Administración y disciplina del PJF (no resuelven el fondo fiscal) | — |

## C. Abogados

| Perfil | Skill |
|---|---|
| Litigante fiscal del contribuyente (despacho, *in-house*) | `abogado-actor-demanda-nulidad` |
| Litigante de amparo fiscal (contra leyes, amparo directo) | `litigante-amparo-revision-fiscal` |
| Abogado de la autoridad (AGJ, ADJ, PFF, IMSS) | `abogado-autoridad-demandada`, `procuraduria-fiscal-federacion` |
| Asesor de PRODECON y defensor del contribuyente | `asesor-prodecon` |
| Penalista fiscal (defraudación, art. 108 CFF; EFOS) | `procuraduria-fiscal-federacion` (lado querellante); para la defensa penal, ver las notas de esa skill |

## D. Especialistas técnicos

| Perfil | Skill |
|---|---|
| Contador fiscal / contralor del contribuyente | `contador-fiscal-defensa` |
| **Perito** contable (de parte o tercero) | `perito-contable-fiscal` |
| Contador público inscrito (CPI) que dictamina estados financieros (art. 32-A CFF) | `contador-fiscal-defensa` |
| Especialista en **precios de transferencia** (arts. 76, 179 y 180 LISR) | `especialista-tecnico-fiscal` |
| Especialista en **comercio exterior y aduanas** (LA, LIGIE, T-MEC) | `especialista-tecnico-fiscal` |
| Especialista en **seguridad social** (LSS, Ley del INFONAVIT) | `especialista-tecnico-fiscal` |
| Coordinador del expediente, pasante, paralegal | `control-plazos-expediente` |

## E. Academia y docencia

| Institución / foro | Relevancia |
|---|---|
| UNAM: Facultad de Derecho (División de Estudios de Posgrado) e **Instituto de Investigaciones Jurídicas** (IIJ) | Doctrina, Biblioteca Jurídica Virtual y revistas arbitradas |
| **Escuela Libre de Derecho**, **ITAM**, **Universidad Panamericana**, **Universidad Iberoamericana**, **ITESM** y otras | Especialidades y maestrías en derecho fiscal |
| **Centro de Estudios Superiores en materia de Derecho Fiscal y Administrativo** del TFJA (CESMDFA) | Formación de juzgadores; *Revista Praxis de la Justicia Fiscal y Administrativa* |
| **Instituto de la Judicatura Federal / Escuela Federal de Formación Judicial** | Formación de los juzgadores del PJF |
| **INDETEC** (Instituto para el Desarrollo Técnico de las Haciendas Públicas) | Coordinación fiscal y haciendas locales |
| **Academia Mexicana de Derecho Fiscal**, **IMCP** (Comisión Fiscal), **Colegio de Contadores Públicos de México**, **ANADE**, **Barra Mexicana Colegio de Abogados** (Comité Fiscal) | Foros profesionales, boletines y posturas técnicas |
| **PRODECON**: publicaciones institucionales y criterios sustantivos | Análisis sistémicos y criterios |

Skill: `docente-investigador-derecho-fiscal`.

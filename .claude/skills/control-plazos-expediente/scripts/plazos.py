#!/usr/bin/env python3
"""Calculadora de plazos en días hábiles para el juicio fiscal (TFJA) y el amparo.

Regla general que aplica:
  1. La notificación surte efectos el día hábil siguiente a aquel en que se practicó
     (art. 70 LFPCA; art. 31, fr. II, Ley de Amparo para particulares).
  2. El plazo empieza a correr el día hábil siguiente a aquel en que surtió efectos.
  3. Se cuentan solo días hábiles; el vencimiento es el último día del plazo.

Los días inhábiles fijos vienen de la ley; los periodos vacacionales y los
suspensiones de labores del TFJA o del PJF cambian cada año y DEBEN pasarse con
--inhabil / --vacaciones a partir de los acuerdos oficiales.

Uso:
  python3 plazos.py 2026-10-01 30
  python3 plazos.py 2026-10-01 15 --calendario amparo
  python3 plazos.py 2026-12-08 30 --vacaciones 2026-12-16:2026-12-31 --inhabil 2026-11-02
  python3 plazos.py 2026-10-01 30 --surte-efectos-mismo-dia   # p. ej. autoridades en amparo
"""
import argparse
import datetime as dt


def nth_weekday(year, month, weekday, n):
    d = dt.date(year, month, 1)
    d += dt.timedelta(days=(weekday - d.weekday()) % 7)
    return d + dt.timedelta(weeks=n - 1)


def fixed_holidays(year, calendario):
    """Días inhábiles por ley. tfja: art. 12 CFF / art. 74 LFT; amparo: art. 19 Ley de Amparo."""
    if calendario == "amparo":
        days = {
            dt.date(year, 1, 1), dt.date(year, 2, 5), dt.date(year, 3, 21),
            dt.date(year, 5, 1), dt.date(year, 5, 5), dt.date(year, 9, 14),
            dt.date(year, 9, 16), dt.date(year, 10, 12), dt.date(year, 11, 20),
            dt.date(year, 12, 25),
        }
    else:
        days = {
            dt.date(year, 1, 1),
            nth_weekday(year, 2, 0, 1),   # primer lunes de febrero
            nth_weekday(year, 3, 0, 3),   # tercer lunes de marzo
            dt.date(year, 5, 1), dt.date(year, 5, 5), dt.date(year, 9, 16),
            nth_weekday(year, 11, 0, 3),  # tercer lunes de noviembre
            dt.date(year, 12, 25),
        }
    if (year - 2024) % 6 == 0:            # transmisión del Poder Ejecutivo
        days.add(dt.date(year, 10, 1))
    return days


DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


def parse_date(s):
    return dt.date.fromisoformat(s)


def build_inhabiles(args, years):
    extra = {parse_date(d) for d in args.inhabil}
    for rango in args.vacaciones:
        ini, fin = (parse_date(x) for x in rango.split(":"))
        d = ini
        while d <= fin:
            extra.add(d)
            d += dt.timedelta(days=1)
    fixed = set()
    for y in years:
        fixed |= fixed_holidays(y, args.calendario)
    return fixed, extra


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("notificacion", help="Fecha en que se practicó la notificación (AAAA-MM-DD)")
    p.add_argument("dias", type=int, help="Número de días hábiles del plazo")
    p.add_argument("--calendario", choices=["tfja", "amparo"], default="tfja")
    p.add_argument("--inhabil", action="append", default=[], help="Día inhábil adicional (repetible)")
    p.add_argument("--vacaciones", action="append", default=[], help="Rango inhábil INICIO:FIN (repetible)")
    p.add_argument("--surte-efectos-mismo-dia", action="store_true",
                   help="La notificación surte efectos el mismo día (no se agrega el día de surtimiento)")
    args = p.parse_args()

    notif = parse_date(args.notificacion)
    fixed, extra = build_inhabiles(args, range(notif.year, notif.year + 3))

    def habil(d):
        return d.weekday() < 5 and d not in fixed and d not in extra

    def siguiente_habil(d):
        d += dt.timedelta(days=1)
        while not habil(d):
            d += dt.timedelta(days=1)
        return d

    surte = notif if args.surte_efectos_mismo_dia else siguiente_habil(notif)
    d = surte
    contados = []
    while len(contados) < args.dias:
        d = siguiente_habil(d)
        contados.append(d)

    saltados = sorted(x for x in (fixed | extra) if contados[0] <= x <= contados[-1] and x.weekday() < 5)
    print(f"Calendario:            {args.calendario}")
    print(f"Notificación:          {notif.isoformat()} ({DIAS[notif.weekday()]})")
    print(f"Surte efectos:         {surte.isoformat()}")
    print(f"Primer día del plazo:  {contados[0].isoformat()}")
    print(f"VENCIMIENTO ({args.dias} días): {contados[-1].isoformat()} ({DIAS[contados[-1].weekday()]})")
    if saltados:
        print("Días inhábiles (entre semana) descontados: " + ", ".join(x.isoformat() for x in saltados))
    print("\nAVISO: verifique los acuerdos de días inhábiles y vacaciones del TFJA/PJF del año.")


if __name__ == "__main__":
    main()

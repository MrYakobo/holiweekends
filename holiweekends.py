#!/usr/bin/env python3

import argparse
import locale
from collections import defaultdict
from datetime import datetime

import holidays

locale.setlocale(locale.LC_ALL, "sv_SE.UTF-8")


def make_report(bad_days):
    s = ""
    sorted_by_num_days = sorted(bad_days.items(), key=lambda x: [len(x[1]), x[0]])
    for year, days in sorted_by_num_days:
        num_days = len(days)

        if num_days == 0:
            s += f"# År {year} är ett kanonår\nInga datumbaserade högtider infaller på helger\n\n"

        else:
            joined = "\n- ".join(days)
            in_future = year > datetime.now().year
            verb = "infaller" if in_future else "inföll"
            plural = f"högtid{'er' if num_days > 1 else ''}"

            s += f"# År {year} {verb} {num_days} {plural} på helgen\n- {joined}\n\n"

    return s


def calc_bad_days(thisyear, horizon):
    bad_days = defaultdict(list)
    holiday_names = holidays.Sweden(include_sundays=False)

    for year in range(thisyear - horizon, thisyear + horizon + 1):
        for holiday in holidays.Sweden(include_sundays=False, years=year):
            holiday_is_weekend = holiday.isoweekday() >= 6
            if holiday_is_weekend:
                desc = f"{holiday_names.get(holiday, None)} ({holiday.strftime('%A')})"

                bad_days[year].append(desc)

    # There are holidays that always occur on weekends
    # (for example, Påskdagen is always on saturday)
    # Those days are not interesting for our report
    common_to_all_years = set.intersection(*map(set, bad_days.values()))
    for year, descs in bad_days.items():
        bad_days[year] = [desc for desc in descs if desc not in common_to_all_years]

    return bad_days


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--year",
        type=int,
        default=datetime.now().year,
        help="Center report around this year (default: %(default)s)",
    )
    parser.add_argument(
        "--horizon",
        type=int,
        default=5,
        help="Look this number of years forward and backwards (default: %(default)s)",
    )
    args = parser.parse_args()

    bad_days = calc_bad_days(args.year, args.horizon)
    report = make_report(bad_days)
    print(report)


if __name__ == "__main__":
    main()

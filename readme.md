# Holidays in Weekends

We all hate it when it happens: you wake up, realize it is Saturday and
1st of May at the same time. You get depressed, realizing that another vacation day was lost between the cracks of dates and weekdays.

With this in mind, there are good years and bad years, that contain different amounts of holidays that occur during the weekend. What better way is there to predict those years than writing a python script for it!!!

The `holiweekends.py` script generates a Swedish markdown report to stdout.
Put this in some web server or something. I can't possibly put any more time into this useless project anymore.

## Example usage

```bash
$ pip3 install -r requirements.txt
$ ./holiweekends.py --year 2023 --horizon 5
```

```markdown
# År 2025 är ett kanonår
Inga datumbaserade högtider infaller på helger

# År 2018 inföll 1 högtid på helgen
- Trettondedag jul (Lördag)

# År 2019 inföll 1 högtid på helgen
- Trettondedag jul (Söndag)

# År 2024 infaller 1 högtid på helgen
- Trettondedag jul (Lördag)

# År 2020 inföll 2 högtider på helgen
- Sveriges nationaldag (Lördag)
- Annandag jul (Lördag)

# År 2026 infaller 2 högtider på helgen
- Sveriges nationaldag (Lördag)
- Annandag jul (Lördag)

# År 2023 inföll 3 högtider på helgen
- Nyårsdagen (Söndag)
- Julafton (Söndag)
- Nyårsafton (Söndag)

# År 2028 infaller 3 högtider på helgen
- Nyårsdagen (Lördag)
- Julafton (Söndag)
- Nyårsafton (Söndag)

# År 2021 inföll 4 högtider på helgen
- Första maj (Lördag)
- Sveriges nationaldag (Söndag)
- Juldagen (Lördag)
- Annandag jul (Söndag)

# År 2027 infaller 4 högtider på helgen
- Första maj (Lördag)
- Sveriges nationaldag (Söndag)
- Juldagen (Lördag)
- Annandag jul (Söndag)

# År 2022 inföll 5 högtider på helgen
- Nyårsdagen (Lördag)
- Första maj (Söndag)
- Julafton (Lördag)
- Juldagen (Söndag)
- Nyårsafton (Lördag)
```

## Dependencies

Depends on [dr-prodigy/python-holidays](https://github.com/dr-prodigy/python-holidays).
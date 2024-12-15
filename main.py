from datetime import datetime

dates = {
    "The Moscow Times": "Wednesday, October 2, 2002",
    "The Guardian": "Friday, 11.10.13",
    "Daily News": "Thursday, 18 August 1977"
}
formats = {
    "The Moscow Times": "%A, %B %d, %Y",  # Полный день недели, полный месяц, день и год (YYYY)
    "The Guardian": "%A, %d.%m.%y",       # Полный день недели, день.месяц.год (YY)
    "Daily News": "%A, %d %B %Y"          # Полный день недели, день месяц, год (YYYY)
}
datetime_objects = {newspaper: datetime.strptime(date, formats[newspaper]) for newspaper, date in dates.items()}

for newspaper, date in datetime_objects.items():
    print(f"{newspaper}: {date}")

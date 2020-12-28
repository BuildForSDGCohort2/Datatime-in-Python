import datetime
import pytz

today = datetime.date.today()
print(today)
print()

birthday = datetime.date(1994, 4, 21)
print(birthday)
print()

#find days since birth 
days_since_birth = ((today - birthday).days/365)
print(days_since_birth)
print()

#adding 10 days to current days
tdelta = datetime.timedelta(days=10)
print(today + tdelta)
print()

print(today.day)
print()

# saturday = 5
print(today.weekday())
print()

# Monday = 0, Sunday = 6
print(datetime.time(7, 2, 20, 15))
# datetime.date (Y, M, D)
# datetime.time (h, m, s, ms)
# datetime.datetime (Y, M, D, h, m, s, ms)

# Add 10 hours to current day
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)
print()

datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('Etc/GMT+3'))
print(datetime_pacific)
print()

# Show all the timezones
for tz in pytz.all_timezones:
  print(tz)

print()

# String formatting with dates
# 2020-12-28 -> December 28, 2020
# we use strftime (f = formatting)
print(datetime_pacific.strftime('%B %d, %Y'))
print()

# December 28, 2020 -> datetime (2020, 12, 28)
# we use strptime (p = parsing)
datetime_thing = datetime.datetime.strptime('December 28, 2020', '%B %d, %Y')
print(repr(datetime_thing))
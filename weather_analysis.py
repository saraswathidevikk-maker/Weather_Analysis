
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

weather = {
    "Kochi": {
        "temp": [31, 32, 30, 29, 31, 33, 32],
        "rain": [0, 5, 12, 20, 0, 0, 3]
    },
    "Munnar": {
        "temp": [18, 19, 17, 16, 18, 20, 19],
        "rain": [2, 8, 15, 25, 5, 0, 4]
    },
    "Palakkad": {
        "temp": [36, 37, 38, -999, 37, 39, 38],
        "rain": [0, 0, 0, 0, 0, 0, 0]
    },
    "Kozhikode": {
        "temp": [30, 31, 30, 29, 30, 32, 31],
        "rain": [0, 10, 8, 18, 2, 0, 1]
    }
}

def clean(values):
    new_temp= []
    for value in values:
        if value >= -20:
            new_temp.append(value)
    return new_temp

print("SENSOR CHECK")
print("-"*60)

for city in sorted(weather):
    values= weather[city]["temp"]
    cleaned_values= clean(values)
    invalid_count = len(values) - len(cleaned_values)
    print(f"{city:<10} {invalid_count} invalid reading(s)")
print()



print("Weekly Summary")
print("-"*60)
print(f"{'City':<10} {'Avg':>7} {'Max':>6} {'Min':>6} {'Rain':>7} {'Rainy':>7}")

# Calculate average temperature
def average(values):
    return sum(values) / len(values)

for city1 in sorted(weather):
    tp1= weather[city1]["temp"]
    cleaned_tp1= clean(tp1)
    rain1= weather[city1]["rain"]

    avg_temp= average(cleaned_tp1)
    max_temp= max(cleaned_tp1)
    min_temp= min(cleaned_tp1)
    total_rain= sum(rain1)

    rainy_days=0
    for rain in rain1:
        if rain > 0:
            rainy_days+= 1

    print(f"{city:<10} {avg_temp:>7.1f} {max_temp:>6} {min_temp:>6} {total_rain:>6} {rainy_days:>6}")

    print("DAY TYPES")
print("-"*40)
print(f"{'City':<10} {'Hot':>7} {'Warm':>8} {'Cool':>8}")
def day_type(temp, hot=35, warm=28):
    if temp >= hot:
        return "Hot"
    elif temp >= warm:
        return "Warm"
    else:
        return "Cool"
for City in sorted(weather):
    tp1= weather[city]["temp"]
    cleaned_tp1= clean(tp1)
    counts ={}

    for temp in cleaned_tp1:
      tp2= day_type(temp)
      counts[tp2]= counts.get(tp2,0)+1
    print(f"{city:<10}{counts.get('Hot', 0):>7}{counts.get('Warm', 0):>8}{counts.get('Cool', 0):>9}")



# Task 5

def city_averages(weather):
    averages = {}

    for ct in weather:
        temp3 = weather[ct]["temp"]
        cleaned_temp3 = clean(temp3)
        averages[ct] = average(cleaned_temp3)

    return averages


def extremes(averages):
    hottest_city = ""
    coolest_city = ""

    hottest_temp = float("-inf")
    coolest_temp = float("inf")

    for city, avg in averages.items():
        if avg > hottest_temp:
            hottest_temp = avg
            hottest_city = city

        if avg < coolest_temp:
            coolest_temp = avg
            coolest_city = city

    return hottest_city, coolest_city


averages = city_averages(weather)

hottest, coolest = extremes(averages)

print()
print(f"Hottest city: {hottest} ({averages[hottest]:.1f})")
print(f"Coolest city: {coolest} ({averages[coolest]:.1f})")

#Task 6
daily_rain = {}

for i, day in enumerate(days):
  total=0

  for city in weather:
    total += weather[city]["rain"][i]
    daily_rain[day] = total

print()
print("RAINFALL BY DAY")

for day,total in daily_rain.items():
  print(f"{day:5}{total:4} mm")

wettest_day =""
highest_rain = 0

for day, total in daily_rain.items():
    if total > highest_rain:
        highest_rain = total
        wettest_day = day
print()
print(f"Wettest day :{wettest_day}{highest_rain} mm")

#Task 7
def heavy_rain(day_index,limit=20):
  alerts =[]

  for city in weather:
    mm= weather[city]["rain"][day_index]
    if mm >=limit:
      alerts.append((city,mm))
  alerts.sort(key=lambda x:  x[0])

  return alerts
print()
print("Rain Alerts (20 mm or more)")

for i,day in enumerate(days):
  alerts = heavy_rain(i)
  if alerts:
    details =",".join(f"{city}{mm} mm" for city, mm in alerts)
    print(f"{day}:{details}")


print()
print("Rain Alerts (10 mm or more)")

for i,day in enumerate(days):
  alerts = heavy_rain(i,limit=10)

  if alerts:
    details = ",".join(f"{city}{mm} mm" for city, mm in alerts)
    print(f"{day}:{details}")
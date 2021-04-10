duration = int(input("Введите нужное количество секунд "))

hours = duration // 3600
minutes = (duration - 3600 * hours) // 60
seconds = 0
days = 0

if duration == 0:
    seconds = 0
    print(seconds, "сек")
elif duration > 0 and duration < 60:
    seconds = duration
    print(seconds, "сек")
elif duration >= 60 and duration < 3600:
    seconds = (duration - 60 * minutes)
    print(minutes, "мин", seconds, "сек")
else:
    seconds = (duration - (3600 * hours + 60 * minutes))
    print(hours, "час", minutes, "мин", seconds, "сек")

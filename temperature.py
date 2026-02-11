print("🌡️ Temperature Checker")
temp = float(input("Enter temperature (°C): "))

if temp < 0:
    print("❄️ Freezing cold! rainy")
elif temp < 15:
    print("🥶 Chilly")
elif temp < 25:
    print("😊 Perfect weather")
elif temp < 35:
    print("🥵 Hot")
else:
    print("🔥 Extreme heat!")
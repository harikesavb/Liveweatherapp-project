from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from PIL import Image, ImageTk
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Weather App")
        self.root.geometry("400x300")
        self.root.resizable(0, 0)

        self.city_var = StringVar()

        Label(root, text="Enter City:").pack(pady=10)
        Entry(root, textvariable=self.city_var).pack(pady=10)

        Button(root, text="Get Weather", command=self.get_weather).pack(pady=10)

        self.weather_label = Label(root, text="", font=("Helvetica", 18))
        self.weather_label.pack(pady=10)

        self.icon_label = Label(root)
        self.icon_label.pack(pady=10)

    def get_weather(self):
        city = self.city_var.get()
        if not city:
            messagebox.showerror("Error", "Please enter a city.")
            return

        api_key = "b79febad6f2b5e628a63c32cbeb8a63d"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather_description = data["weather"][0]["description"]
                icon = data["weather"][0]["icon"]

                self.weather_label.config(text=f"Weather: {weather_description}")

                img_url = f"http://openweathermap.org/img/w/{icon}.png"
                img_data = requests.get(img_url).content
                img = ImageTk.PhotoImage(Image.open((img_data)))

                self.icon_label.config(image=img)
                self.icon_label.image = img
            else:
                messagebox.showerror("Error", f"Error: {data['message']}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    app = WeatherApp(root)
    root.mainloop()

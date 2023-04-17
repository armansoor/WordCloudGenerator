import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog

class WordCloudGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Word Cloud Generator")

        self.url_label = tk.Label(master, text="Enter a URL:")
        self.url_label.pack()

        self.url_entry = tk.Entry(master)
        self.url_entry.pack()

        self.generate_button = tk.Button(master, text="Generate", command=self.generate_word_cloud)
        self.generate_button.pack()

    def generate_word_cloud(self):
        url = self.url_entry.get()

        # Fetch the text from the URL
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text()

        # Generate the word cloud
        wordcloud = WordCloud(width=800, height=800, background_color='white',
                              min_font_size=10, colormap='Blues').generate(text)

        # Display the word cloud
        plt.figure(figsize=(8,8), facecolor=None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)
        plt.show()

root = tk.Tk()
word_cloud_generator = WordCloudGenerator(root)
root.mainloop()

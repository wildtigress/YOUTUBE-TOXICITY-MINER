"""
gui.py – dark desktop app with your key
"""
import os, tkinter.filedialog, threading
import customtkinter as ctk
from miner import CommentMiner

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Comment Miner")
        self.geometry("500x350")
        self.miner = CommentMiner()
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="YouTube URL:").pack(pady=10)
        self.url = ctk.CTkEntry(self, width=400)
        self.url.pack()
        ctk.CTkButton(self, text="Start Mining", command=self.start).pack(pady=10)
        self.progress = ctk.CTkProgressBar(self, width=400)
        self.progress.set(0)
        self.progress.pack(pady=10)
        self.status = ctk.CTkLabel(self, text="Ready")
        self.status.pack()

    def start(self):
        threading.Thread(target=self.run, daemon=True).start()

    def run(self):
        url = self.url.get()
        self.status.configure(text="Working…")
        self.progress.start()
        try:
            df = self.miner.fetch(url)
            path = tkinter.filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel", "*.xlsx"), ("CSV", "*.csv"), ("JSON", "*.json")])
            if path:
                if path.endswith(".csv"):
                    df.to_csv(path, index=False)
                elif path.endswith(".json"):
                    df.to_json(path, orient="records", indent=2, force_ascii=False)
                else:
                    df.to_excel(path, index=False)
                self.status.configure(text=f"Saved {len(df)} rows")
        except Exception as e:
            self.status.configure(text=str(e))
        finally:
            self.progress.stop()

if __name__ == "__main__":
    App().mainloop()
import os
import shutil
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from datetime import datetime
import threading
from pathlib import Path
import webbrowser
import winreg

class Sims4BackupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Sims 4 Backup")
        self.root.geometry("650x600")
        self.root.resizable(False, False)  # Prevent resizing
        
        # Set window icon - try multiple paths for exe and script
        icon_loaded = False
        icon_paths = [
            Path(__file__).parent / "ToppingSimsBackup.ico",  # Same folder as script
            Path("ToppingSimsBackup.ico"),  # Current directory
            Path(os.getcwd()) / "ToppingSimsBackup.ico",  # Working directory
        ]
        
        for icon_path in icon_paths:
            try:
                if icon_path.exists():
                    self.root.iconbitmap(str(icon_path))
                    icon_loaded = True
                    break
            except:
                continue
        
        if not icon_loaded:
            # Try without path (might work if in system path)
            try:
                self.root.iconbitmap("ToppingSimsBackup.ico")
            except:
                pass  # Silently fail if icon not found
        
        # Predefined folders to backup
        self.folders_to_backup = [
            r"C:\Users\maria\Documents\Electronic Arts\The Sims 4\Mods",
            r"C:\Users\maria\Documents\Electronic Arts\The Sims 4\saves",
            r"C:\Users\maria\Documents\Electronic Arts\The Sims 4\Tray"
        ]
        
        # Registry key for storing settings
        self.registry_key = r"Software\ToppingSims4Backup"
        
        # Load saved backup destination or use default
        self.backup_destination = self.load_config()
        if not self.backup_destination:
            self.backup_destination = r"C:\Users\maria\Desktop\TS4\_Backup MIS"
        
        self.create_widgets()
        self.check_folders()
        
    def create_widgets(self):
        # Title frame with colored background
        title_frame = tk.Frame(self.root, bg="#3caad6", height=60)
        title_frame.pack(fill="x")
        title_frame.pack_propagate(False)
        
        title = tk.Label(title_frame, text="The Sims 4 Backup", 
                        font=("Arial", 18, "bold"), fg="white", bg="#3caad6")
        title.pack(expand=True)
        
        # Main content frame
        content_frame = tk.Frame(self.root, bg="#f5f5f5")
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # First box - Folders
        # Title above box
        title1 = tk.Label(content_frame, text="Mapper, der bliver taget backup af", 
                         font=("Arial", 10), anchor="w", bg="#f5f5f5", fg="#333333")
        title1.pack(fill="x", pady=(0, 5))
        
        # Shadow frame for drop shadow effect
        shadow_frame1 = tk.Frame(content_frame, bg="#c0c0c0", highlightthickness=0)
        shadow_frame1.pack(fill="x")
        
        # Main white box
        info_frame = tk.Frame(shadow_frame1, bg="white", highlightthickness=0, 
                             relief="flat", bd=0)
        info_frame.pack(fill="x", padx=(0, 3), pady=(0, 3))
        
        # Content inside box
        inner_padding = tk.Frame(info_frame, bg="white")
        inner_padding.pack(fill="x", padx=20, pady=15)
        
        # List folders
        for folder in self.folders_to_backup:
            folder_name = os.path.basename(folder)
            label = tk.Label(inner_padding, text=f"📁 {folder_name}", 
                           font=("Arial", 10), anchor="w", bg="white", fg="#333333")
            label.pack(fill="x", pady=3)
        
        # Second box - Destination
        # Title above box
        title2 = tk.Label(content_frame, text="Backup placering", 
                         font=("Arial", 10), anchor="w", bg="#f5f5f5", fg="#333333")
        title2.pack(fill="x", pady=(20, 5))
        
        # Shadow frame for drop shadow effect
        shadow_frame2 = tk.Frame(content_frame, bg="#c0c0c0", highlightthickness=0)
        shadow_frame2.pack(fill="x")
        
        # Main white box
        dest_frame = tk.Frame(shadow_frame2, bg="white", highlightthickness=0,
                             relief="flat", bd=0)
        dest_frame.pack(fill="x", padx=(0, 3), pady=(0, 3))
        
        # Content inside box
        inner_padding2 = tk.Frame(dest_frame, bg="white")
        inner_padding2.pack(fill="both", padx=20, pady=15)
        
        # Container for path and button
        dest_container = tk.Frame(inner_padding2, bg="white")
        dest_container.pack(fill="x")
        
        # Path label on the left
        self.dest_label = tk.Label(dest_container, text=self.backup_destination, 
                             font=("Arial", 9), wraplength=420, justify="left", 
                             bg="white", fg="#333333", anchor="w")
        self.dest_label.pack(side="left", fill="x", expand=True)
        
        # Change button on the right
        change_btn = tk.Button(dest_container, text="Skift placering", 
                              command=self.change_destination,
                              bg="#e0e0e0", fg="#333333",
                              font=("Arial", 9),
                              relief="flat",
                              cursor="hand2",
                              padx=10, pady=5)
        change_btn.pack(side="right", padx=(10, 0))
        
        # Status frame
        status_frame = tk.Frame(content_frame, bg="#f5f5f5")
        status_frame.pack(pady=15)
        
        self.status_label = tk.Label(status_frame, text="Klar til backup", 
                                     font=("Arial", 10), fg="blue", bg="#f5f5f5")
        self.status_label.pack()
        
        # Progress bar
        self.progress = ttk.Progressbar(content_frame, length=560, mode='determinate')
        self.progress.pack(pady=5)
        
        self.progress_text = tk.Label(content_frame, text="", font=("Arial", 9), fg="gray", bg="#f5f5f5")
        self.progress_text.pack()
        
        # Custom rounded button using Canvas
        button_container = tk.Frame(content_frame, bg="#f5f5f5")
        button_container.pack(pady=20)
        
        # Create canvas for rounded button
        canvas = tk.Canvas(button_container, width=220, height=60, 
                          bg="#f5f5f5", highlightthickness=0)
        canvas.pack()
        
        # Add method to canvas for creating rounded rectangles
        def create_rounded_rect(x1, y1, x2, y2, radius=10, **kwargs):
            points = [
                x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1
            ]
            return canvas.create_polygon(points, smooth=True, **kwargs)
        
        # Draw rounded rectangle
        self.button_bg = create_rounded_rect(10, 10, 210, 50, radius=10, fill="#3caad6", outline="")
        
        # Add text on top
        self.button_text = canvas.create_text(110, 30, 
                                              text="Start Backup",
                                              font=("Arial", 13, "bold"),
                                              fill="white")
        
        # Bind click events
        canvas.bind("<Button-1>", lambda e: self.start_backup())
        canvas.bind("<Enter>", lambda e: canvas.itemconfig(self.button_bg, fill="#2a9ac5"))
        canvas.bind("<Leave>", lambda e: canvas.itemconfig(self.button_bg, fill="#3caad6"))
        canvas.config(cursor="hand2")
        
        # Store canvas reference for disabling
        self.backup_btn_canvas = canvas
        
        # Footer with link
        footer_frame = tk.Frame(content_frame, bg="#f5f5f5")
        footer_frame.pack(side="bottom", pady=10)
        
        footer_label = tk.Label(footer_frame, text="Topping | ", 
                               font=("Arial", 9), bg="#f5f5f5", fg="#666666")
        footer_label.pack(side="left")
        
        footer_link = tk.Label(footer_frame, text="ts4.topping.dk", 
                              font=("Arial", 9), bg="#f5f5f5", fg="#3caad6", 
                              cursor="hand2")
        footer_link.pack(side="left")
        
        # Make link clickable
        footer_link.bind("<Button-1>", lambda e: self.open_website())
        footer_link.bind("<Enter>", lambda e: footer_link.config(font=("Arial", 9, "underline")))
        footer_link.bind("<Leave>", lambda e: footer_link.config(font=("Arial", 9)))
        
    def check_folders(self):
        """Check if source folders exist"""
        missing = []
        for folder in self.folders_to_backup:
            if not os.path.exists(folder):
                missing.append(os.path.basename(folder))
        
        if missing:
            self.status_label.config(
                text=f"⚠️ Advarsel: Nogle mapper blev ikke fundet: {', '.join(missing)}", 
                fg="orange"
            )
            
    def start_backup(self):
        # Disable button during backup
        self.backup_btn_canvas.unbind("<Button-1>")
        self.backup_btn_canvas.config(cursor="")
        self.backup_btn_canvas.itemconfig(self.button_bg, fill="#999999")
        
        # Run backup in a separate thread
        thread = threading.Thread(target=self.perform_backup)
        thread.daemon = True
        thread.start()
        
    def perform_backup(self):
        try:
            self.status_label.config(text="Starter backup...", fg="orange")
            self.root.update()
            
            # Create backup folder with timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            backup_folder = os.path.join(self.backup_destination, f"Backup_{timestamp}")
            
            # Create destination folder if it doesn't exist
            os.makedirs(backup_folder, exist_ok=True)
            
            total_folders = len(self.folders_to_backup)
            self.progress['maximum'] = total_folders
            
            for i, folder in enumerate(self.folders_to_backup, 1):
                if os.path.exists(folder):
                    folder_name = os.path.basename(folder)
                    dest_path = os.path.join(backup_folder, folder_name)
                    
                    self.status_label.config(text=f"Kopierer: {folder_name}")
                    self.progress_text.config(text=f"Mappe {i} af {total_folders}")
                    self.progress['value'] = i - 0.5
                    self.root.update()
                    
                    # Copy the entire folder
                    shutil.copytree(folder, dest_path)
                    
                    self.progress['value'] = i
                    self.root.update()
                else:
                    self.progress_text.config(
                        text=f"Springt over: {os.path.basename(folder)} (ikke fundet)"
                    )
            
            self.status_label.config(text="✅ Backup fuldført!", fg="green")
            self.progress_text.config(text=f"Gemt i: Backup_{timestamp}")
            self.backup_btn_canvas.bind("<Button-1>", lambda e: self.start_backup())
            self.backup_btn_canvas.config(cursor="hand2")
            self.backup_btn_canvas.itemconfig(self.button_bg, fill="#3caad6")
            
            messagebox.showinfo("Succes", 
                              f"Backup er fuldført!\n\n"
                              f"Placering:\n{backup_folder}\n\n"
                              f"Tid: {datetime.now().strftime('%H:%M:%S')}")
            
        except Exception as e:
            self.status_label.config(text="❌ Backup fejlede!", fg="red")
            self.progress_text.config(text=str(e))
            self.backup_btn_canvas.bind("<Button-1>", lambda e: self.start_backup())
            self.backup_btn_canvas.config(cursor="hand2")
            self.backup_btn_canvas.itemconfig(self.button_bg, fill="#3caad6")
            messagebox.showerror("Fejl", f"Backup fejlede:\n\n{str(e)}")
    
    def open_website(self):
        """Open the website in default browser"""
        webbrowser.open("https://ts4.topping.dk")
    
    def load_config(self):
        """Load backup destination from Windows Registry"""
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.registry_key, 0, winreg.KEY_READ)
            value, _ = winreg.QueryValueEx(key, "BackupDestination")
            winreg.CloseKey(key)
            return value
        except:
            return ''
    
    def save_config(self):
        """Save backup destination to Windows Registry"""
        try:
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, self.registry_key)
            winreg.SetValueEx(key, "BackupDestination", 0, winreg.REG_SZ, self.backup_destination)
            winreg.CloseKey(key)
        except Exception as e:
            print(f"Could not save config: {e}")
    
    def change_destination(self):
        """Allow user to change backup destination"""
        new_destination = filedialog.askdirectory(
            title="Vælg hvor backup skal gemmes",
            initialdir=self.backup_destination if os.path.exists(self.backup_destination) else os.path.expanduser("~")
        )
        
        if new_destination:
            self.backup_destination = new_destination
            self.dest_label.config(text=self.backup_destination)
            self.save_config()
            messagebox.showinfo("Placering ændret", 
                              f"Backup placering er nu:\n{self.backup_destination}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Sims4BackupApp(root)
    root.mainloop()

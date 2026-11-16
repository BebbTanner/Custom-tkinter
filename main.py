import customtkinter as ctk

root = ctk.CTk()
root.geometry("300x200")

# Adjust corner_radius (higher number = more rounded)
btn = ctk.CTkButton(
    master=root, 
    text="Modern Button", 
    corner_radius=32,    # Controls the roundness
    fg_color="#2b8a3e",  # Button color
    hover_color="#237032" # Color when hovered
)
btn.pack(pady=50)

root.mainloop()
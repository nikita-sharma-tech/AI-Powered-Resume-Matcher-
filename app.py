import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
from resume_match_backend import read_resume, read_job_description, calculate_percent_match

class ResumeMatcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resume JD Matcher ")
        self.root.geometry("820x720")
        self.resume_file = None
        self.jd_file = None

        ttk.Label(root, text="Resume Matcher", font=("Helvetica", 26, 'bold')).pack(pady=20)

        ttk.Button(root, text=" Upload Resume (PDF)", bootstyle=PRIMARY, command=self.upload_resume).pack(pady=10)
        ttk.Button(root, text=" Upload Job Description (TXT)", bootstyle=INFO, command=self.upload_jd).pack(pady=10)
        ttk.Button(root, text=" Check Match", bootstyle=SUCCESS, command=self.check_match).pack(pady=15)

        # Score Box
        self.score_box = ttk.Label(root, text="", font=("Helvetica", 20, 'bold'),
                                   bootstyle=INFO, width=30, anchor='center')
        self.score_box.pack(pady=10)

        # Matched Frame
        self.matched_frame = ttk.LabelFrame(root, text=" Matched Terms", bootstyle=SUCCESS)
        self.matched_frame.pack(pady=10, fill='both', expand=True, padx=20)
        self.matched_text = ttk.Text(self.matched_frame, height=6, font=("Segoe UI", 11), wrap='word')
        self.matched_text.pack(padx=10, pady=5, fill='both', expand=True)

        # Unmatched Frame
        self.unmatched_frame = ttk.LabelFrame(root, text=" Unmatched JD Terms", bootstyle=DANGER)
        self.unmatched_frame.pack(pady=10, fill='both', expand=True, padx=20)
        self.unmatched_text = ttk.Text(self.unmatched_frame, height=4, font=("Segoe UI", 11), wrap='word')
        self.unmatched_text.pack(padx=10, pady=5, fill='both', expand=True)

    def upload_resume(self):
        self.resume_file = filedialog.askopenfile(filetypes=[("PDF files", "*.pdf")])
        if self.resume_file:
            messagebox.showinfo("Success", "Resume uploaded successfully!")

    def upload_jd(self):
        self.jd_file = filedialog.askopenfile(filetypes=[("Text files", "*.txt")])
        if self.jd_file:
            messagebox.showinfo("Success", "Job Description uploaded successfully!")

    def check_match(self):
        if not self.resume_file or not self.jd_file:
            messagebox.showerror("Error", "Please upload both resume and job description.")
            return

        try:
            resume_text = read_resume(self.resume_file.name, isJDFile='N')
            jd_text, stemmed_dict = read_job_description(self.jd_file.name, isJDFile='Y')
            percent, matched, unmatched = calculate_percent_match(resume_text, jd_text, stemmed_dict)

            # Display score in boxed label
            self.score_box.config(text=f" Match Score: {percent}%", bootstyle=INFO if percent >= 60 else WARNING)

            # Clear old content
            self.matched_text.delete('1.0', 'end')
            self.unmatched_text.delete('1.0', 'end')

            # Insert matched terms
            self.matched_text.insert('end', ', '.join(matched))

            # Insert unmatched terms
            self.unmatched_text.insert('end', ', '.join(unmatched))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")  # Try: 'flatly', 'morph', 'vapor', 'superhero'
    app = ResumeMatcherApp(root)
    root.mainloop()

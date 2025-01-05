import subprocess
import sys
from fpdf import FPDF
def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("All required packages have been installed.")
    except Exception as e:
        print(f"An error occurred while installing requirements: {e}")
install_requirements()
def get_response_from_ollama(prompt, model=input("Please Enter Exact Model Name: ")):
    try:
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print("Error:", result.stderr)
            return None
    except FileNotFoundError:
        print("Ollama program not found. Make sure the CLI is installed correctly.")
        return None
def save_response_to_pdf(response, filename=input("Please Specify File Name:") + ".pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', size=12)
    pdf.multi_cell(0, 10, response)
    pdf.output(filename)
    print(f"PDF saved successfully: {filename}")
prompt = input("Please enter the prompt you want to send to your Model: ")
response = get_response_from_ollama(prompt)

if response:
    save_response_to_pdf(response)

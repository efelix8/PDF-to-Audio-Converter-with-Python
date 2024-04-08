import pyttsx3
import PyPDF2

def get_page_number():
    """Get the page number from the user."""
    while True:
        try:
            val = input("Enter the page number from where you want to start: ")
            val_converted = int(val) - 1
            return val_converted
        except ValueError:
            print("Invalid input. Please enter an integer value.")

def read_pdf(pdf_file, start_page):
    """Read a PDF file and extract text from the specified page."""
    with open(pdf_file, 'rb') as book:
        pdf_reader = PyPDF2.PdfFileReader(book)
        page = pdf_reader.getPage(start_page)
        text = page.extractText()
    return text

def speak_text(text):
    """Speak the given text using the pyttsx3 library."""
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()

if __name__ == "__main__":
    # Get the page number from the user
    start_page = get_page_number()

    # Read the PDF file
    pdf_file = 'python_basics.pdf'
    text = read_pdf(pdf_file, start_page)

    # Speak the text
    speak_text(text)
    

# PDF-to-Audio-Converter-with-Python

This code is a Python program that reads a PDF file from a specific page (entered by the user) and voices its text using the pyttsx3 library.

How the code works

get_page_number(num_pages) function:

Prompts the user for the page number to start reading.
It uses a loop to provide a valid integer input.
Returns the page number minus 1.
read_pdf(pdf_file, start_page) function:

Opens the PDF file and creates a PdfReader object.
Gets the total number of pages and checks the validity of the start page.
Extracts and returns the text from the specified page.
speak_text(text) function:

Speaks the text using pyttsx3.
main block:

Gets the PDF file name and start page from the user.
Reads the text using the read_pdf() function.
Speaks the text using the speak_text() function.
Improving the code:

Add error handling.
Add user-friendly messages.
Support different PDF file names.
Use libraries like PyMuPDF for wider PDF version compatibility.
Make the code structure more modular.

# Importing Libraries
from gtts import gTTS
from PyPDF2 import PdfReader

# Open the PDF file
pdf_file_path = 'specify_the_file_path.pdf'
pdf_file = open(pdf_file_path, 'rb')

# Create PDF Reader Object
pdf_reader = PdfReader(pdf_file)
page_count = len(pdf_reader.pages)  # Count number of pages
text_list = []

# Extracting text data from each page of the PDF file
for i in range(page_count):
    try:
        page = pdf_reader.pages[i]
        text_list.append(page.extract_text())
    except Exception as e:
        print(f"Error on page {i}: {e}")

# Converting multiline text to a single line text
text_string = " ".join(text_list)

# Print extracted text for verification
print(text_string)

# Set language to English
language = 'en'

# Call Google Text-to-Speech (gTTS)
my_audio = gTTS(text=text_string, lang=language, slow=False)

# Save as an MP3 file
my_audio.save("Audio.mp3")

print("Audio file 'Audio.mp3' has been created successfully!")

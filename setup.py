import nltk
import os

def download_nltk_data():
    """Download required NLTK data."""
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)
        nltk.download('maxent_ne_chunker', quiet=True)
        nltk.download('words', quiet=True)
        print("NLTK data downloaded successfully")
    except Exception as e:
        print(f"Error downloading NLTK data: {e}")

def create_required_directories():
    """Create required directories if they don't exist."""
    directories = [
        '.streamlit',
        'TranscriptIQ/pages',
        'TranscriptIQ/myfunctions'
    ]
    
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"Created directory: {directory}")
        except Exception as e:
            print(f"Error creating directory {directory}: {e}")

if __name__ == "__main__":
    print("Running setup...")
    download_nltk_data()
    create_required_directories()
    print("Setup completed successfully") 
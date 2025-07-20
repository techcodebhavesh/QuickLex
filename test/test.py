import os
import sys
import dotenv

# Add parent directory to path to import local gptpdf module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

dotenv.load_dotenv()
api_key = os.getenv('api_key')
base_url = os.getenv('base_url')

pdf_path = 'D:/QuickLex/examples/rh/2_MSCI_Hedged_Methodology_20241111.pdf'
output_dir = 'D:/QuickLex/examples/rh/'


# import shutil
# shutil.rmtree(output_dir, ignore_errors=True)

def test_parse_pdf():
    from quicklex import parse_pdf
    content, image_paths = parse_pdf(
        pdf_path, 
        output_dir=output_dir, 
        api_key=api_key, 
        base_url=base_url, 
        model='meta-llama/llama-4-scout-17b-16e-instruct', 
        gpt_worker=6
        )
    print(content)
    print(image_paths)


if __name__ == '__main__':
    test_parse_pdf()
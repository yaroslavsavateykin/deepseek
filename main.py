from openai import OpenAI
import pypandoc
from pypdf import PdfReader
import os


from dotenv import load_dotenv

load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")


class TaskParser:
    @staticmethod
    def parse_to_md(input_file: str, output_folder: str) -> None:
        output_md = input_file.strip(".pdf") + ".md"

        if input_file.endswith(".pdf"):
            reader = PdfReader(input_file)
            output = "\n".join(x.extract_text(0) for x in reader.pages)

        else:
            output = pypandoc.convert_file(
                input_file,
                "gfm",
                outputfile=f"{output_folder}/{output_md}",
                extra_args=[f"--extract-media=./{output_folder}/images"],
            )

        print(output)


if __name__ == "__main__":
    print(os.walk("source/"))
    for dirpath, dirnames, filenames in os.walk("source/"):
        print(filenames)
        for filename in filenames:
            TaskParser.parse_to_md(f"source/{filename}", "")

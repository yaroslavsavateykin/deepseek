from openai import OpenAI
import pypandoc
import os

from dotenv import load_dotenv

load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")


class TaskParser:
    @staticmethod
    def parse_to_md(input_file: str, output_folder: str) -> None:
        output_md = input_file.strip(".pdf") + ".md"

        if not input_file.endswith(".pdf"):
            output = pypandoc.convert_file(
                input_file,
                "gfm",
                outputfile=output_md,
                extra_args=[f"--extract-media=./{output_folder}/images"],
            )
        else:

            

        print(output)


if __name__ == "__main__":
    TaskParser.parse_to_md("source/task-chem-11-Kalin-mun-08-9.pdf", "")

import os
import subprocess


def convert_word_to_pdf(soffice_path, word_file_path, output_dir):
    conv_cmd = f"{soffice_path} --headless --norestore --invisible --nodefault --nofirststartwizard --nolockcheck --nologo --convert-to pdf:writer_pdf_Export --outdir {output_dir} {word_file_path}"
    response = subprocess.run(
        conv_cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    files = os.listdir("tmp")
    print("After conversion:: Files in /tmp directory:", files)
    if response.returncode != 0:
        response = subprocess.run(
            conv_cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if response.returncode != 0:
            return False
    return True

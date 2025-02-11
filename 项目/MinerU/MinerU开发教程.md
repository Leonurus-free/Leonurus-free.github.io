## 版本
0.10.6
----

## python调用
~~~
import os  
  
from magic_pdf.data.data_reader_writer import FileBasedDataWriter, FileBasedDataReader  
from magic_pdf.data.dataset import PymuDocDataset  
from magic_pdf.model.doc_analyze_by_custom_model import doc_analyze  
from magic_pdf.config.enums import SupportedPdfParseMethod  
  
# args  
pdf_file_name = "demo/demo1.pdf"  # replace with the real pdf path  
name_without_suff = pdf_file_name.split(".")[0]  
  
# prepare env  
local_image_dir, local_md_dir = "output/images", "output"  
image_dir = str(os.path.basename(local_image_dir))  
  
os.makedirs(local_image_dir, exist_ok=True)  
  
image_writer, md_writer = FileBasedDataWriter(local_image_dir), FileBasedDataWriter(  
    local_md_dir  
)  
image_dir = str(os.path.basename(local_image_dir))  
  
# read bytes  
reader1 = FileBasedDataReader("")  
pdf_bytes = reader1.read(pdf_file_name)  # read the pdf content  
  
# proc  
## Create Dataset Instance  
ds = PymuDocDataset(pdf_bytes)  
  
## inference  
if ds.classify() == SupportedPdfParseMethod.OCR:  
    infer_result = ds.apply(doc_analyze, ocr=True)  
  
    ## pipeline  
    pipe_result = infer_result.pipe_ocr_mode(image_writer)  
  
else:  
    infer_result = ds.apply(doc_analyze, ocr=False)  
  
    ## pipeline  
    pipe_result = infer_result.pipe_txt_mode(image_writer)  
  
### draw model result on each page  
infer_result.draw_model(os.path.join(local_md_dir, f"{name_without_suff}_model.pdf"))  
  
### draw layout result on each page  
pipe_result.draw_layout(os.path.join(local_md_dir, f"{name_without_suff}_layout.pdf"))  
  
### draw spans result on each page  
pipe_result.draw_span(os.path.join(local_md_dir, f"{name_without_suff}_spans.pdf"))  
  
### dump markdown  
pipe_result.dump_md(md_writer, f"{name_without_suff}.md", image_dir)  
  
### dump content list  
pipe_result.dump_content_list(md_writer, f"{name_without_suff}_content_list.json", image_dir)
~~~

## 需要改动
* 更改magic_pdf/libs/config_reader.py
	~~~
	current_directory = os.getcwd()  
	print("当前工作目录:", current_directory)

	home_dir = current_directory
	将原来读取magic-pdf.json文件的路径从/root/magic-pdf.json更改为/home/MinerU/magic-pdf.json
	~~~
* 
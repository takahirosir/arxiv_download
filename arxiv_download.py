import arxiv
import os

search = arxiv.Search(
  query = "LLM AND medical",
  max_results = 150,
  sort_by = arxiv.SortCriterion.SubmittedDate,
  sort_order = arxiv.SortOrder.Descending
)

newpath = r'./download' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

for result in search.results():
    result.download_pdf(dirpath="./download")

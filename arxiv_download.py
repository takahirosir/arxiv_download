import arxiv

search = arxiv.Search(
  query = "LLM AND medical",
  max_results = 5,
  sort_by = arxiv.SortCriterion.SubmittedDate,
  sort_order = arxiv.SortOrder.Descending
)

for result in search.results():
    result.download_pdf()

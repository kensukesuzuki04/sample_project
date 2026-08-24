# note/

Project documentation that is not code: data descriptions, method notes,
literature summaries, meeting notes.

Suggested files:

| File | Contents |
|---|---|
| `readme_<dataset>.md` | Where a dataset came from, its variables, its quirks |
| `LITREVIEW.md` | Running summary of papers read |
| `data_registry.md` | Which raw file feeds which script and output |

Rules:

- Markdown (`.md`) only. Keep it in Git so it is versioned with the code.
- No data files here — those go in the Dropbox-backed `data/` junction.
- Update a note in the same commit as the code change it describes.

# Development

## Project layout

```text
flet-review/
├── pyproject.toml                 # package metadata, setuptools build
├── zensical.toml                  # this documentation site
├── docs/                          # documentation pages
└── src/
    ├── flet_review/
    │   ├── __init__.py            # exports InAppReview
    │   └── flet_review.py         # Python service
    └── flutter/flet_review/
        ├── pubspec.yaml           # Dart package
        └── lib/
            ├── flet_review.dart   # exports Extension
            └── src/
                ├── extension.dart     # creates the service
                └── flet_review.dart   # InAppReviewService
```

setuptools bundles everything under `src/flutter/flet_review` as package
data, so the Flutter code travels with the wheel.

## Testing changes

`flet run` doesn't include native extensions, so test on a real device:

```bash
flet debug android -d <device-id>
flet debug ios -d <device-id>
```

## Building the package

```bash
python -m build
```

## Documentation

The docs are built with [Zensical](https://zensical.org). The API reference
is generated from the docstrings via mkdocstrings.

```bash
pip install --group dev        # or: uv sync --group dev
zensical serve                 # live preview at http://localhost:8000
zensical build                 # static site in ./site
```

## Releasing

Releases are automated with GitHub Actions:

| Workflow | Trigger | What it does |
|---|---|---|
| `docs.yml` | Push to `main` touching docs, source or `zensical.toml` | Builds the site and deploys it to GitHub Pages |
| `release.yml` | Push of a `v*` tag | Checks versions, builds the package, publishes it to PyPI, creates a GitHub release |

To publish a new version:

1. Bump `version` in **both** `pyproject.toml` and
   `src/flutter/flet_review/pubspec.yaml`.
2. Commit and push to `main`.
3. Tag and push:

    ```bash
    git tag v0.1.1
    git push origin v0.1.1
    ```

!!! warning "Versions must match"
    The release fails if the tag, `pyproject.toml` and `pubspec.yaml` disagree.

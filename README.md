- Development
  - conda env create -f environment.yml
  - build: sphinx-build docs _build

- Useful links
  - https://sphinx-design.readthedocs.io/en/sbt-theme/dropdowns.html


name: Docs
on: [push, pull_request, workflow_dispatch]
permissions:
    contents: write
jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v3
      - name: Install dependencies
        run: |
          pip install sphinx sphinx_rtd_theme sphinx-book-theme sphinx-tabs sphinx-togglebutton
      - name: Sphinx build
        run: |
          sphinx-build doc _build
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        if: ${{ github.event_name == 'push' && github.ref == 'refs/heads/main' }}
        with:
          publish_branch: gh-pages
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: _build/
          force_orphan: true
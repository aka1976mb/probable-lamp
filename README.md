# nocodb-to-gpt-via-api

## Development Instructions

> [!TIP]
> This project utilizes [`uv`](https://docs.astral.sh/uv/) for module management.
> You can find installation instructions via [relevant operating system](https://docs.astral.sh/uv/getting-started/installation/) documentation.

- Clone: `gh repo clone aksbdc/nocodb-to-gpt-via-api`
- Source: `cd repo "
- Build: [`make`](https://www.gnu.org/software/make/)

### Environment Variables

If you encounter issues with `python-dotenv` not loading the `.env` file, you can set the environment variables directly in your shell before running the script.

For PowerShell:
```powershell
$env:API_KEY='YOUR_API_KEY'; $env:TABLE_NAME='YOUR_TABLE_NAME'; $env:DEFAULT_VIEW='YOUR_DEFAULT_VIEW'; uv run main.py
```

### Branch Management

- `main` → production ready environment.
- `staging` → released changes to be merged into `main`.
- `dev` → testing changes to be merged into `staging`.

## [Architecture Diagram](https://github.com/aksbdc/nocodb-to-gpt-via-api/wiki)

## Scenario Planning

1. [Small Business Owner](https://aksbdc.org/success-stories/)
1. [Expert Advisor](https://aksbdc.org/about/advisors/)
1. [General Public](https://alaska.gov/)

### [System Benchmarking](https://github.com/aksbdc/nocodb-to-gpt-via-api/wiki)

### [Experimental Design](Makefile)

### [Research Question](docs/NOTES.md)

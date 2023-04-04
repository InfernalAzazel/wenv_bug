import json
from typing import Any, Optional
import numpy as np
import openpyxl
import pandas as pd
import typer
from openpyxl.styles import Border, Side, Font, Alignment
from openpyxl.workbook import Workbook
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.worksheet import Worksheet
from pandas import DataFrame
from rich import print
from rich.progress import Progress, SpinnerColumn, TextColumn

__version__ = 'V1.0, 20230320'


def version_callback(value: bool):
    if value:
        print(f"wenv_bug CLI Version: {__version__}")
        raise typer.Exit()


def main(
        spdx_file: str = typer.Argument(...,
                                        help='The spdx json format file that needs to be processed e.g: data.json'),
        components_file: str = typer.Argument(...,
                                              help='The components csv format file that needs to be processed e.g: data.components.csv'),
        vulnerabilities_file: str = typer.Argument(...,
                                                   help='The vulnerabilities csv format file that needs to be processed e.g: data.vulnerabilities.csv'),
        template_file: str = typer.Argument('template.xlsx',
                                            help='The template xlsx format file name e.g: template.xlsx'),
        _: Optional[bool] = typer.Option(
            None, "--version", callback=version_callback
        ),
        __: Optional[bool] = typer.Option(
            None, "-v", callback=version_callback
        ),

):
    progress = Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True, )
    progress.start()
    progress.add_task(description="handle...", total=None)
    progress.add_task(description="generate xlsx file...", total=None)
    progress.stop()


if __name__ == "__main__":
    typer.run(main)

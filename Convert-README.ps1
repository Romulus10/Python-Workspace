Get-ChildItem -Recurse -Filter doc\ | ForEach-Object { 
python -m markdown .\README.md > docs.html
}
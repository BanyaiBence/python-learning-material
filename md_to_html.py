import markdown

with open('./lesson-2/jegyzet.md', 'r') as f:
    markdown_content = f.read()

html_content = markdown.markdown(markdown_content)

with open('./lesson-2/jegyzet.html', 'w') as f:
    f.write(html_content)
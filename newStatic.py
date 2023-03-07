"""
newStatic - convert markdown documents to html using jinja2 templates

for each content_file
    load metadata and markdown content
    render layout template, replace {{ content }} with rendered markdown
    write html output to render_path
"""

import pprint
import markdown, toml
import pathlib, glob
from jinja2 import Environment, FileSystemLoader

DEFAULTS = {}

class SetDefaults:
    def __init__(self) -> None:
        DEFAULTS['source'] = pathlib.Path.cwd()
        DEFAULTS['destination'] = pathlib.Path.cwd()
        DEFAULTS['title'] = "newStatic"
        DEFAULTS['tagline'] = "a python static site generator"

class CommandArguments:
    pass

class ConfigFileLoader:
    pass

class SiteConfig:
    pass

class PageMetadata:
    pass

class TemplateLoader:
    def __init__(self) -> None:
        pass

class HTMLOutput:
    pass

class newStatic:
    def __init__(self) -> None:
        SiteDefaults = SetDefaults()
        pprint.pp(DEFAULTS)
    
    def testrender(self):
        md_parser = markdown.Markdown(extensions=['meta','fenced_code'])
        template_environment = Environment(loader=FileSystemLoader("layouts/"))

        files = (p.resolve() for p in pathlib.Path(".").glob("**/*") if p.suffix in {".md", ".markdown", ".cmark"})
        for content_file in files:
            print(content_file)
            with open(content_file, 'r') as markdown_file:
                content = markdown_file.read()
        
            html_output = md_parser.convert(content)
            template = template_environment.get_template("default.jinja2")

            output_file = pathlib.PurePath(content_file).stem + '.html'
            with open(output_file, 'w') as output_file:
                output_file.write(template.render({'content': html_output, 'site_title': "homepage", 'page_title': md_parser.Meta['title'][0] }))

if __name__ == "__main__":
    newStatic()

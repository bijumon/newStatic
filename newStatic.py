"""
newStatic - convert markdown documents to html using jinja2 templates

for each content_file
    load metadata and markdown content
    render layout template, replace {{ content }} with rendered markdown
    write html output to render_path

# loading the config file
load if config_file exists in
 - source dir
 - path in cmdline arg
else load builtin default

merge siteconfig from defaults
merge siteconfig from cmdline
"""

import argparse, pprint
import markdown, toml
import pathlib, glob
from jinja2 import Environment, FileSystemLoader

DEFAULTS = {}
DEFAULTS['source'] = pathlib.Path.cwd()
DEFAULTS['destination'] = pathlib.Path.cwd()
DEFAULTS['config'] = '_config.toml'
DEFAULTS['title'] = "newStatic"
DEFAULTS['tagline'] = "a python static site generator"

class CommandArguments:
    args = {}

    def __init__(self) -> None:
        cmdline = argparse.ArgumentParser(prog=DEFAULTS['title'], description=DEFAULTS['tagline'])
        cmdline.add_argument('--source', type=str)
        cmdline.add_argument('--destination', type=str)
        cmdline.add_argument('--config', type=str)
        self.args = vars(cmdline.parse_args())
            
    def config(self) -> None:
        cmdline = {k: v for k, v in self.args.items() if v is not None}
        return cmdline

class ConfigFileLoader:
    config_from_file = {}

    def load(self,config_file):
        with open(config_file, 'r') as SiteConfigFile:
           self.config_from_file = toml.loads(config_file.read())
        
    def config(self) -> str:
        pprint.pp(self.config_from_file)
        return self.config_from_file

class Site:
    siteconfig = {}

    def __init__(self) -> None:
        # load config and merge with defaults
        file_config = ConfigFileLoader()
        cmdline = CommandArguments()

        self.siteconfig |= DEFAULTS
        self.siteconfig |= file_config.config()
        self.siteconfig |= cmdline.config()

    def show_config(self) -> None:
        pprint.pp(self.siteconfig)
    
site = Site()
site.show_config()

class PageMetadata:
        pass

class TemplateLoader:
    def __init__(self) -> None:
        pass

class HTMLOutput:
    pass

class newStatic:
    def __init__(self) -> None:
        pass
    
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

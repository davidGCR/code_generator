import yaml
from jinja2 import Environment, FileSystemLoader
import os

ENVIRONMENT = Environment(
  loader = FileSystemLoader('./template'),
  trim_blocks=True, 
  lstrip_blocks=True
)
CONFIG_DATA = yaml.safe_load(open('./config.yaml'))

def generate_domain_filename(input_string):
    parts = input_string.split('_')
    capitalized_parts = [parts[0].capitalize()] + [part.capitalize() for part in parts[1:]]
    output_string = ''.join(capitalized_parts)
    return output_string

CONFIG_DATA['domainFilename'] = generate_domain_filename(CONFIG_DATA['filename'])

def render_template(template_filename):
  return ENVIRONMENT.get_template(template_filename).render(CONFIG_DATA)
  
def generate_python_file(filename, template_filename):
   directory = os.path.dirname(filename)
   if not os.path.exists(directory):
     os.makedirs(directory)
   with open(filename, 'w') as f:
    code_file = render_template(template_filename)
    f.write(code_file)

if __name__ == "__main__":
#   print(render_template(template_filename='rest/routers/router.py'))
  
  generate_python_file(
    filename=f"src/rest/routers/{CONFIG_DATA['filename']}.py",
    template_filename='routerTemplate.py'
    )
  generate_python_file(
    filename=f"src/use_cases/{CONFIG_DATA['filename']}.py",
    template_filename='useCaseTemplate.py'
    )
  generate_python_file(
    filename=f"src/repository/{CONFIG_DATA['filename']}.py",
    template_filename='repositoryTemplate.py'
    )
#   print(CONFIG_DATA)
  
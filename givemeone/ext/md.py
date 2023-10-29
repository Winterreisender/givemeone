from pathlib import Path
from faker import Faker
from faker.providers import lorem



def main(path :Path, args):
    fake = Faker(['en_US'])
    TEXT = f"""# {fake.address()}
## {fake.address()}
{fake.sentence()}
![](https://source.unsplash.com/random/200x150.jpg)
- {fake.name()}
- {fake.name()}
- {fake.name()}

## {fake.address()}
{fake.sentence()}
1. {fake.name()}
2. {fake.name()}
### {fake.name()}
![](https://example.com)
"""

    with open(path,'w') as f:
        f.write(TEXT)
    
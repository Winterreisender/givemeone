from pathlib import Path
from faker import Faker
from faker.providers import lorem

def main(path :Path, args):
    fake = Faker()
    fake.add_provider(lorem)
    text = fake.paragraph(nb_sentences=5)
    with open(path,'w') as f:
        f.write(text)
    
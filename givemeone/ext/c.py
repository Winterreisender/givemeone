from pathlib import Path

HELLOWORLD = """#include <stdio.h>
int main() {
    printf("Hello World \\n");
}
"""

def main(path :Path):
    with open(path,'w') as f:
        f.write(HELLOWORLD)
    
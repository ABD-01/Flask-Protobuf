import random
from tabulate import tabulate

def generateRandomTable():
    def generate_lorem_ipsum():
        lorem_ipsum = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit,',
                    'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut', 'labore', 'et', 'dolore', 'magna',
                    'aliqua.', 'Ut', 'enim', 'ad', 'minim', 'veniam,', 'quis', 'nostrud', 'exercitation', 'ullamco',
                    'laboris', 'nisi', 'ut', 'aliquip', 'ex', 'ea', 'commodo', 'consequat.', 'Duis', 'aute', 'irure',
                    'dolor', 'in', 'reprehenderit', 'in', 'voluptate', 'velit', 'esse', 'cillum', 'dolore', 'eu',
                    'fugiat', 'nulla', 'pariatur.', 'Excepteur', 'sint', 'occaecat', 'cupidatat', 'non', 'proident,',
                    'sunt', 'in', 'culpa', 'qui', 'officia', 'deserunt', 'mollit', 'anim', 'id', 'est', 'laborum']
        return " ".join(random.choices(lorem_ipsum, k=random.randint(3, 20)))



    def generate_random_data(types, weights, depth=0):
        
        def generate_content(type,weights, depth):
            if type == 'ENUM':
                return f'Enum-{random.randint(1, 5)}'
            elif type == 'STRING':
                return generate_lorem_ipsum()
            elif type == 'INT32':
                return random.randint(1, 1000)
            elif type == 'Message' and depth > 0:
                return generate_random_data(types, weights, depth+1)
            else:
                return ''

        num_rows = 10
        data = []
        headers = ['Field Index', "Name", "Type", "Content"]

        for i in range(num_rows-2):
            field_type = random.choices(types, weights=weights)[0]
            row = [
                i,
                f'Field{i}',
                field_type,
                generate_content(field_type, weights, 0)  # Specify depth, e.g., 2
            ]
            data.append(row)
        
        return data

    headers = ['Field Index', "Name", "Type", "Content"]
    # Example usage:

    types = ['ENUM', 'STRING', 'INT32']
    weights = [5, 75, 20]
    random_data = generate_random_data(types, weights)

    for i in range(3):
        row = [
            i+8,
            f"Field{i+8}",
        'Message',
            tabulate(generate_random_data(types, weights), headers=headers, tablefmt="unsafehtml")
        ]
        random_data.append(row)

    return tabulate(random_data, headers=headers, tablefmt="unsafehtml")

with open("random_table.js", "w") as f:
    f.write(f'''
function generateRandomTable() {{
    const randomIndex = Math.floor(Math.random() * 30);
    const tables = [
    ''')
    for i in range(30):
        a = generateRandomTable()
        a = a.replace('<table>', '<table class="table table-bordered">').strip()
        f.write(f'''
        `{a}`,
        ''')
    
    f.write(f'''
    ];
    return tables[randomIndex];
    }}
    ''')
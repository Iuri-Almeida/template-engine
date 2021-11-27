"""
    Project: My Template Engine

    Author: Iuri Lopes Almeida

    GitHub: https://github.com/Iuri-Almeida

    Goal: Create a Template Engine

    Reference: https://www.aosabook.org/en/500L/a-template-engine.html
"""
from template_engine import TemplateEngine


def render_template(template: str = 'index.html', context: dict = None) -> str:
    with open(template) as file:
        engine = TemplateEngine(file.read())
        html = engine.render(context or {})

    return html


def format_price(price: float) -> str:
    return f'{price:.2f}'


def main():
    print(render_template('pages/index.html', {
        'upper': str.upper,
        'format_price': format_price,
        'name': 'Iuri Lopes Almeida',
        'product_list': [
            {
                'name': 'Playstation',
                'price': 1000,
                'show': True
            },
            {
                'name': 'XBox',
                'price': 3000,
                'show': False
            }
        ]}
    ))


if __name__ == '__main__':
    main()

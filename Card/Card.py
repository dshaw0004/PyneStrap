import pynecone as pc

class Card():
    stylesheet_btn = {
        'bg': 'blue',
        'border_radius': 'sm',
        'padding': '0.5ch 1ch',
        'margin_top': '1ch',
    }

    def img_card_1(self, border_radius='sm', title_size='md', bg_color='#fafafa', outline=True, **kwargs):
        stylesheet_card1 = {
            'max-width': '16rem',
            'border_radius': border_radius,
            'bg': bg_color,
            'outline': '1px solid grey' if outline else '0',

        }

        return pc.box(
            pc.center(
                pc.image(src="https://pynecone.io/black.png",
                         width="100%", height="auto"),
                width="100%", height="50%",
            ),
            pc.box(
                pc.heading('card heading', size=title_size),
                pc.text('card summary '),
                pc.center(

                    pc.link(
                        "link here",
                        href="https://github.com/dshaw0004",
                        color="white",
                        is_external=True,
                    ),
                    style=self.stylesheet_btn
                ),
                padding='1ch',
                border_top= '1px solid grey',
            ),
            style=stylesheet_card1
        )


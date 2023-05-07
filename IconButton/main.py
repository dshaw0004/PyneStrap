import pynecone as pc


# class IconButton():
def Right_Icon_BTN(text: str = 'Button', font_size: str = '1.5rem', bg_color: str = 'blue'):
    return pc.button(
        pc.text(text,
                font_size=font_size,
                margin_right="1ch"
                ),
        pc.icon(tag='search'),
        bg=bg_color
    )


def Left_Icon_BTN(text: str = 'Search', font_size: str = '1.5rem', bg_color: str = 'blue', icon_name='search'):
    return pc.button(
        pc.icon(tag=icon_name),
        pc.text(text,
                # font_size=font_size,
                margin_left="1ch",
                color="white",
                _hover={
                    'color': "#123456"
                }
                ),
        bg=bg_color,
        size='lg',
        _hover={
            'bg_color': "#1234ef"
        }
    )

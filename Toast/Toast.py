import pynecone as pc
import time
# from typing import Callable


def pass_func():
    return True

# on_open_func:Callable = pass_func, on_close_func:Callable = pass_func,
    # on_open = on_open_func,
    # on_close = on_close_func,

# class IconButton():
def toast1(toast_header: str = 'Toast Header', toast_body:str = 'Toast Body', trigger_component: pc.component = pc.button('open toast'), default_open:bool = False,) -> pc.component:
    print(time.time())
    return pc.popover(
    pc.popover_trigger(trigger_component),
    pc.popover_content(
        pc.popover_header(toast_header),
        pc.popover_body(toast_body),
        pc.popover_close_button(),
    ),
    auto_focus=True,
    is_lazy=True,
    close_on_blur=True,
    close_on_esc=True,
    default_is_open=default_open,
)
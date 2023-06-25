import pynecone as pc

def primary_button(text:str = 'primary', is_loading:bool=False, is_disabled:bool=False, **kwargs)->pc.Component:
    kwargs.setdefault('size', 'sm')
    kwargs.setdefault('is_full_width', False)
    kwargs.setdefault('loading_text', 'loading')
    return pc.button(text, 
                     is_loading=is_loading,
                     is_disabled=is_disabled,
                     size=kwargs['size'],
                     is_full_width=kwargs['is_full_width'],
                     loading_text=kwargs['loading_text'],
                     
                     color='white',
                     bg='#0d6efd',
                     _hover={
                         'bg': '#0b5ed7'
                     },
                     )

def secondary_button(text:str = 'secondary', is_loading:bool=False, is_disabled:bool=False, **kwargs)->pc.Component:
    kwargs.setdefault('size', 'sm')
    kwargs.setdefault('is_full_width', False)
    kwargs.setdefault('loading_text', 'loading')
    return pc.button(text, 
                     is_loading=is_loading,
                     is_disabled=is_disabled,
                     size=kwargs['size'],
                     is_full_width=kwargs['is_full_width'],
                     loading_text=kwargs['loading_text'],
                     color='white',
                     bg='#6c757d',
                     _hover={
                         'bg': '#5c636a'
                     }
                     )

def success_button(text:str = 'success', is_loading:bool=False, is_disabled:bool=False, **kwargs)->pc.Component:
    kwargs.setdefault('size', 'sm')
    kwargs.setdefault('is_full_width', False)
    kwargs.setdefault('loading_text', 'loading')
    return pc.button(text, 
                     is_loading=is_loading,
                     is_disabled=is_disabled,
                     size=kwargs['size'],
                     is_full_width=kwargs['is_full_width'],
                     loading_text=kwargs['loading_text'],
                     color='white',
                     bg='#198754',
                     _hover={
                         'bg': '#157347'
                     }
                     )

def danger_button(text:str = 'danger', is_loading:bool=False, is_disabled:bool=False,**kwargs)->pc.Component:
    kwargs.setdefault('size', 'sm')
    kwargs.setdefault('is_full_width', False)
    kwargs.setdefault('loading_text', 'loading')
    return pc.button(text, 
                     is_loading=is_loading,
                     is_disabled=is_disabled,
                     size=kwargs['size'],
                     is_full_width=kwargs['is_full_width'],
                     loading_text=kwargs['loading_text'],
                     color='white',
                     bg='#dc3545',
                     _hover={
                         'bg': '#bb2d3b'
                     }
                     )

def warning_button(text:str = 'warning', is_loading:bool=False, is_disabled:bool=False,**kwargs)->pc.Component:
    kwargs.setdefault('size', 'sm')
    kwargs.setdefault('is_full_width', False)
    kwargs.setdefault('loading_text', 'loading')
    return pc.button(text, 
                     is_loading=is_loading,
                     is_disabled=is_disabled,
                     size=kwargs['size'],
                     is_full_width=kwargs['is_full_width'],
                     loading_text=kwargs['loading_text'],
                     color='black',
                     bg='#ffc107',
                     _hover={
                         'bg': '#ffca2c'
                     }
                     )

def info_button(text:str = 'info', is_loading:bool=False, is_disabled:bool=False,**kwargs)->pc.Component:
    kwargs.setdefault('size', 'sm')
    kwargs.setdefault('is_full_width', False)
    kwargs.setdefault('loading_text', 'loading')
    return pc.button(text, 
                     is_loading=is_loading,
                     is_disabled=is_disabled,
                     size=kwargs['size'],
                     is_full_width=kwargs['is_full_width'],
                     loading_text=kwargs['loading_text'],
                     bg='#0dcaf0',
                     color='black',
                     _hover={
                         'bg': '#31d2f2'
                     }
                     )

def dark_button(text:str = 'dark', is_loading:bool=False, is_disabled:bool=False, **kwargs)->pc.Component:
    kwargs.setdefault('size', 'sm')
    kwargs.setdefault('is_full_width', False)
    kwargs.setdefault('loading_text', 'loading')
    return pc.button(text, 
                     is_loading=is_loading,
                     is_disabled=is_disabled,
                     size=kwargs['size'],
                     is_full_width=kwargs['is_full_width'],
                     loading_text=kwargs['loading_text'],
                     color='white',
                     bg='#212529',
                     _hover={
                         'bg': '#1c1f23'
                     }
                     )

def light_button(text:str = 'light', is_loading:bool=False, is_disabled:bool=False, **kwargs)->pc.Component:
    kwargs.setdefault('size', 'sm')
    kwargs.setdefault('is_full_width', False)
    kwargs.setdefault('loading_text', 'loading')
    return pc.button(text, 
                     is_loading=is_loading,
                     is_disabled=is_disabled,
                     size=kwargs['size'],
                     is_full_width=kwargs['is_full_width'],
                     loading_text=kwargs['loading_text'],
                     color='black',
                     bg='#f8f9fa',
                     _hover={
                         'bg': '#f9fafb'
                     }
                     )
import pynecone as pc

def Navbar():
    return pc.flex(
            pc.hstack(
                pc.image(src=""),
                pc.heading("PyneStrap")
                ),
            pc.spacer(),
            pc.flex(
                pc.link("Home", href="/"),
                pc.link("About", href="/about"),
                pc.link("Contact", href="/contact"),
                justify="space-around"
                ),
            width="100%",
            justify="space-between",
            padding_x="5"
            )

from kivy.app import App
from kivy.uix.button import Button


def callback(instance):
    print "The button <%s> is being pressed" % instance.text


bt1 = Button(text="zhangjiawei")
bt1.bind(on_press=callback)


class zjw(App):
    def build(self):
        return bt1


if __name__ == "__main__":
    zjw().run()

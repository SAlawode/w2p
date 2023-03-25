import cmd

class MyCmd(cmd.Cmd):
    def do_hello(self, args):
        print("Hello,", args)

    def do_quit(self, args):
        return True

if __name__ == '__main__':
    MyCmd().cmdloop()

import sys
import modules


def get_class_instance(class_name):
    class_ = getattr(modules, class_name)
    return class_()


def main():
    module = get_class_instance('Hello')
    print(module.msg())

    module = get_class_instance('World')
    print(module.msg())

    return 0


if __name__ == '__main__':
    sys.exit(main())

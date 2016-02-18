import argparse

from bottle import run

from .app import app


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_serve = subparsers.add_parser('serve', help="Start server")
    parser_serve.set_defaults(func=serve)

    args = parser.parse_args()

    if getattr(args, 'func', None):
        args.func()
    else:
        parser.print_help()


def serve():
    run(app, host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()

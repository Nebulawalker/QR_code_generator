import qrcode
import argparse
import os


def argparser():
    argparser = argparse.ArgumentParser(
        description="Cкрипт для создания QR-кодов"
    )
    argparser.add_argument(
        'string_to_qr',
        help='Строка, которую нужно преобразовать в QR-code',
        )
    argparser.add_argument(
        '--folder',
        help='Каталог для сохранения QR-кода (по умолчанию QR_codes).',
        default='QR_codes',
    )
    return argparser.parse_args()


def create_qr_code(data, folder):
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, f'"{data}"-QR.png')
    img = qrcode.make(data)
    img.save(filepath)


def main():
    args = argparser()
    create_qr_code(args.string_to_qr, args.folder)


if __name__ == '__main__':
    main()

import hashlib

def blake2(message):
    # Khởi tạo đối tượng blake2b với kích thước digest là 64 bytes
    blake2_hash = hashlib.blake2b(digest_size=64)
    blake2_hash.update(message)
    return blake2_hash.digest()

def main():
    # Nhập chuỗi văn bản và mã hóa sang định dạng utf-8
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    hashed_text = blake2(text)

    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print("BLAKE2 Hash:", hashed_text.hex())

if __name__ == "__main__":
    main()

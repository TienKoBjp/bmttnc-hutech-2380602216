from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Hàm tạo cặp khóa client từ tham số DH
def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

# Hàm tính toán bí mật chung
def derive_shared_secret(private_key, server_public_key):
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    # 1. Load khóa công khai của server đã lưu ở file .pem
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())

    # 2. Lấy tham số DH từ khóa công khai của server để đảm bảo cả hai dùng chung tham số
    parameters = server_public_key.parameters()
    
    # 3. Tạo cặp khóa riêng cho client
    private_key, public_key = generate_client_key_pair(parameters)

    # 4. Tính toán bí mật chung (Shared Secret)
    shared_secret = derive_shared_secret(private_key, server_public_key)

    print("Shared Secret:", shared_secret.hex())

if __name__ == "__main__":
    main()
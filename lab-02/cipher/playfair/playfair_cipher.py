class PlayFairCipher:
    def __init__(self) -> None:
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I")  # Chuyển "J" thành "I" trong khóa
        key = key.upper()
        
        # Lọc bỏ các ký tự trùng lặp trong key nhưng giữ nguyên thứ tự xuất hiện
        seen = set()
        clean_key = []
        for letter in key:
            if letter not in seen and letter.isalpha():
                seen.add(letter)
                clean_key.append(letter)
                
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = [letter for letter in alphabet if letter not in seen]
        
        matrix = clean_key + remaining_letters
        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return 0, 0 # Giá trị mặc định nếu không tìm thấy

    def playfair_encrypt(self, plain_text, matrix):
        # Xóa bỏ dòng matrix = self.create_playfair_matrix(key_string) cũ đi
        
        plain_text = plain_text.replace("J", "I").upper()
        plain_text = "".join([c for c in plain_text if c.isalpha()])
        
        # Xử lý tạo cặp ký tự chèn X
        prepared_text = ""
        i = 0
        while i < len(plain_text):
            prepared_text += plain_text[i]
            if i + 1 < len(plain_text):
                if plain_text[i] == plain_text[i+1]:
                    prepared_text += "X"
                    i += 1
                else:
                    prepared_text += plain_text[i+1]
                    i += 2
            else:
                i += 1
                
        if len(prepared_text) % 2 != 0:
            prepared_text += "X"

        encrypted_text = ""
        for i in range(0, len(prepared_text), 2):
            pair = prepared_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        # Xóa bỏ dòng tạo matrix từ key_string cũ đi
        
        cipher_text = cipher_text.upper().replace("J", "I")
        cipher_text = "".join([c for c in cipher_text if c.isalpha()])
        
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
                
        return decrypted_text
import random
import tornado.ioloop
import tornado.web
import tornado.websocket

# Lớp xử lý kết nối WebSocket
class WebSocketServer(tornado.websocket.WebSocketHandler):
    clients = set()

    def open(self):
        WebSocketServer.clients.add(self)
        print("Client connected")

    def on_close(self):
        WebSocketServer.clients.remove(self)
        print("Client disconnected")

    @classmethod
    def send_message(cls, message):
        print(f"Sending message {message} to {len(cls.clients)} client(s).")
        for client in cls.clients:
            client.write_message(message)

# Lớp hỗ trợ chọn từ ngẫu nhiên
class RandomWordSelector:
    def __init__(self, word_list):
        self.word_list = word_list

    def sample(self):
        return random.choice(self.word_list)

def main():
    # Cấu hình ứng dụng Tornado
    app = tornado.web.Application([
        (r"/websocket/", WebSocketServer),
    ], 
    websocket_ping_interval=10, 
    websocket_ping_timeout=30)
    
    app.listen(8888)
    
    io_loop = tornado.ioloop.IOLoop.current()
    
    # Khởi tạo bộ chọn từ
    word_selector = RandomWordSelector(['apple', 'banana', 'orange', 'grape', 'melon'])
    
    # Thiết lập tác vụ gửi tin nhắn định kỳ mỗi 3000ms (3 giây)
    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda: WebSocketServer.send_message(word_selector.sample()), 3000
    )
    periodic_callback.start()
    
    print("Server started on port 8888...")
    io_loop.start()

if __name__ == "__main__":
    main()
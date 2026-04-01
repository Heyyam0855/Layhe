#!/usr/bin/env python3
"""
Sadə Python Web Server
Bu server HTTP istəklərini qəbul edib cavab verir
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """HTTP istəklərini idarə edən sinif"""
    
    def do_GET(self):
        """GET istəklərini emal edir"""
        # Fayl yollarını təmizləyir
        if self.path == '/':
            self.path = '/index.html'
        
        try:
            # Fayl uzantısını təyin edir
            if self.path.endswith('.html'):
                content_type = 'text/html; charset=utf-8'
            elif self.path.endswith('.css'):
                content_type = 'text/css'
            elif self.path.endswith('.js'):
                content_type = 'application/javascript'
            else:
                content_type = 'text/html; charset=utf-8'
            
            # Faylı oxuyur
            file_path = self.path.lstrip('/')
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                self.send_response(200)
                self.send_header('Content-type', content_type)
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            else:
                self.send_error_page()
                
        except Exception as e:
            print(f"Xəta: {e}")
            self.send_error_page()
    
    def send_error_page(self):
        """404 xəta səhifəsini göstərir"""
        self.send_response(404)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        error_html = """
        <!DOCTYPE html>
        <html lang="az">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>404 - Səhifə Tapılmadı</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 20px;
                }
                .container {
                    background: white;
                    padding: 40px;
                    border-radius: 20px;
                    text-align: center;
                    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                }
                h1 {
                    font-size: 5em;
                    color: #667eea;
                    margin: 0;
                }
                h2 {
                    color: #333;
                    margin: 20px 0;
                }
                p {
                    color: #666;
                    margin-bottom: 30px;
                }
                a {
                    display: inline-block;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 15px 40px;
                    border-radius: 25px;
                    text-decoration: none;
                    font-weight: bold;
                    transition: transform 0.3s ease;
                }
                a:hover {
                    transform: scale(1.1);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>404</h1>
                <h2>🔍 Səhifə Tapılmadı</h2>
                <p>Axtardığınız səhifə mövcud deyil və ya köçürülüb.</p>
                <a href="/">🏠 Ana səhifəyə qayıt</a>
            </div>
        </body>
        </html>
        """
        self.wfile.write(error_html.encode('utf-8'))
    
    def log_message(self, format, *args):
        """Log mesajlarını formatlaşdırır"""
        print(f"[İstək] {self.address_string()} - {format % args}")

def run_server(port=8000):
    """Web server-i işə salır"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print(f"╔═══════════════════════════════════════╗")
    print(f"║   Python Web Server İşə Salındı      ║")
    print(f"╚═══════════════════════════════════════╝")
    print(f"\n🌐 Server ünvanı: http://localhost:{port}")
    print(f"📡 Port: {port}")
    print(f"\n⚡ Server işləyir... (Dayandırmaq üçün Ctrl+C basın)\n")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n⛔ Server dayandırılır...")
        httpd.shutdown()
        print("✓ Server uğurla bağlandı!")

if __name__ == '__main__':
    run_server()


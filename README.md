# ETL Project - Real-time Data Pipeline

## Giới thiệu
Dự án này tập trung vào việc xây dựng một luồng xử lý dữ liệu (Extract - Transform - Load) hiện đại, cho phép đồng bộ hóa dữ liệu từ các hệ thống cơ sở dữ liệu quan hệ (RDBMS) sang các hệ thống NoSQL và In-memory storage theo thời gian thực.

Dự án ứng dụng cơ chế **Database Triggers** kết hợp với các công cụ xử lý dữ liệu lớn như **Apache Spark** và **Apache Kafka** để đảm bảo tính toàn vẹn và tốc độ của dữ liệu.

## Kiến trúc hệ thống
Dưới đây là sơ đồ mô tả luồng di chuyển của dữ liệu từ nguồn cấp đến các điểm lưu trữ cuối cùng:

![Kiến trúc hệ thống ETL](https://googleusercontent.com/image_generation_content/0)

*Lưu ý: Để ảnh hiển thị vĩnh viễn, bạn nên tải ảnh về, bỏ vào thư mục `images/` trong repo và thay link trên thành `images/ten_anh.png`.*

**Các thành phần chính:**
* **Source:** MySQL (Capture các thay đổi thông qua Trigger).
* **Message Broker:** Apache Kafka (Điều phối dữ liệu giữa các dịch vụ).
* **Processing Unit:** Apache Spark (Xử lý và biến đổi dữ liệu).
* **Sink/Storage:** MongoDB (Lưu trữ dạng tài liệu) và Redis (Bộ nhớ đệm tốc độ cao).

## 📁 Cấu trúc thư mục
Dựa trên kiến trúc hiện tại, repo được tổ chức như sau:
- `config/`: Chứa các thông số cấu hình kết nối database.
- `data/`: Lưu trữ dữ liệu thô hoặc các tệp tin trung gian.
- `databases/`: Các script định nghĩa schema và quản lý cơ sở dữ liệu.
- `sql/`: Tập hợp các lệnh SQL và định nghĩa Trigger cho database nguồn.
- `main.py`: Điểm khởi đầu của ứng dụng (Entry point).
- `requirement.txt`: Danh sách các thư viện Python cần thiết.

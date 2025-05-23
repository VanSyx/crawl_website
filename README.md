echo
# crawl_website
# 📰 VNExpress News Crawler – Crawl tin tức chuyên mục AI

### ✅ Thu thập tin tức từ chuyên mục "AI" trên trang VNExpress mỗi ngày lúc 6h sáng và lưu vào file CSV.

---

## 📁 Mục lục

- [🧰 Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
- [📦 Cài đặt thư viện](#-cài-đặt-thư-viện)
- [🚀 Cách chạy chương trình thủ công](#-cách-chạy-chương-trình-thủ-công)
- [📅 Thiết lập chạy tự động bằng Task Scheduler](#-thiết-lập-chạy-tự-động-bằng-task-scheduler)
- [📝 Mô tả dữ liệu](#-mô-tả-dữ-liệu)
- [📂 Cấu trúc project](#-cấu-trúc-project)
- [📌 Ghi chú mở rộng](#-ghi-chú-mở-rộng)

---

## Cấu trúc dự án
📦 VnExpressNewsCrawler
├── crawl_vnexpress.py          # File chính thực hiện crawl dữ liệu
├── requirements.txt            # Danh sách thư viện cần cài
├── run_crawl_vnexpress.bat     # File chạy tự động qua Task Scheduler
├── vnexpress_crawl.csv         # Kết quả được lưu tại đây
└── README.md                   # Hướng dẫn sử dụng (file này)

---

## 🧰 Yêu cầu hệ thống

- Python 3.7 trở lên
- Các thư viện cần thiết:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `schedule`

---

## 📦 Cài đặt thư viện

Chạy lệnh sau để cài đặt các thư viện:

```bash
pip install -r requirements.txt

## Cách chạy chương trình thủ công
Tại thư mục chứa file crawl_vnexpress.py, mở Terminal (CMD) và chạy:
    ------------------------- 
    python crawl_vnexpress.py
    -------------------------
Chương trình sẽ tự động:
    Duyệt toàn bộ các trang trong chuyên mục AI
    Lấy tiêu đề, mô tả, nội dung, hình ảnh
    Lưu dữ liệu vào file vnexpress_crawl.csv

📅 Thiết lập chạy tự động bằng Task Scheduler
Bước 1: Tạo file .bat
Mở Notepad, nhập nội dung sau (sửa đường dẫn nếu cần):
    ------------------------- 
    @echo off
    cd /d D:\RPA\Crawl_tin_tuc
    python crawl_vnexpress.py
    ------------------------- 
Lưu lại với tên run_crawl_vnexpress.bat

Bước 2: Đặt lịch chạy lúc 6h sáng mỗi ngày
    ------------------------- 
    Mở ứng dụng Task Scheduler từ Start Menu.
    Chọn Create Basic Task
    Đặt tên: Crawl VNExpress AI
    Chọn: Daily, thời gian là 06:00 AM
    Hành động: chọn Start a program
    Browse đến file run_crawl_vnexpress.bat
    Nhấn Finish
    ------------------------- 

✅ Sau khi hoàn thành, chương trình sẽ tự động chạy mỗi sáng lúc 6h và cập nhật file CSV mới.

📝 Mô tả dữ liệu
File CSV đầu ra là vnexpress_crawl.csv gồm 4 cột:

Cột	Mô tả nội dung
title	Tiêu đề bài viết
summary	Mô tả ngắn của bài viết
content	Nội dung chi tiết bài viết (dưới dạng HTML)
image	Link ảnh đầu tiên trong nội dung bài viết
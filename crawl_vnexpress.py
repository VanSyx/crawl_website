import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import schedule
def crawl_vnexpress():
    
    # Tạo danh sách để lưu dữ liệu
    data = []
    
    page = 1
    while True:
        # 1. Gửi HTTP request đến trang web
        if page == 1:
            response = requests.get("https://vnexpress.net/khoa-hoc-cong-nghe/ai")
        else:
            response = requests.get(f"https://vnexpress.net/khoa-hoc-cong-nghe/ai-p{page}")
        # 2. Kiểm tra nếu request thành công
        if response.status_code == 200:
            # 3. Sử dụng BeautifulSoup để phân tích HTML
            soup = BeautifulSoup(response.content, "html.parser")
        
            # 4. Tìm kiếm các bài báo có thẻ h3 và class="title-news
            news = soup.find_all('h2', class_='title-news')
            if not news:
                print("✅ Đã lấy hết bài viết.")
                break
        
            # Lấy link của tất cả các bài viết
            links = []
            for link in news:
                url = link.find('a').attrs["href"]
                links.append(url)
        
            # 5. Đối với mỗi bài báo, lấy tiêu đề, mô tả, hình ảnh, nội dung bài viết
            for link in links:
                i_news = requests.get(link)
                i_soup = BeautifulSoup(i_news.content, "html.parser")
            
                title = i_soup.find("h1", class_="title-detail").text
                try:
                    summary = i_soup.find("h2", class_="description").get_text(strip=True)
                except:
                    summary = ""
                body = i_soup.find("div", id="article-body")
            
                try:
                    content = body.decode_contents()
                except:
                    content = " "
            
                try:
                    image = body.find("img").attrs["src"]
                except:
                    image = " "
            
                item = [title, summary, content, image]
                data.append(item)           
        page += 1
        time.sleep(1)
        # 6. Lưu dữ liệu vào file CSV
        df = pd.DataFrame(data, columns=["title", "summary", "content", "image"])   
        df.to_csv(r"D:\RPA\Crawl_tin_tuc\vnexpress_crawl.csv", index=False, encoding='utf-8-sig') 
        print("Đã lưu dữ liệu vào file vnexpress_crawl.csv")
    schedule.every().day.at("06:00").do(crawl_vnexpress)
    print("Đã lên lịch chạy hàng ngày lúc 06:00 sáng")
    while True:
        schedule.run_pending()
        time.sleep(1)
        
        
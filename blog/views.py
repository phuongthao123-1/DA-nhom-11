from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.core.paginator import Paginator
from .models import Post, Category, Tag
from datetime import datetime, timedelta
import random

def get_dummy_categories():
    """Tạo các danh mục mẫu"""
    categories = [
        {'id': 1, 'name': 'Công nghệ', 'slug': 'cong-nghe', 'description': 'Bài viết về công nghệ và đổi mới'},
        {'id': 2, 'name': 'Kinh doanh', 'slug': 'kinh-doanh', 'description': 'Bài viết về kinh doanh và đầu tư'},
        {'id': 3, 'name': 'Không gian', 'slug': 'khong-gian', 'description': 'Bài viết về khám phá không gian'},
        {'id': 4, 'name': 'Năng lượng', 'slug': 'nang-luong', 'description': 'Bài viết về năng lượng sạch và tái tạo'},
        {'id': 5, 'name': 'AI', 'slug': 'ai', 'description': 'Bài viết về trí tuệ nhân tạo'},
    ]
    return [type('Category', (), cat) for cat in categories]

def get_dummy_tags():
    """Tạo các thẻ mẫu"""
    tags = [
        {'id': 1, 'name': 'SpaceX', 'slug': 'spacex'},
        {'id': 2, 'name': 'Tesla', 'slug': 'tesla'},
        {'id': 3, 'name': 'Neuralink', 'slug': 'neuralink'},
        {'id': 4, 'name': 'Twitter', 'slug': 'twitter'},
        {'id': 5, 'name': 'Starlink', 'slug': 'starlink'},
        {'id': 6, 'name': 'Xe điện', 'slug': 'xe-dien'},
        {'id': 7, 'name': 'Năng lượng mặt trời', 'slug': 'nang-luong-mat-troi'},
        {'id': 8, 'name': 'Tên lửa', 'slug': 'ten-lua'},
        {'id': 9, 'name': 'Sao Hỏa', 'slug': 'sao-hoa'},
        {'id': 10, 'name': 'Boring Company', 'slug': 'boring-company'},
    ]
    return [type('Tag', (), tag) for tag in tags]

def get_dummy_posts():
    """Tạo các bài viết mẫu về Elon Musk"""
    categories = get_dummy_categories()
    tags = get_dummy_tags()
    
    now = datetime.now()
    
    # Nội dung chi tiết cho bài đầu tiên
    spacex_content = """
    <h2>Tầm nhìn của SpaceX</h2>
    <p>SpaceX được thành lập vào năm 2002 với sứ mệnh cách mạng hóa công nghệ không gian và giảm chi phí vận chuyển vào không gian. Elon Musk đã thành lập công ty với tầm nhìn cuối cùng là cho phép con người sống trên các hành tinh khác, đặc biệt là sao Hỏa.</p>
    
    <p>Công ty đã đạt được nhiều cột mốc quan trọng trong những năm qua:</p>
    
    <ul>
        <li>2008: Falcon 1 trở thành tên lửa nhiên liệu lỏng đầu tiên do tư nhân phát triển đạt quỹ đạo Trái đất</li>
        <li>2010: SpaceX trở thành công ty tư nhân đầu tiên phóng tàu vũ trụ lên quỹ đạo và quay trở lại Trái đất</li>
        <li>2012: Tàu Dragon trở thành tàu vũ trụ tư nhân đầu tiên ghép nối với Trạm vũ trụ quốc tế (ISS)</li>
        <li>2015: SpaceX thực hiện thành công việc hạ cánh và thu hồi tầng đầu của tên lửa Falcon 9</li>
        <li>2018: Phóng thành công Falcon Heavy, tên lửa mạnh nhất đang hoạt động trên thế giới</li>
        <li>2020: SpaceX trở thành công ty tư nhân đầu tiên đưa phi hành gia lên ISS</li>
    </ul>
    
    <h2>Starship: Tương lai của du hành liên hành tinh</h2>
    <p>Starship là hệ thống tên lửa thế hệ tiếp theo của SpaceX, được thiết kế để đưa con người lên Mặt trăng, sao Hỏa và xa hơn. Đây là tên lửa lớn nhất và mạnh nhất từng được phát triển, có khả năng tái sử dụng hoàn toàn.</p>
    
    <p>Một số tính năng chính của Starship bao gồm:</p>
    
    <ul>
        <li>Khả năng vận chuyển hơn 100 tấn hàng hóa lên quỹ đạo Trái đất thấp</li>
        <li>Thiết kế hoàn toàn có thể tái sử dụng, giảm đáng kể chi phí phóng</li>
        <li>Sử dụng động cơ Raptor tiên tiến đốt methane lỏng và oxy lỏng</li>
        <li>Khả năng tiếp nhiên liệu trên quỹ đạo cho các nhiệm vụ liên hành tinh</li>
        <li>Có thể đưa tới 100 người vào không gian trong một lần phóng</li>
    </ul>
    
    <h2>Tầm nhìn cho sao Hỏa</h2>
    <p>Elon Musk đã nhiều lần tuyên bố rằng mục tiêu cuối cùng của SpaceX là thiết lập một thuộc địa con người tự lực cánh sinh trên sao Hỏa. Tầm nhìn này nhằm biến loài người thành một loài liên hành tinh và bảo vệ sự tồn tại lâu dài của nền văn minh trước các mối đe dọa tiềm tàng.</p>
    
    <p>Kế hoạch cho sao Hỏa bao gồm:</p>
    
    <ul>
        <li>Xây dựng một đội tàu Starship để vận chuyển người và vật liệu đến sao Hỏa</li>
        <li>Thiết lập cơ sở hạ tầng ban đầu để sản xuất nhiên liệu tên lửa từ tài nguyên sao Hỏa</li>
        <li>Mở rộng dần thành một thành phố tự lực cánh sinh với một triệu người</li>
        <li>Phát triển kiến trúc bền vững cho cuộc sống trên sao Hỏa</li>
    </ul>
    
    <p>Những thách thức cần vượt qua bao gồm phát triển hệ thống hỗ trợ sự sống đáng tin cậy, bảo vệ khỏi bức xạ vũ trụ, và xây dựng một nền kinh tế bền vững trên sao Hỏa.</p>
    
    <p>Mặc dù tham vọng, tầm nhìn này đã truyền cảm hứng cho một thế hệ mới các nhà khoa học, kỹ sư và nhà thám hiểm không gian, đưa loài người vào một kỷ nguyên mới của khám phá không gian.</p>
    """
    
    # Nội dung chi tiết cho bài thứ hai
    tesla_content = """
    <h2>Sứ mệnh của Tesla</h2>
    <p>Tesla, Inc. được thành lập với sứ mệnh thúc đẩy quá trình chuyển đổi thế giới sang năng lượng bền vững. Công ty do Martin Eberhard và Marc Tarpenning thành lập vào năm 2003, với Elon Musk tham gia với tư cách là nhà đầu tư ban đầu và sau đó trở thành CEO.</p>
    
    <p>Sứ mệnh của Tesla không chỉ là sản xuất xe điện, mà còn tạo ra một hệ sinh thái năng lượng sạch hoàn chỉnh. Điều này bao gồm:</p>
    
    <ul>
        <li>Phát triển xe điện tiên tiến, hấp dẫn và giá cả phải chăng</li>
        <li>Mở rộng hệ thống sạc nhanh toàn cầu (Supercharger)</li>
        <li>Sản xuất pin năng lượng mặt trời và hệ thống lưu trữ cho nhà ở và doanh nghiệp</li>
        <li>Cung cấp giải pháp lưu trữ năng lượng quy mô lớn cho các tiện ích</li>
    </ul>
    
    <h2>Công nghệ pin</h2>
    <p>Pin là yếu tố cốt lõi của tất cả các sản phẩm Tesla, từ xe hơi đến hệ thống lưu trữ năng lượng. Công ty đã dẫn đầu trong việc phát triển công nghệ pin tiên tiến, bao gồm:</p>
    
    <p>Tesla liên tục đầu tư vào nghiên cứu và phát triển để cải thiện công nghệ pin của mình. Những tiến bộ gần đây bao gồm:</p>
    
    <ul>
        <li>Pin 4680: Thiết kế pin thế hệ tiếp theo với mật độ năng lượng cao hơn và chi phí thấp hơn</li>
        <li>Cải tiến hóa học pin để tăng tuổi thọ và độ an toàn</li>
        <li>Giảm sử dụng kim loại đất hiếm và vật liệu khó tìm</li>
        <li>Quy trình sản xuất tiên tiến tại các nhà máy Gigafactory</li>
    </ul>
    
    <h2>Tương lai của lưu trữ năng lượng</h2>
    <p>Mặc dù Tesla nổi tiếng với xe điện, nhưng Elon Musk thường nói rằng mảng kinh doanh lưu trữ năng lượng của công ty có thể cuối cùng trở nên lớn hơn hoạt động sản xuất ô tô của nó. Điều này phù hợp với tầm nhìn dài hạn của Tesla về một tương lai năng lượng bền vững.</p>
    
    <p>Các sản phẩm lưu trữ năng lượng của Tesla bao gồm:</p>
    
    <ul>
        <li>Powerwall: Hệ thống lưu trữ năng lượng gia đình tích hợp với pin mặt trời</li>
        <li>Powerpack: Giải pháp lưu trữ năng lượng quy mô thương mại</li>
        <li>Megapack: Hệ thống lưu trữ quy mô tiện ích để ổn định lưới điện</li>
    </ul>
    
    <p>Những hệ thống này đóng vai trò quan trọng trong việc giải quyết tính không liên tục của năng lượng tái tạo như năng lượng mặt trời và gió, cho phép lưu trữ năng lượng khi sản xuất vượt quá nhu cầu và giải phóng năng lượng khi cần.</p>
    
    <p>Các dự án lưu trữ pin quy mô lớn của Tesla đã được triển khai trên toàn cầu, bao gồm:</p>
    
    <ul>
        <li>Hornsdale Power Reserve ở Nam Úc, một trong những hệ thống lưu trữ pin lớn nhất thế giới</li>
        <li>Dự án lưu trữ năng lượng Moss Landing ở California</li>
        <li>Nhiều dự án tiện ích quy mô lớn hỗ trợ lưới điện và tích hợp năng lượng tái tạo</li>
    </ul>
    
    <p>Khi thế giới chuyển đổi sang năng lượng tái tạo, nhu cầu về lưu trữ năng lượng dự kiến sẽ tăng đáng kể, đặt Tesla ở vị thế tốt để dẫn đầu trong lĩnh vực này.</p>
    """
    
    # Nội dung chi tiết cho bài thứ ba
    neuralink_content = """
    <h2>Neuralink: Kết nối não bộ con người với công nghệ</h2>
    <p>Neuralink Corporation là một công ty công nghệ thần kinh do Elon Musk đồng sáng lập vào năm 2016. Công ty đang phát triển các thiết bị cấy ghép có thể tích hợp vào não người để giao tiếp với máy tính và có khả năng nâng cao chức năng não.</p>
    
    <h2>Công nghệ đột phá</h2>
    <p>Neuralink đang phát triển một hệ thống giao diện não-máy tính (BMI) tiên tiến bao gồm:</p>
    
    <ul>
        <li><strong>Sợi điện cực siêu mỏng:</strong> Các sợi linh hoạt có đường kính chỉ vài micron, mỏng hơn nhiều so với các điện cực thông thường, giúp giảm thiểu tổn thương mô não.</li>
        <li><strong>Robot phẫu thuật:</strong> Một robot chính xác cao được thiết kế để cấy ghép các sợi điện cực vào não với độ chính xác cực cao.</li>
        <li><strong>Chip xử lý:</strong> Thiết bị nhỏ gọn được gắn bên ngoài hộp sọ để xử lý và truyền dữ liệu không dây.</li>
        <li><strong>Phần mềm:</strong> Các thuật toán học máy tiên tiến để giải mã tín hiệu não và chuyển đổi chúng thành lệnh điều khiển.</li>
    </ul>
    
    <h2>Ứng dụng y tế</h2>
    <p>Mục tiêu ban đầu của Neuralink là phát triển các ứng dụng y tế để giúp đỡ những người mắc các bệnh thần kinh nghiêm trọng. Một số ứng dụng tiềm năng bao gồm:</p>
    
    <ul>
        <li>Khôi phục khả năng vận động cho người bị liệt</li>
        <li>Khôi phục thị giác cho người khiếm thị</li>
        <li>Khôi phục khả năng giao tiếp cho người mắc các bệnh như ALS</li>
        <li>Điều trị các tình trạng thần kinh như bệnh Parkinson, động kinh và trầm cảm</li>
    </ul>
    
    <p>Neuralink đã thực hiện một số thử nghiệm trên động vật và đang làm việc để bắt đầu thử nghiệm lâm sàng trên người. Công ty đã nhận được sự chấp thuận từ FDA cho các thử nghiệm trên người và đã bắt đầu tuyển dụng cho các thử nghiệm lâm sàng đầu tiên.</p>
    
    <h2>Tầm nhìn dài hạn</h2>
    <p>Ngoài các ứng dụng y tế, Elon Musk đã chia sẻ tầm nhìn dài hạn táo bạo hơn nhiều cho Neuralink:</p>
    
    <ul>
        <li><strong>Cộng sinh với AI:</strong> Tạo ra một "lớp kỹ thuật số" cho não để con người có thể theo kịp sự phát triển của trí tuệ nhân tạo.</li>
        <li><strong>Giao tiếp não với não:</strong> Khả năng truyền ý nghĩ và khái niệm trực tiếp giữa các cá nhân mà không cần ngôn ngữ.</li>
        <li><strong>Mở rộng khả năng nhận thức:</strong> Tăng cường trí nhớ, khả năng xử lý và các chức năng nhận thức khác.</li>
        <li><strong>Tích hợp với thế giới kỹ thuật số:</strong> Tương tác trực tiếp với máy tính, internet và môi trường ảo.</li>
    </ul>
    
    <p>Những tầm nhìn này đặt ra những câu hỏi sâu sắc về bản chất của ý thức và tương lai của loài người. Mặc dù nhiều người xem đây là viễn tưởng xa vời, Musk tin rằng những tiến bộ như vậy có thể trở nên cần thiết để con người tiếp tục phát triển trong kỷ nguyên AI.</p>
    
    <h2>Thách thức và tranh cãi</h2>
    <p>Neuralink phải đối mặt với nhiều thách thức trong hành trình của mình:</p>
    
    <ul>
        <li><strong>Thách thức kỹ thuật:</strong> Phát triển vật liệu điện cực sinh học tương thích lâu dài, thu nhỏ điện tử, và giải mã tín hiệu não phức tạp.</li>
        <li><strong>Quy định và an toàn:</strong> Đáp ứng các tiêu chuẩn nghiêm ngặt của FDA và các cơ quan quản lý khác cho các thiết bị cấy ghép não.</li>
        <li><strong>Vấn đề đạo đức:</strong> Giải quyết các câu hỏi về quyền riêng tư của suy nghĩ, cải thiện con người, và sự tiếp cận bình đẳng với công nghệ.</li>
        <li><strong>Chấp nhận của công chúng:</strong> Vượt qua nỗi sợ hãi và hiểu lầm về công nghệ cấy ghép não.</li>
    </ul>
    
    <p>Các nhà phê bình cũng đặt câu hỏi về tính thực tế của các mốc thời gian mà Musk đưa ra, chỉ ra rằng các công nghệ thần kinh thường phát triển chậm hơn nhiều so với dự đoán.</p>
    
    <p>Dù có những thách thức này, Neuralink vẫn đại diện cho một nỗ lực tham vọng để mở rộng biên giới của tương tác giữa con người và máy móc, với tiềm năng tạo ra những đột phá đáng kể trong cả y học thần kinh và sự hiểu biết của chúng ta về chính bộ não con người.</p>
    """
    
    # Tạo danh sách bài viết
    posts = [
        {
            'id': 1,
            'title': 'Starship: Tương lai của du hành liên hành tinh',
            'slug': 'starship-tuong-lai-cua-du-hanh-lien-hanh-tinh',
            'content': spacex_content,
            'excerpt': 'Tìm hiểu về tàu vũ trụ Starship của SpaceX và cách nó sẽ cách mạng hóa du hành vũ trụ, đưa con người lên sao Hỏa và xa hơn nữa.',
            'category': categories[2],  # Không gian
            'tags': [tags[0], tags[7], tags[8]],  # SpaceX, Tên lửa, Sao Hỏa
            'is_featured': True,
            'created_at': now - timedelta(days=5),
            'updated_at': now - timedelta(days=5),
        },
        {
            'id': 2,
            'title': 'Tesla và tương lai của lưu trữ năng lượng',
            'slug': 'tesla-va-tuong-lai-cua-luu-tru-nang-luong',
            'content': tesla_content,
            'excerpt': 'Cách các sản phẩm lưu trữ năng lượng của Tesla đang định hình tương lai của lưới điện và năng lượng tái tạo.',
            'category': categories[3],  # Năng lượng
            'tags': [tags[1], tags[6]],  # Tesla, Năng lượng mặt trời
            'is_featured': True,
            'created_at': now - timedelta(days=10),
            'updated_at': now - timedelta(days=8),
        },
        {
            'id': 3,
            'title': 'Tương lai của trí tuệ nhân tạo theo Elon Musk',
            'slug': 'tuong-lai-cua-tri-tue-nhan-tao-theo-elon-musk',
            'content': neuralink_content,
            'excerpt': 'Khám phá quan điểm của Elon Musk về sự phát triển của AI và tầm nhìn của ông về tương lai của công nghệ thần kinh.',
            'category': categories[4],  # AI
            'tags': [tags[2], tags[4]],  # Neuralink, Twitter
            'is_featured': True,
            'created_at': now - timedelta(days=15),
            'updated_at': now - timedelta(days=15),
        },
        {
            'id': 4,
            'title': 'Cách Elon Musk điều hành nhiều công ty cùng lúc',
            'slug': 'cach-elon-musk-dieu-hanh-nhieu-cong-ty-cung-luc',
            'excerpt': 'Tìm hiểu về phương pháp quản lý thời gian và triết lý lãnh đạo giúp Elon Musk điều hành Tesla, SpaceX, Neuralink và The Boring Company.',
            'category': categories[1],  # Kinh doanh
            'tags': [tags[0], tags[1], tags[2], tags[9]],  # SpaceX, Tesla, Neuralink, Boring Company
            'is_featured': False,
            'created_at': now - timedelta(days=20),
            'updated_at': now - timedelta(days=20),
        },
        {
            'id': 5,
            'title': 'Mạng lưới vệ tinh Starlink và tương lai của internet toàn cầu',
            'slug': 'mang-luoi-ve-tinh-starlink-va-tuong-lai-cua-internet-toan-cau',
            'excerpt': 'Khám phá cách mạng lưới vệ tinh Starlink của SpaceX đang mang internet tốc độ cao đến những vùng xa xôi nhất trên thế giới.',
            'category': categories[0],  # Công nghệ
            'tags': [tags[0], tags[4]],  # SpaceX, Starlink
            'is_featured': False,
            'created_at': now - timedelta(days=25),
            'updated_at': now - timedelta(days=23),
        },
    ]
    
    return [type('Post', (), post) for post in posts]


def blog_list(request):
    # Lấy dữ liệu mẫu
    posts = get_dummy_posts()
    categories = get_dummy_categories()
    tags = get_dummy_tags()
    
    # Sắp xếp bài viết theo thời gian tạo (mới nhất trước)
    posts = sorted(posts, key=lambda p: p.created_at, reverse=True)
    
    # Lọc theo danh mục nếu có
    category_slug = request.GET.get('category')
    if category_slug:
        posts = [p for p in posts if p.category.slug == category_slug]
    
    # Lọc theo thẻ nếu có
    tag_slug = request.GET.get('tag')
    if tag_slug:
        posts = [p for p in posts if any(t.slug == tag_slug for t in p.tags)]
    
    # Tìm kiếm nếu có
    query = request.GET.get('q')
    if query:
        posts = [p for p in posts if query.lower() in p.title.lower() or query.lower() in p.excerpt.lower()]
    
    # Phân trang
    paginator = Paginator(posts, 4)  # 4 bài viết mỗi trang
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    # Lấy bài viết gần đây
    recent_posts = sorted(get_dummy_posts(), key=lambda p: p.created_at, reverse=True)[:3]
    
    return render(request, 'blog/blog_list.html', {
        'title': 'Elon Musk - Blog',
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'recent_posts': recent_posts
    })

def blog_detail(request, post_id, slug):
    # Lấy dữ liệu mẫu
    all_posts = get_dummy_posts()
    categories = get_dummy_categories()
    tags = get_dummy_tags()
    
    # Tìm bài viết hiện tại
    post = next((p for p in all_posts if p.id == post_id and p.slug == slug), None)
    if not post:
        # Trả về 404 nếu không tìm thấy
        post = all_posts[0]  # Tạm thời lấy bài đầu tiên để demo
    
    # Lấy bài viết trước và sau
    all_posts_sorted = sorted(all_posts, key=lambda p: p.created_at, reverse=True)
    current_index = next((i for i, p in enumerate(all_posts_sorted) if p.id == post.id), -1)
    
    prev_post = all_posts_sorted[current_index + 1] if current_index < len(all_posts_sorted) - 1 else None
    next_post = all_posts_sorted[current_index - 1] if current_index > 0 else None
    
    # Lấy bài viết gần đây
    recent_posts = sorted(all_posts, key=lambda p: p.created_at, reverse=True)[:3]
    
    # Lấy bài viết liên quan (cùng danh mục hoặc cùng thẻ)
    related_posts = [p for p in all_posts if p.id != post.id and 
                     (p.category.id == post.category.id or 
                      any(t1.id == t2.id for t1 in p.tags for t2 in post.tags))]
    related_posts = sorted(related_posts, key=lambda p: p.created_at, reverse=True)[:3]
    
    return render(request, 'blog/blog_detail.html', {
        'title': f'Elon Musk - {post.title}',
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
        'categories': categories,
        'tags': tags,
        'recent_posts': recent_posts,
        'related_posts': related_posts
    })

from bs4 import BeautifulSoup
html_doc = """
div class="reviews__item-user">
            <a href="/users/2145224/" rel="nofollow">
                <div class="reviews__item-user-avatar">
                    <img src="https://image2.yell.ru/imager/MmVhMDQ3MWFjYzc3MDgxYjMwO/080x080/avatar/5/3/1/a_n03qml1bc4n3a5rs_1608829102.jpg" width="60" height="60" alt="" style="opacity: 1; transition: all 0.5s ease 0s;">
                </div>
                <div class="reviews__item-user-name" itemprop="author">Roman Filev</div>
            </a>
"""
soup = BeautifulSoup(html_doc, "lxml")
print(soup.findAll("div", text="Roman Filev"))
# vsco.co ͼƬץȡ����

����scrapy����ʹ��selenium����chrome���ض�̬��ҳ�������������ɵ�HTML�õ���Ҫ��ͼƬ����

## ׼������
- ��װselenium
```bash
pip install selenium
```

- ���ذ�װchromeDriver
selenium����chrome�������Ҫ��chromeDriver����Э����[����chromeDriver������](http://chromedriver.storage.googleapis.com/index.html?path=2.7/)
������ɺ��Ƶ�python����Ŀ¼�µ�Scripts�ļ����У�windows�е�·����`C:\Python27\Scripts`

- ��װpillow��
scrapy�ٷ��ĵ����Ƽ�ʹ��pillow����������ͼ������ͼƬ��һ��ΪJPEG/RGB��ʽ,[pillow](http://pillow.readthedocs.org/en/latest/installation.html)

## ������׼���󣬿�ʼ��д����
- ����ͼƬ�ܵ�
��settings.py�ļ���д��
```python
    ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
    IMAGES_STORE = 'D:\images'  # ϵͳ����Ҫ���ͼƬ���ļ���·��
```

- ��item�ж���image_urls
```python
    image_urls = scrapy.Field()
    images = scrapy.Field()
```

- ץȡͼƬ
��start_request�л�ȡ��ҳ��Ϣ���ֱ����chrome���������ÿһҳ��url��`time.sleep(3)`ʹ����˯��3����Ϊ�˵ȴ�ҳ��JSȫ��������ϣ�
���ץȡ����img��ǩ�����Ӹ�ֵ��item��������ͼƬ�ܵ�������δ���õ�����£�Ĭ��ֻ����ԭͼ�ߴ��ͼƬ

## ��������
```bash
scrapy crawl vsco
```
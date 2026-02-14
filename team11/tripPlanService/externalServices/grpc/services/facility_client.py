"""
Facility Service Client - Fully Mocked with Real Iranian Places
"""

import logging
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)


class FacilityClient:
    """
    Fully mocked client with real places from all Iranian provinces
    Each province has at least 3 samples with real locations
    """

    def __init__(self, base_url: str = 'http://localhost:8000/team4/api', use_mocks: bool = True):
        self.base_url = base_url.rstrip('/')
        self.use_mocks = use_mocks
        logger.info("FacilityClient initialized in FULL MOCK mode with real Iranian places")

        # Initialize all mock data
        self._initialize_mock_data()

    def _initialize_mock_data(self):
        """Initialize comprehensive mock data for all Iranian provinces"""
        self.mock_places = [
            # Tehran Province
            {
                'id': 'place_tehran_001',
                'title': 'برج میلاد',
                'category': 'CULTURAL',
                'province': 'تهران',
                'location': 'تهران',
                'address': 'تهران، بزرگراه همت، برج میلاد',
                'lat': 35.7447, 'lng': 51.3753,
                'entry_fee': 500000,
                'price_tier': 'MODERATE',
                'description': 'برج میلاد تهران، ششمین برج بلند جهان و نماد پایتخت ایران',
                'images': ['https://example.com/milad-tower.jpg'],
                'opening_hours': {'daily': '09:00-23:00'},
                'rating': 4.5, 'review_count': 12500
            },
            {
                'id': 'place_tehran_002',
                'title': 'کاخ گلستان',
                'category': 'HISTORICAL',
                'province': 'تهران',
                'location': 'تهران',
                'address': 'تهران، خیابان پانزده خرداد، کاخ گلستان',
                'lat': 35.6793, 'lng': 51.4213,
                'entry_fee': 200000,
                'price_tier': 'BUDGET',
                'description': 'کاخ سلطنتی دوره قاجار و یکی از آثار ثبت شده یونسکو',
                'images': ['https://example.com/golestan-palace.jpg'],
                'opening_hours': {'daily': '09:00-18:00'},
                'rating': 4.7, 'review_count': 8900
            },
            {
                'id': 'place_tehran_003',
                'title': 'بازار تجریش',
                'category': 'CULTURAL',
                'province': 'تهران',
                'location': 'تهران',
                'address': 'تهران، میدان تجریش، بازار سنتی',
                'lat': 35.8047, 'lng': 51.4331,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'بازار سنتی تجریش با طراوت کوهپایه‌ای',
                'images': ['https://example.com/tajrish-bazaar.jpg'],
                'opening_hours': {'daily': '08:00-22:00'},
                'rating': 4.3, 'review_count': 5600
            },
            {
                'id': 'place_tehran_004',
                'title': 'پارک جمشیدیه',
                'category': 'NATURAL',
                'province': 'تهران',
                'location': 'تهران',
                'address': 'تهران، نیاوران، پارک جمشیدیه',
                'lat': 35.8159, 'lng': 51.4692,
                'entry_fee': 50000,
                'price_tier': 'BUDGET',
                'description': 'پارک کوهستانی زیبا در دامنه البرز',
                'images': ['https://example.com/jamshidieh-park.jpg'],
                'opening_hours': {'daily': '06:00-21:00'},
                'rating': 4.6, 'review_count': 7800
            },
            {
                'id': 'place_tehran_005',
                'title': 'موزه ملی ایران',
                'category': 'CULTURAL',
                'province': 'تهران',
                'location': 'تهران',
                'address': 'تهران، خیابان امام خمینی، موزه ملی ایران',
                'lat': 35.6880, 'lng': 51.4158,
                'entry_fee': 200000,
                'price_tier': 'BUDGET',
                'description': 'موزه باستان‌شناسی با آثار تاریخی ایران',
                'images': ['https://example.com/national-museum.jpg'],
                'opening_hours': {'daily': '09:00-17:00'},
                'rating': 4.7, 'review_count': 9200
            },
            {
                'id': 'place_tehran_006',
                'title': 'رستوران دیزی سنتی',
                'category': 'DINING',
                'province': 'تهران',
                'location': 'تهران',
                'address': 'تهران، خیابان ولیعصر، رستوران دیزی',
                'lat': 35.7200, 'lng': 51.4180,
                'entry_fee': 0,
                'price_tier': 'BUDGET',
                'description': 'رستوران سنتی با دیزی اصیل تهرانی',
                'images': ['https://example.com/dizi-restaurant.jpg'],
                'opening_hours': {'daily': '11:00-22:00'},
                'rating': 4.4, 'review_count': 6500
            },
            {
                'id': 'place_tehran_007',
                'title': 'پارک آب و آتش',
                'category': 'RECREATIONAL',
                'province': 'تهران',
                'location': 'تهران',
                'address': 'تهران، شهرک غرب، پارک آب و آتش',
                'lat': 35.7583, 'lng': 51.3753,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'پارک مدرن با طراحی منحصر به فرد',
                'images': ['https://example.com/ab-o-atash-park.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.5, 'review_count': 8300
            },

            # Isfahan Province
            {
                'id': 'place_isfahan_001',
                'title': 'میدان نقش جهان',
                'category': 'HISTORICAL',
                'province': 'اصفهان',
                'location': 'اصفهان',
                'address': 'اصفهان، میدان امام (نقش جهان)',
                'lat': 32.6579, 'lng': 51.6773,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'دومین میدان بزرگ جهان و میراث جهانی یونسکو',
                'images': ['https://example.com/naghsh-jahan.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.9, 'review_count': 15600
            },
            {
                'id': 'place_isfahan_002',
                'title': 'مسجد شیخ لطف الله',
                'category': 'RELIGIOUS',
                'province': 'اصفهان',
                'location': 'اصفهان',
                'address': 'اصفهان، میدان نقش جهان، ضلع شرقی',
                'lat': 32.6575, 'lng': 51.6782,
                'entry_fee': 500000,
                'price_tier': 'MODERATE',
                'description': 'شاهکار معماری اسلامی دوره صفوی',
                'images': ['https://example.com/sheikh-lotfollah.jpg'],
                'opening_hours': {'daily': '08:00-19:00'},
                'rating': 4.9, 'review_count': 11200
            },
            {
                'id': 'place_isfahan_003',
                'title': 'سی و سه پل',
                'category': 'HISTORICAL',
                'province': 'اصفهان',
                'location': 'اصفهان',
                'address': 'اصفهان، خیابان چهارباغ، روی رودخانه زاینده رود',
                'lat': 32.6474, 'lng': 51.6725,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'پل تاریخی سی و سه پل بر روی زاینده رود',
                'images': ['https://example.com/si-o-se-pol.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.8, 'review_count': 9800
            },
            {
                'id': 'place_isfahan_004',
                'title': 'رستوران شهرزاد',
                'category': 'DINING',
                'province': 'اصفهان',
                'location': 'اصفهان',
                'address': 'اصفهان، چهارباغ عباسی، رستوران شهرزاد',
                'lat': 32.6540, 'lng': 51.6720,
                'entry_fee': 0,
                'price_tier': 'MODERATE',
                'description': 'رستوران سنتی با غذاهای اصیل اصفهانی',
                'images': ['https://example.com/shahrzad-restaurant.jpg'],
                'opening_hours': {'daily': '12:00-23:00'},
                'rating': 4.5, 'review_count': 3400
            },

            # Fars Province
            {
                'id': 'place_fars_001',
                'title': 'تخت جمشید',
                'category': 'HISTORICAL',
                'province': 'فارس',
                'location': 'شیراز',
                'address': 'فارس، مرودشت، تخت جمشید',
                'lat': 29.9357, 'lng': 52.8910,
                'entry_fee': 500000,
                'price_tier': 'MODERATE',
                'description': 'پایتخت باستانی ایران و میراث جهانی یونسکو',
                'images': ['https://example.com/persepolis.jpg'],
                'opening_hours': {'daily': '08:00-17:00'},
                'rating': 5.0, 'review_count': 25000
            },
            {
                'id': 'place_fars_002',
                'title': 'مسجد نصیرالملک',
                'category': 'RELIGIOUS',
                'province': 'فارس',
                'location': 'شیراز',
                'address': 'شیراز، خیابان لطفعلی خان زند، مسجد نصیرالملک',
                'lat': 29.6061, 'lng': 52.5479,
                'entry_fee': 300000,
                'price_tier': 'BUDGET',
                'description': 'مسجد رنگین کمان با شیشه‌های رنگی خیره کننده',
                'images': ['https://example.com/nasir-ol-molk.jpg'],
                'opening_hours': {'daily': '08:00-18:00'},
                'rating': 4.9, 'review_count': 18900
            },
            {
                'id': 'place_fars_003',
                'title': 'باغ ارم',
                'category': 'NATURAL',
                'province': 'فارس',
                'location': 'شیراز',
                'address': 'شیراز، خیابان ارم، باغ ارم',
                'lat': 29.6440, 'lng': 52.5327,
                'entry_fee': 200000,
                'price_tier': 'BUDGET',
                'description': 'باغ تاریخی و موزه پارس با کاخ زیبا',
                'images': ['https://example.com/eram-garden.jpg'],
                'opening_hours': {'daily': '08:00-20:00'},
                'rating': 4.7, 'review_count': 8700
            },
            {
                'id': 'place_fars_004',
                'title': 'هتل زندیه',
                'category': 'STAY',
                'province': 'فارس',
                'location': 'شیراز',
                'address': 'شیراز، خیابان زند، هتل زندیه',
                'lat': 29.6120, 'lng': 52.5364,
                'entry_fee': 4000000,
                'price_tier': 'LUXURY',
                'description': 'هتل پنج ستاره در مرکز شیراز',
                'images': ['https://example.com/zandieh-hotel.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.6, 'review_count': 2100
            },

            # Khorasan Razavi Province
            {
                'id': 'place_khorasan_001',
                'title': 'حرم مطهر امام رضا',
                'category': 'RELIGIOUS',
                'province': 'خراسان رضوی',
                'location': 'مشهد',
                'address': 'مشهد، حرم مطهر امام رضا',
                'lat': 36.2879, 'lng': 59.6157,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'بزرگترین مسجد جهان و قطب زیارتی ایران',
                'images': ['https://example.com/imam-reza-shrine.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 5.0, 'review_count': 45000
            },
            {
                'id': 'place_khorasan_002',
                'title': 'مقبره فردوسی',
                'category': 'CULTURAL',
                'province': 'خراسان رضوی',
                'location': 'توس',
                'address': 'خراسان رضوی، توس، آرامگاه فردوسی',
                'lat': 36.4700, 'lng': 59.5100,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'آرامگاه فردوسی، شاعر بزرگ ایران',
                'images': ['https://example.com/ferdowsi-tomb.jpg'],
                'opening_hours': {'daily': '08:00-20:00'},
                'rating': 4.6, 'review_count': 6700
            },
            {
                'id': 'place_khorasan_003',
                'title': 'پارک کوهسنگی',
                'category': 'NATURAL',
                'province': 'خراسان رضوی',
                'location': 'مشهد',
                'address': 'مشهد، بلوار کوهسنگی، پارک کوهسنگی',
                'lat': 36.3378, 'lng': 59.5342,
                'entry_fee': 50000,
                'price_tier': 'BUDGET',
                'description': 'پارک جنگلی و طبیعی در ارتفاعات مشهد',
                'images': ['https://example.com/koohsangi-park.jpg'],
                'opening_hours': {'daily': '06:00-22:00'},
                'rating': 4.4, 'review_count': 5400
            },
            {
                'id': 'place_khorasan_004',
                'title': 'رستوران سنتی سرای سعدی',
                'category': 'DINING',
                'province': 'خراسان رضوی',
                'location': 'مشهد',
                'address': 'مشهد، بلوار طالقانی، سرای سعدی',
                'lat': 36.2950, 'lng': 59.6050,
                'entry_fee': 0,
                'price_tier': 'MODERATE',
                'description': 'رستوران سنتی با غذاهای محلی خراسان',
                'images': ['https://example.com/saadi-saray.jpg'],
                'opening_hours': {'daily': '11:00-23:30'},
                'rating': 4.5, 'review_count': 4200
            },

            # Yazd Province
            {
                'id': 'place_yazd_001',
                'title': 'شهر تاریخی یزد',
                'category': 'HISTORICAL',
                'province': 'یزد',
                'location': 'یزد',
                'address': 'یزد، بافت تاریخی شهر',
                'lat': 31.8974, 'lng': 54.3569,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'بافت تاریخی خشتی یزد، میراث جهانی یونسکو',
                'images': ['https://example.com/yazd-old-city.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.8, 'review_count': 9600
            },
            {
                'id': 'place_yazd_002',
                'title': 'برج‌های سکوت',
                'category': 'HISTORICAL',
                'province': 'یزد',
                'location': 'یزد',
                'address': 'یزد، صفاییه، دخمه زرتشتیان',
                'lat': 31.9217, 'lng': 54.3642,
                'entry_fee': 150000,
                'price_tier': 'BUDGET',
                'description': 'دخمه‌های زرتشتیان با معماری منحصر به فرد',
                'images': ['https://example.com/towers-of-silence.jpg'],
                'opening_hours': {'daily': '08:00-19:00'},
                'rating': 4.5, 'review_count': 5300
            },
            {
                'id': 'place_yazd_003',
                'title': 'باغ دولت‌آباد',
                'category': 'NATURAL',
                'province': 'یزد',
                'location': 'یزد',
                'address': 'یزد، خیابان مسجد جامع، باغ دولت‌آباد',
                'lat': 31.9050, 'lng': 54.3450,
                'entry_fee': 200000,
                'price_tier': 'BUDGET',
                'description': 'باغ ایرانی با بلندترین بادگیر جهان',
                'images': ['https://example.com/dowlat-abad.jpg'],
                'opening_hours': {'daily': '08:00-20:00'},
                'rating': 4.6, 'review_count': 4800
            },
            {
                'id': 'place_yazd_004',
                'title': 'کافه تراس موزه',
                'category': 'DINING',
                'province': 'یزد',
                'location': 'یزد',
                'address': 'یزد، خیابان امام خمینی، کافه تراس',
                'lat': 31.8970, 'lng': 54.3680,
                'entry_fee': 0,
                'price_tier': 'BUDGET',
                'description': 'کافه سنتی با منظره بام‌های یزد',
                'images': ['https://example.com/terrace-cafe.jpg'],
                'opening_hours': {'daily': '09:00-23:00'},
                'rating': 4.4, 'review_count': 2100
            },

            # Gilan Province
            {
                'id': 'place_gilan_001',
                'title': 'جنگل‌های ابر',
                'category': 'NATURAL',
                'province': 'گیلان',
                'location': 'ماسوله',
                'address': 'گیلان، فومن، جنگل‌های ابر',
                'lat': 37.1575, 'lng': 49.1200,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'جنگل‌های زیبای پوشیده از مه در ارتفاعات گیلان',
                'images': ['https://example.com/abr-forest.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.9, 'review_count': 8900
            },
            {
                'id': 'place_gilan_002',
                'title': 'روستای ماسوله',
                'category': 'CULTURAL',
                'province': 'گیلان',
                'location': 'ماسوله',
                'address': 'گیلان، فومن، روستای پله‌کانی ماسوله',
                'lat': 37.1563, 'lng': 48.9875,
                'entry_fee': 300000,
                'price_tier': 'MODERATE',
                'description': 'روستای پله‌کانی معروف در دل جنگل',
                'images': ['https://example.com/masouleh.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.8, 'review_count': 14500
            },
            {
                'id': 'place_gilan_003',
                'title': 'بازار رشت',
                'category': 'CULTURAL',
                'province': 'گیلان',
                'location': 'رشت',
                'address': 'رشت، خیابان سعدی، بازار بزرگ رشت',
                'lat': 37.2794, 'lng': 49.5828,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'بازار تاریخی رشت با صنایع دستی گیلان',
                'images': ['https://example.com/rasht-bazaar.jpg'],
                'opening_hours': {'daily': '08:00-21:00'},
                'rating': 4.4, 'review_count': 6200
            },
            {
                'id': 'place_gilan_004',
                'title': 'رستوران گیلانی',
                'category': 'DINING',
                'province': 'گیلان',
                'location': 'رشت',
                'address': 'رشت، میدان شهرداری، رستوران غذای گیلکی',
                'lat': 37.2808, 'lng': 49.5890,
                'entry_fee': 0,
                'price_tier': 'MODERATE',
                'description': 'رستوران سنتی با غذاهای محلی گیلان',
                'images': ['https://example.com/gilani-restaurant.jpg'],
                'opening_hours': {'daily': '11:00-23:00'},
                'rating': 4.6, 'review_count': 5100
            },

            # Khuzestan Province
            {
                'id': 'place_khuzestan_001',
                'title': 'شوش تاریخی',
                'category': 'HISTORICAL',
                'province': 'خوزستان',
                'location': 'شوش',
                'address': 'خوزستان، شوش، محوطه باستانی شوش',
                'lat': 32.1942, 'lng': 48.2436,
                'entry_fee': 200000,
                'price_tier': 'BUDGET',
                'description': 'یکی از قدیمی‌ترین شهرهای جهان، میراث یونسکو',
                'images': ['https://example.com/susa.jpg'],
                'opening_hours': {'daily': '08:00-18:00'},
                'rating': 4.7, 'review_count': 4300
            },
            {
                'id': 'place_khuzestan_002',
                'title': 'چغازنبیل',
                'category': 'HISTORICAL',
                'province': 'خوزستان',
                'location': 'شوش',
                'address': 'خوزستان، شوش، زیگورات چغازنبیل',
                'lat': 32.0086, 'lng': 48.5217,
                'entry_fee': 250000,
                'price_tier': 'BUDGET',
                'description': 'زیگورات باستانی عیلامی، میراث جهانی',
                'images': ['https://example.com/choghazanbil.jpg'],
                'opening_hours': {'daily': '08:00-17:00'},
                'rating': 4.8, 'review_count': 3800
            },
            {
                'id': 'place_khuzestan_003',
                'title': 'پل سفید',
                'category': 'CULTURAL',
                'province': 'خوزستان',
                'location': 'اهواز',
                'address': 'اهواز، رودخانه کارون، پل سفید',
                'lat': 31.3203, 'lng': 48.6927,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'پل معروف اهواز بر روی رودخانه کارون',
                'images': ['https://example.com/white-bridge.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.3, 'review_count': 5600
            },
            {
                'id': 'place_khuzestan_004',
                'title': 'هتل نادری',
                'category': 'STAY',
                'province': 'خوزستان',
                'location': 'اهواز',
                'address': 'اهواز، خیابان نادری، هتل نادری',
                'lat': 31.3260, 'lng': 48.6880,
                'entry_fee': 2500000,
                'price_tier': 'MODERATE',
                'description': 'هتل با امکانات عالی در اهواز',
                'images': ['https://example.com/naderi-hotel.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.2, 'review_count': 1800
            },

            # Azarbaijan Sharqi Province
            {
                'id': 'place_azarbaijan_sh_001',
                'title': 'کلیسای سنت استپانوس',
                'category': 'RELIGIOUS',
                'province': 'آذربایجان شرقی',
                'location': 'جلفا',
                'address': 'آذربایجان شرقی، جلفا، کلیسای سنت استپانوس',
                'lat': 38.9569, 'lng': 45.4844,
                'entry_fee': 300000,
                'price_tier': 'BUDGET',
                'description': 'کلیسای ارامنه، میراث جهانی یونسکو',
                'images': ['https://example.com/st-stepanos.jpg'],
                'opening_hours': {'daily': '08:00-18:00'},
                'rating': 4.8, 'review_count': 3400
            },
            {
                'id': 'place_azarbaijan_sh_002',
                'title': 'دریاچه ارومیه',
                'category': 'NATURAL',
                'province': 'آذربایجان شرقی',
                'location': 'تبریز',
                'address': 'آذربایجان شرقی، دریاچه نمک ارومیه',
                'lat': 37.7000, 'lng': 45.3167,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'بزرگترین دریاچه ایران',
                'images': ['https://example.com/urmia-lake.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.2, 'review_count': 6700
            },
            {
                'id': 'place_azarbaijan_sh_003',
                'title': 'بازار تبریز',
                'category': 'CULTURAL',
                'province': 'آذربایجان شرقی',
                'location': 'تبریز',
                'address': 'تبریز، بازار تاریخی تبریز',
                'lat': 38.0792, 'lng': 46.2914,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'قدیمی‌ترین بازار سرپوشیده جهان، میراث یونسکو',
                'images': ['https://example.com/tabriz-bazaar.jpg'],
                'opening_hours': {'daily': '08:00-20:00'},
                'rating': 4.7, 'review_count': 11200
            },
            {
                'id': 'place_azarbaijan_sh_004',
                'title': 'رستوران کوزه',
                'category': 'DINING',
                'province': 'آذربایجان شرقی',
                'location': 'تبریز',
                'address': 'تبریز، خیابان فردوسی، رستوران کوزه',
                'lat': 38.0800, 'lng': 46.2950,
                'entry_fee': 0,
                'price_tier': 'MODERATE',
                'description': 'رستوران سنتی آذری با غذاهای محلی',
                'images': ['https://example.com/koozeh-restaurant.jpg'],
                'opening_hours': {'daily': '12:00-23:00'},
                'rating': 4.5, 'review_count': 3900
            },

            # Mazandaran Province
            {
                'id': 'place_mazandaran_001',
                'title': 'تله‌کابین توچال',
                'category': 'RECREATIONAL',
                'province': 'مازندران',
                'location': 'چالوس',
                'address': 'مازندران، چالوس، تله‌کابین توچال',
                'lat': 35.8392, 'lng': 51.3892,
                'entry_fee': 800000,
                'price_tier': 'EXPENSIVE',
                'description': 'یکی از بلندترین تله‌کابین‌های جهان',
                'images': ['https://example.com/tochal-telecabin.jpg'],
                'opening_hours': {'daily': '08:00-17:00'},
                'rating': 4.7, 'review_count': 8900
            },
            {
                'id': 'place_mazandaran_002',
                'title': 'دریای مازندران',
                'category': 'NATURAL',
                'province': 'مازندران',
                'location': 'نوشهر',
                'address': 'مازندران، نوشهر، ساحل دریای خزر',
                'lat': 36.6464, 'lng': 51.4967,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'سواحل زیبای دریای خزر',
                'images': ['https://example.com/caspian-sea.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.5, 'review_count': 12000
            },
            {
                'id': 'place_mazandaran_003',
                'title': 'قلعه رودخان',
                'category': 'HISTORICAL',
                'province': 'مازندران',
                'location': 'فومن',
                'address': 'مازندران، فومن، قلعه تاریخی رودخان',
                'lat': 37.2400, 'lng': 49.2700,
                'entry_fee': 200000,
                'price_tier': 'BUDGET',
                'description': 'قلعه تاریخی در دل جنگل',
                'images': ['https://example.com/rudkhan-castle.jpg'],
                'opening_hours': {'daily': '08:00-18:00'},
                'rating': 4.8, 'review_count': 7600
            },
            {
                'id': 'place_mazandaran_004',
                'title': 'هتل درین',
                'category': 'STAY',
                'province': 'مازندران',
                'location': 'چالوس',
                'address': 'مازندران، چالوس، جاده چالوس، هتل درین',
                'lat': 36.6550, 'lng': 51.4200,
                'entry_fee': 3500000,
                'price_tier': 'MODERATE',
                'description': 'هتل ساحلی با منظره دریا',
                'images': ['https://example.com/darin-hotel.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.4, 'review_count': 2400
            },

            # Kerman Province
            {
                'id': 'place_kerman_001',
                'title': 'کلوت‌های شهداد',
                'category': 'NATURAL',
                'province': 'کرمان',
                'location': 'شهداد',
                'address': 'کرمان، شهداد، دشت لوت',
                'lat': 30.6300, 'lng': 57.7100,
                'entry_fee': 500000,
                'price_tier': 'MODERATE',
                'description': 'منظره خارق‌العاده کویر لوت، میراث یونسکو',
                'images': ['https://example.com/kaluts.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.9, 'review_count': 5600
            },
            {
                'id': 'place_kerman_001b',
                'title': 'کویر لوت',
                'category': 'NATURAL',
                'province': 'کرمان',
                'location': 'شهداد',
                'address': 'کرمان، شهداد، کویر لوت',
                'lat': 30.5200, 'lng': 58.4800,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'گرم‌ترین نقطه کره زمین و میراث جهانی یونسکو',
                'images': ['https://example.com/dasht-lut.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.8, 'review_count': 4200
            },
            {
                'id': 'place_kerman_001c',
                'title': 'چشمه‌های آبگرم گنو',
                'category': 'NATURAL',
                'province': 'کرمان',
                'location': 'کرمان',
                'address': 'کرمان، روستای گنو، چشمه‌های آبگرم',
                'lat': 30.4300, 'lng': 57.0900,
                'entry_fee': 150000,
                'price_tier': 'BUDGET',
                'description': 'چشمه‌های آبگرم درمانی در کنار کویر',
                'images': ['https://example.com/genu-springs.jpg'],
                'opening_hours': {'daily': '06:00-22:00'},
                'rating': 4.6, 'review_count': 2800
            },
            {
                'id': 'place_kerman_001d',
                'title': 'دریاچه نمک سیرجان',
                'category': 'NATURAL',
                'province': 'کرمان',
                'location': 'سیرجان',
                'address': 'کرمان، سیرجان، دریاچه نمک',
                'lat': 29.4500, 'lng': 55.6800,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'دریاچه نمک زیبا با منظره خیره‌کننده',
                'images': ['https://example.com/sirjan-salt-lake.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.5, 'review_count': 1900
            },
            {
                'id': 'place_kerman_001e',
                'title': 'دره راگه',
                'category': 'NATURAL',
                'province': 'کرمان',
                'location': 'راور',
                'address': 'کرمان، راور، دره راگه',
                'lat': 31.2600, 'lng': 56.8050,
                'entry_fee': 200000,
                'price_tier': 'BUDGET',
                'description': 'دره‌ای زیبا با صخره‌های رنگارنگ',
                'images': ['https://example.com/rageh-valley.jpg'],
                'opening_hours': {'daily': '07:00-19:00'},
                'rating': 4.7, 'review_count': 3100
            },
            {
                'id': 'place_kerman_002',
                'title': 'باغ شاهزاده ماهان',
                'category': 'HISTORICAL',
                'province': 'کرمان',
                'location': 'ماهان',
                'address': 'کرمان، ماهان، باغ شاهزاده',
                'lat': 30.0686, 'lng': 57.2839,
                'entry_fee': 300000,
                'price_tier': 'BUDGET',
                'description': 'باغ ایرانی زیبا در دل کویر',
                'images': ['https://example.com/shahzadeh-garden.jpg'],
                'opening_hours': {'daily': '08:00-20:00'},
                'rating': 4.8, 'review_count': 6800
            },
            {
                'id': 'place_kerman_003',
                'title': 'گنبد جبلیه',
                'category': 'HISTORICAL',
                'province': 'کرمان',
                'location': 'کرمان',
                'address': 'کرمان، میدان مشتاق، گنبد جبلیه',
                'lat': 30.2839, 'lng': 57.0789,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'بنای تاریخی دوره سلجوقی',
                'images': ['https://example.com/gonbad-jabaliye.jpg'],
                'opening_hours': {'daily': '08:00-18:00'},
                'rating': 4.4, 'review_count': 2900
            },
            {
                'id': 'place_kerman_004',
                'title': 'سفره‌خانه سنتی',
                'category': 'DINING',
                'province': 'کرمان',
                'location': 'کرمان',
                'address': 'کرمان، خیابان شهید بهشتی، سفره‌خانه کرمانی',
                'lat': 30.2900, 'lng': 57.0700,
                'entry_fee': 0,
                'price_tier': 'BUDGET',
                'description': 'غذاهای سنتی کرمان',
                'images': ['https://example.com/kermani-sofreh.jpg'],
                'opening_hours': {'daily': '11:30-23:00'},
                'rating': 4.3, 'review_count': 1800
            },

            # Hormozgan Province
            {
                'id': 'place_hormozgan_001',
                'title': 'جزیره قشم',
                'category': 'NATURAL',
                'province': 'هرمزگان',
                'location': 'قشم',
                'address': 'هرمزگان، جزیره قشم',
                'lat': 26.9580, 'lng': 56.2719,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'بزرگترین جزیره ایران با مناظر بکر',
                'images': ['https://example.com/qeshm-island.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.8, 'review_count': 9400
            },
            {
                'id': 'place_hormozgan_002',
                'title': 'دره ستارگان',
                'category': 'NATURAL',
                'province': 'هرمزگان',
                'location': 'قشم',
                'address': 'هرمزگان، قشم، دره ستارگان',
                'lat': 26.8700, 'lng': 55.6100,
                'entry_fee': 200000,
                'price_tier': 'BUDGET',
                'description': 'دره‌ای با سنگ‌های خاص و منظره شگفت‌انگیز',
                'images': ['https://example.com/stars-valley.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.9, 'review_count': 6200
            },
            {
                'id': 'place_hormozgan_003',
                'title': 'بندر عباس',
                'category': 'CULTURAL',
                'province': 'هرمزگان',
                'location': 'بندرعباس',
                'address': 'هرمزگان، بندرعباس، ساحل خلیج فارس',
                'lat': 27.1865, 'lng': 56.2808,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'بندر جنوبی ایران با فرهنگ خاص',
                'images': ['https://example.com/bandar-abbas.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.3, 'review_count': 7100
            },
            {
                'id': 'place_hormozgan_004',
                'title': 'هتل حافظ',
                'category': 'STAY',
                'province': 'هرمزگان',
                'location': 'بندرعباس',
                'address': 'هرمزگان، بندرعباس، خیابان امام خمینی',
                'lat': 27.1900, 'lng': 56.2750,
                'entry_fee': 2000000,
                'price_tier': 'MODERATE',
                'description': 'هتل مدرن در مرکز بندرعباس',
                'images': ['https://example.com/hafez-hotel.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.1, 'review_count': 1600
            },

            # Sistan and Baluchestan Province
            {
                'id': 'place_sistan_001',
                'title': 'کوه تفتان',
                'category': 'NATURAL',
                'province': 'سیستان و بلوچستان',
                'location': 'خاش',
                'address': 'سیستان و بلوچستان، خاش، آتشفشان تفتان',
                'lat': 28.6086, 'lng': 61.1306,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'آتشفشان فعال و قله بلند ایران',
                'images': ['https://example.com/taftan-volcano.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.6, 'review_count': 2800
            },
            {
                'id': 'place_sistan_002',
                'title': 'دریاچه هامون',
                'category': 'NATURAL',
                'province': 'سیستان و بلوچستان',
                'location': 'زابل',
                'address': 'سیستان و بلوچستان، زابل، دریاچه هامون',
                'lat': 31.0000, 'lng': 61.5000,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'دریاچه فصلی زیبا با پرندگان مهاجر',
                'images': ['https://example.com/hamoon-lake.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.4, 'review_count': 3200
            },
            {
                'id': 'place_sistan_003',
                'title': 'بازار زاهدان',
                'category': 'CULTURAL',
                'province': 'سیستان و بلوچستان',
                'location': 'زاهدان',
                'address': 'سیستان و بلوچستان، زاهدان، بازار سنتی',
                'lat': 29.4963, 'lng': 60.8629,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'بازار سنتی با صنایع دستی بلوچی',
                'images': ['https://example.com/zahedan-bazaar.jpg'],
                'opening_hours': {'daily': '08:00-20:00'},
                'rating': 4.2, 'review_count': 2400
            },
            {
                'id': 'place_sistan_004',
                'title': 'رستوران بلوچی',
                'category': 'DINING',
                'province': 'سیستان و بلوچستان',
                'location': 'زاهدان',
                'address': 'سیستان و بلوچستان، زاهدان، خیابان دانشگاه',
                'lat': 29.5000, 'lng': 60.8700,
                'entry_fee': 0,
                'price_tier': 'BUDGET',
                'description': 'غذاهای سنتی بلوچی',
                'images': ['https://example.com/baluchi-restaurant.jpg'],
                'opening_hours': {'daily': '11:00-22:00'},
                'rating': 4.3, 'review_count': 1500
            },

            # Lorestan Province
            {
                'id': 'place_lorestan_001',
                'title': 'آبشار بیشه',
                'category': 'NATURAL',
                'province': 'لرستان',
                'location': 'دورود',
                'address': 'لرستان، دورود، آبشار بیشه',
                'lat': 33.4897, 'lng': 49.0608,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'یکی از زیباترین آبشارهای ایران',
                'images': ['https://example.com/bisheh-waterfall.jpg'],
                'opening_hours': {'daily': '06:00-20:00'},
                'rating': 4.7, 'review_count': 4200
            },
            {
                'id': 'place_lorestan_002',
                'title': 'پل کشکان',
                'category': 'HISTORICAL',
                'province': 'لرستان',
                'location': 'خرم‌آباد',
                'address': 'لرستان، خرم‌آباد، پل تاریخی کشکان',
                'lat': 33.4942, 'lng': 48.3558,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'پل تاریخی دوره ساسانی',
                'images': ['https://example.com/kashkan-bridge.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.5, 'review_count': 3100
            },
            {
                'id': 'place_lorestan_003',
                'title': 'قلعه فلک‌الافلاک',
                'category': 'HISTORICAL',
                'province': 'لرستان',
                'location': 'خرم‌آباد',
                'address': 'لرستان، خرم‌آباد، قلعه فلک‌الافلاک',
                'lat': 33.4877, 'lng': 48.3569,
                'entry_fee': 150000,
                'price_tier': 'BUDGET',
                'description': 'قلعه تاریخی مستحکم خرم‌آباد',
                'images': ['https://example.com/falak-ol-aflak.jpg'],
                'opening_hours': {'daily': '08:00-19:00'},
                'rating': 4.6, 'review_count': 5400
            },
            {
                'id': 'place_lorestan_004',
                'title': 'کافه کوهستان',
                'category': 'DINING',
                'province': 'لرستان',
                'location': 'خرم‌آباد',
                'address': 'لرستان، خرم‌آباد، بلوار آزادگان',
                'lat': 33.4900, 'lng': 48.3600,
                'entry_fee': 0,
                'price_tier': 'BUDGET',
                'description': 'کافه دنج با منظره کوهستانی',
                'images': ['https://example.com/koohestan-cafe.jpg'],
                'opening_hours': {'daily': '09:00-23:00'},
                'rating': 4.3, 'review_count': 1200
            },

            # Bushehr Province
            {
                'id': 'place_bushehr_001',
                'title': 'خانه‌های تاریخی بوشهر',
                'category': 'HISTORICAL',
                'province': 'بوشهر',
                'location': 'بوشهر',
                'address': 'بوشهر، بافت قدیمی شهر',
                'lat': 28.9684, 'lng': 50.8385,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'خانه‌های تاریخی با معماری خلیج فارس',
                'images': ['https://example.com/bushehr-houses.jpg'],
                'opening_hours': {'daily': '08:00-18:00'},
                'rating': 4.4, 'review_count': 2600
            },
            {
                'id': 'place_bushehr_002',
                'title': 'ساحل بوشهر',
                'category': 'NATURAL',
                'province': 'بوشهر',
                'location': 'بوشهر',
                'address': 'بوشهر، خیابان ساحلی',
                'lat': 28.9700, 'lng': 50.8400,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'ساحل زیبای خلیج فارس',
                'images': ['https://example.com/bushehr-beach.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.3, 'review_count': 4800
            },
            {
                'id': 'place_bushehr_003',
                'title': 'موزه خلیج فارس',
                'category': 'CULTURAL',
                'province': 'بوشهر',
                'location': 'بوشهر',
                'address': 'بوشهر، خیابان امام خمینی، موزه خلیج فارس',
                'lat': 28.9650, 'lng': 50.8350,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'موزه دریایی و تاریخ جنوب ایران',
                'images': ['https://example.com/persian-gulf-museum.jpg'],
                'opening_hours': {'daily': '09:00-17:00'},
                'rating': 4.2, 'review_count': 1800
            },
            {
                'id': 'place_bushehr_004',
                'title': 'رستوران دریایی',
                'category': 'DINING',
                'province': 'بوشهر',
                'location': 'بوشهر',
                'address': 'بوشهر، بلوار ساحلی، رستوران غذای دریایی',
                'lat': 28.9720, 'lng': 50.8420,
                'entry_fee': 0,
                'price_tier': 'MODERATE',
                'description': 'رستوران با غذاهای دریایی تازه',
                'images': ['https://example.com/seafood-restaurant.jpg'],
                'opening_hours': {'daily': '11:00-23:00'},
                'rating': 4.5, 'review_count': 3200
            },

            # Zanjan Province
            {
                'id': 'place_zanjan_001',
                'title': 'غار کتله‌خور',
                'category': 'NATURAL',
                'province': 'زنجان',
                'location': 'زنجان',
                'address': 'زنجان، روستای گرماب، غار کتله‌خور',
                'lat': 36.4697, 'lng': 48.3836,
                'entry_fee': 300000,
                'price_tier': 'MODERATE',
                'description': 'غار آهکی زیبا با استالاکتیت‌ها',
                'images': ['https://example.com/katalekhor-cave.jpg'],
                'opening_hours': {'daily': '08:00-18:00'},
                'rating': 4.7, 'review_count': 4500
            },
            {
                'id': 'place_zanjan_002',
                'title': 'سلطانیه',
                'category': 'HISTORICAL',
                'province': 'زنجان',
                'location': 'سلطانیه',
                'address': 'زنجان، سلطانیه، گنبد سلطانیه',
                'lat': 36.4344, 'lng': 48.7975,
                'entry_fee': 400000,
                'price_tier': 'MODERATE',
                'description': 'بزرگترین گنبد آجری جهان، میراث یونسکو',
                'images': ['https://example.com/soltaniyeh.jpg'],
                'opening_hours': {'daily': '08:00-19:00'},
                'rating': 4.8, 'review_count': 6700
            },
            {
                'id': 'place_zanjan_003',
                'title': 'بازار زنجان',
                'category': 'CULTURAL',
                'province': 'زنجان',
                'location': 'زنجان',
                'address': 'زنجان، بازار تاریخی زنجان',
                'lat': 36.6736, 'lng': 48.4787,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'بازار سنتی با صنایع دستی چاقو زنجان',
                'images': ['https://example.com/zanjan-bazaar.jpg'],
                'opening_hours': {'daily': '08:00-20:00'},
                'rating': 4.4, 'review_count': 2900
            },
            {
                'id': 'place_zanjan_004',
                'title': 'هتل زنجان گرند',
                'category': 'STAY',
                'province': 'زنجان',
                'location': 'زنجان',
                'address': 'زنجان، میدان انقلاب، هتل گرند',
                'lat': 36.6750, 'lng': 48.4800,
                'entry_fee': 2500000,
                'price_tier': 'MODERATE',
                'description': 'هتل مدرن در مرکز شهر',
                'images': ['https://example.com/zanjan-grand-hotel.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.2, 'review_count': 1400
            },

            # Semnan Province
            {
                'id': 'place_semnan_001',
                'title': 'کویر مرنجاب',
                'category': 'NATURAL',
                'province': 'سمنان',
                'location': 'آران و بیدگل',
                'address': 'سمنان، آران و بیدگل، کویر مرنجاب',
                'lat': 34.3000, 'lng': 51.7000,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'دریای ماسه‌های طلایی کویر مرکزی',
                'images': ['https://example.com/maranjab-desert.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.9, 'review_count': 5800
            },
            {
                'id': 'place_semnan_002',
                'title': 'کاروانسرای مرنجاب',
                'category': 'HISTORICAL',
                'province': 'سمنان',
                'location': 'آران و بیدگل',
                'address': 'سمنان، کویر مرنجاب، کاروانسرا',
                'lat': 34.2956, 'lng': 51.6789,
                'entry_fee': 200000,
                'price_tier': 'BUDGET',
                'description': 'کاروانسرای صفوی در دل کویر',
                'images': ['https://example.com/maranjab-caravanserai.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.7, 'review_count': 4200
            },
            {
                'id': 'place_semnan_003',
                'title': 'مسجد جامع سمنان',
                'category': 'RELIGIOUS',
                'province': 'سمنان',
                'location': 'سمنان',
                'address': 'سمنان، خیابان امام خمینی، مسجد جامع',
                'lat': 35.5769, 'lng': 53.3953,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'مسجد تاریخی دوره سلجوقی',
                'images': ['https://example.com/semnan-jame-mosque.jpg'],
                'opening_hours': {'daily': '05:00-22:00'},
                'rating': 4.5, 'review_count': 2100
            },
            {
                'id': 'place_semnan_004',
                'title': 'کافه سنتی',
                'category': 'DINING',
                'province': 'سمنان',
                'location': 'سمنان',
                'address': 'سمنان، میدان امام، کافه سنتی',
                'lat': 35.5750, 'lng': 53.3950,
                'entry_fee': 0,
                'price_tier': 'BUDGET',
                'description': 'کافه سنتی با غذاهای محلی',
                'images': ['https://example.com/semnan-traditional-cafe.jpg'],
                'opening_hours': {'daily': '10:00-23:00'},
                'rating': 4.3, 'review_count': 1300
            },

            # Qazvin Province
            {
                'id': 'place_qazvin_001',
                'title': 'قلعه الموت',
                'category': 'HISTORICAL',
                'province': 'قزوین',
                'location': 'الموت',
                'address': 'قزوین، الموت، قلعه حسن صباح',
                'lat': 36.4000, 'lng': 50.6000,
                'entry_fee': 300000,
                'price_tier': 'MODERATE',
                'description': 'قلعه افسانه‌ای حسن صباح',
                'images': ['https://example.com/alamut-castle.jpg'],
                'opening_hours': {'daily': '08:00-18:00'},
                'rating': 4.8, 'review_count': 6100
            },
            {
                'id': 'place_qazvin_002',
                'title': 'چهلستون قزوین',
                'category': 'HISTORICAL',
                'province': 'قزوین',
                'location': 'قزوین',
                'address': 'قزوین، میدان سپه، کاخ چهلستون',
                'lat': 36.2698, 'lng': 50.0041,
                'entry_fee': 200000,
                'price_tier': 'BUDGET',
                'description': 'کاخ صفوی با نقاشی‌های دیواری',
                'images': ['https://example.com/chehelsotun-qazvin.jpg'],
                'opening_hours': {'daily': '09:00-18:00'},
                'rating': 4.5, 'review_count': 3400
            },
            {
                'id': 'place_qazvin_003',
                'title': 'بازار قیصریه',
                'category': 'CULTURAL',
                'province': 'قزوین',
                'location': 'قزوین',
                'address': 'قزوین، بازار قیصریه',
                'lat': 36.2720, 'lng': 50.0050,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'بازار تاریخی دوره صفوی',
                'images': ['https://example.com/qeysarie-bazaar.jpg'],
                'opening_hours': {'daily': '08:00-20:00'},
                'rating': 4.4, 'review_count': 2800
            },
            {
                'id': 'place_qazvin_004',
                'title': 'رستوران بیدستان',
                'category': 'DINING',
                'province': 'قزوین',
                'location': 'قزوین',
                'address': 'قزوین، خیابان سپه، رستوران سنتی',
                'lat': 36.2700, 'lng': 50.0040,
                'entry_fee': 0,
                'price_tier': 'MODERATE',
                'description': 'رستوران سنتی در بنای تاریخی',
                'images': ['https://example.com/bidestan-restaurant.jpg'],
                'opening_hours': {'daily': '12:00-23:00'},
                'rating': 4.6, 'review_count': 2400
            },

            # Qom Province
            {
                'id': 'place_qom_001',
                'title': 'حرم حضرت معصومه',
                'category': 'RELIGIOUS',
                'province': 'قم',
                'location': 'قم',
                'address': 'قم، حرم حضرت معصومه',
                'lat': 34.6416, 'lng': 50.8764,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'حرم مقدس حضرت فاطمه معصومه',
                'images': ['https://example.com/masoumeh-shrine.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.9, 'review_count': 28000
            },
            {
                'id': 'place_qom_002',
                'title': 'مسجد جمکران',
                'category': 'RELIGIOUS',
                'province': 'قم',
                'location': 'قم',
                'address': 'قم، جاده جمکران، مسجد جمکران',
                'lat': 34.6940, 'lng': 50.9314,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'مسجد معروف شیعیان',
                'images': ['https://example.com/jamkaran-mosque.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.7, 'review_count': 15600
            },
            {
                'id': 'place_qom_003',
                'title': 'موزه آستان مقدس',
                'category': 'CULTURAL',
                'province': 'قم',
                'location': 'قم',
                'address': 'قم، حرم حضرت معصومه، موزه',
                'lat': 34.6420, 'lng': 50.8770,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'موزه با آثار تاریخی و هنری',
                'images': ['https://example.com/astan-museum.jpg'],
                'opening_hours': {'daily': '09:00-18:00'},
                'rating': 4.5, 'review_count': 4200
            },
            {
                'id': 'place_qom_004',
                'title': 'هتل الزهرا',
                'category': 'STAY',
                'province': 'قم',
                'location': 'قم',
                'address': 'قم، بلوار شهید صدوقی، هتل الزهرا',
                'lat': 34.6400, 'lng': 50.8800,
                'entry_fee': 1800000,
                'price_tier': 'MODERATE',
                'description': 'هتل در نزدیکی حرم',
                'images': ['https://example.com/alzahra-hotel.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.3, 'review_count': 2100
            },

            # Hamedan Province
            {
                'id': 'place_hamedan_001',
                'title': 'غار علیصدر',
                'category': 'NATURAL',
                'province': 'همدان',
                'location': 'کبودرآهنگ',
                'address': 'همدان، کبودرآهنگ، غار علیصدر',
                'lat': 35.2983, 'lng': 48.3028,
                'entry_fee': 500000,
                'price_tier': 'MODERATE',
                'description': 'بزرگترین غار آبی جهان',
                'images': ['https://example.com/alisadr-cave.jpg'],
                'opening_hours': {'daily': '08:00-18:00'},
                'rating': 4.9, 'review_count': 11200
            },
            {
                'id': 'place_hamedan_002',
                'title': 'آرامگاه بوعلی سینا',
                'category': 'CULTURAL',
                'province': 'همدان',
                'location': 'همدان',
                'address': 'همدان، میدان بوعلی، آرامگاه بوعلی سینا',
                'lat': 34.7992, 'lng': 48.5146,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'آرامگاه دانشمند بزرگ ایرانی',
                'images': ['https://example.com/avicenna-tomb.jpg'],
                'opening_hours': {'daily': '08:00-20:00'},
                'rating': 4.6, 'review_count': 6700
            },
            {
                'id': 'place_hamedan_003',
                'title': 'گنجنامه',
                'category': 'HISTORICAL',
                'province': 'همدان',
                'location': 'همدان',
                'address': 'همدان، آبشار گنجنامه، کتیبه‌های هخامنشی',
                'lat': 34.7597, 'lng': 48.4794,
                'entry_fee': 200000,
                'price_tier': 'BUDGET',
                'description': 'کتیبه‌های هخامنشی و آبشار',
                'images': ['https://example.com/ganjnameh.jpg'],
                'opening_hours': {'daily': '07:00-20:00'},
                'rating': 4.7, 'review_count': 8100
            },
            {
                'id': 'place_hamedan_004',
                'title': 'رستوران حاج محمود',
                'category': 'DINING',
                'province': 'همدان',
                'location': 'همدان',
                'address': 'همدان، خیابان اکباتان، رستوران حاج محمود',
                'lat': 34.8000, 'lng': 48.5150,
                'entry_fee': 0,
                'price_tier': 'BUDGET',
                'description': 'رستوران معروف با کباب همدانی',
                'images': ['https://example.com/haj-mahmoud-restaurant.jpg'],
                'opening_hours': {'daily': '11:00-23:00'},
                'rating': 4.5, 'review_count': 4800
            },

            # Markazi Province
            {
                'id': 'place_markazi_001',
                'title': 'تپه نوش جان',
                'category': 'HISTORICAL',
                'province': 'مرکزی',
                'location': 'ملایر',
                'address': 'مرکزی، ملایر، تپه باستانی نوش جان',
                'lat': 34.2972, 'lng': 48.8239,
                'entry_fee': 150000,
                'price_tier': 'BUDGET',
                'description': 'محوطه باستانی هزاره اول قبل از میلاد',
                'images': ['https://example.com/nushijan-tepe.jpg'],
                'opening_hours': {'daily': '08:00-17:00'},
                'rating': 4.4, 'review_count': 1800
            },
            {
                'id': 'place_markazi_002',
                'title': 'مسجد جامع اراک',
                'category': 'RELIGIOUS',
                'province': 'مرکزی',
                'location': 'اراک',
                'address': 'مرکزی، اراک، مسجد جامع',
                'lat': 34.0917, 'lng': 49.6892,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'مسجد تاریخی قاجار',
                'images': ['https://example.com/arak-jame-mosque.jpg'],
                'opening_hours': {'daily': '05:00-22:00'},
                'rating': 4.3, 'review_count': 2100
            },
            {
                'id': 'place_markazi_003',
                'title': 'پارک جنگلی اراک',
                'category': 'NATURAL',
                'province': 'مرکزی',
                'location': 'اراک',
                'address': 'مرکزی، اراک، پارک جنگلی',
                'lat': 34.1000, 'lng': 49.7000,
                'entry_fee': 50000,
                'price_tier': 'BUDGET',
                'description': 'فضای سبز و تفریحی اراک',
                'images': ['https://example.com/arak-forest-park.jpg'],
                'opening_hours': {'daily': '06:00-21:00'},
                'rating': 4.2, 'review_count': 3400
            },
            {
                'id': 'place_markazi_004',
                'title': 'سفره‌خانه سنتی',
                'category': 'DINING',
                'province': 'مرکزی',
                'location': 'اراک',
                'address': 'مرکزی، اراک، خیابان امام، سفره‌خانه',
                'lat': 34.0950, 'lng': 49.6900,
                'entry_fee': 0,
                'price_tier': 'BUDGET',
                'description': 'غذاهای محلی مرکزی',
                'images': ['https://example.com/markazi-sofreh.jpg'],
                'opening_hours': {'daily': '11:30-23:00'},
                'rating': 4.1, 'review_count': 1600
            },

            # Ilam Province
            {
                'id': 'place_ilam_001',
                'title': 'آبشار زیرآب',
                'category': 'NATURAL',
                'province': 'ایلام',
                'location': 'پلدختر',
                'address': 'ایلام، پلدختر، آبشار زیرآب',
                'lat': 33.1500, 'lng': 47.7200,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'آبشار زیبا در دل جنگل‌های زاگرس',
                'images': ['https://example.com/zirab-waterfall.jpg'],
                'opening_hours': {'daily': '07:00-19:00'},
                'rating': 4.6, 'review_count': 2900
            },
            {
                'id': 'place_ilam_002',
                'title': 'تنگه ورور',
                'category': 'NATURAL',
                'province': 'ایلام',
                'location': 'ایوان',
                'address': 'ایلام، ایوان، دره تنگه ورور',
                'lat': 33.8119, 'lng': 46.3150,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'دره‌ای باریک و زیبا در کوهستان',
                'images': ['https://example.com/tangheh-varor.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.7, 'review_count': 3200
            },
            {
                'id': 'place_ilam_003',
                'title': 'قلعه فلک‌الافلاک ایلام',
                'category': 'HISTORICAL',
                'province': 'ایلام',
                'location': 'ایلام',
                'address': 'ایلام، خیابان شهدا، قلعه',
                'lat': 33.6374, 'lng': 46.4227,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'قلعه تاریخی ساسانی',
                'images': ['https://example.com/ilam-castle.jpg'],
                'opening_hours': {'daily': '08:00-18:00'},
                'rating': 4.4, 'review_count': 1900
            },
            {
                'id': 'place_ilam_004',
                'title': 'کافه کوهستان ایلام',
                'category': 'DINING',
                'province': 'ایلام',
                'location': 'ایلام',
                'address': 'ایلام، بلوار طالقانی، کافه',
                'lat': 33.6400, 'lng': 46.4250,
                'entry_fee': 0,
                'price_tier': 'BUDGET',
                'description': 'کافه با منظره کوهستانی',
                'images': ['https://example.com/ilam-mountain-cafe.jpg'],
                'opening_hours': {'daily': '09:00-23:00'},
                'rating': 4.2, 'review_count': 1100
            },

            # Kohgiluyeh and Boyer-Ahmad Province
            {
                'id': 'place_kohgiluyeh_001',
                'title': 'دریاچه مارگون',
                'category': 'NATURAL',
                'province': 'کهگیلویه و بویراحمد',
                'location': 'سی سخت',
                'address': 'کهگیلویه و بویراحمد، سی سخت، دریاچه مارگون',
                'lat': 30.8000, 'lng': 51.2000,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'یکی از زیباترین دریاچه‌های ایران',
                'images': ['https://example.com/margoon-lake.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.9, 'review_count': 5600
            },
            {
                'id': 'place_kohgiluyeh_002',
                'title': 'آبشار مارگون',
                'category': 'NATURAL',
                'province': 'کهگیلویه و بویراحمد',
                'location': 'سی سخت',
                'address': 'کهگیلویه و بویراحمد، آبشار مارگون',
                'lat': 30.7833, 'lng': 51.2000,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'آبشار پلکانی بلند و زیبا',
                'images': ['https://example.com/margoon-waterfall.jpg'],
                'opening_hours': {'daily': '07:00-19:00'},
                'rating': 4.8, 'review_count': 4900
            },
            {
                'id': 'place_kohgiluyeh_003',
                'title': 'سد تنگ تامرادی',
                'category': 'NATURAL',
                'province': 'کهگیلویه و بویراحمد',
                'location': 'یاسوج',
                'address': 'کهگیلویه و بویراحمد، یاسوج، سد تامرادی',
                'lat': 30.6683, 'lng': 51.5878,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'سد و دریاچه زیبا در یاسوج',
                'images': ['https://example.com/tangtamoradi-dam.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.5, 'review_count': 3100
            },
            {
                'id': 'place_kohgiluyeh_004',
                'title': 'رستوران سنتی قشقایی',
                'category': 'DINING',
                'province': 'کهگیلویه و بویراحمد',
                'location': 'یاسوج',
                'address': 'کهگیلویه و بویراحمد، یاسوج، خیابان امام',
                'lat': 30.6700, 'lng': 51.5900,
                'entry_fee': 0,
                'price_tier': 'BUDGET',
                'description': 'غذاهای محلی لری و قشقایی',
                'images': ['https://example.com/qashqai-restaurant.jpg'],
                'opening_hours': {'daily': '11:00-22:00'},
                'rating': 4.4, 'review_count': 1800
            },

            # Chaharmahal and Bakhtiari Province
            {
                'id': 'place_chaharmahal_001',
                'title': 'کوه و روستای چلگرد',
                'category': 'NATURAL',
                'province': 'چهارمحال و بختیاری',
                'location': 'چلگرد',
                'address': 'چهارمحال و بختیاری، چلگرد',
                'lat': 32.4667, 'lng': 50.1000,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'دشت‌ها و کوهستان‌های سرسبز بختیاری',
                'images': ['https://example.com/chelgerd.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.7, 'review_count': 3400
            },
            {
                'id': 'place_chaharmahal_002',
                'title': 'آبشار آتشگاه',
                'category': 'NATURAL',
                'province': 'چهارمحال و بختیاری',
                'location': 'شهرکرد',
                'address': 'چهارمحال و بختیاری، آبشار آتشگاه',
                'lat': 32.3667, 'lng': 50.8167,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'آبشار زیبا در دل کوهستان',
                'images': ['https://example.com/atashgah-waterfall.jpg'],
                'opening_hours': {'daily': '07:00-19:00'},
                'rating': 4.6, 'review_count': 2800
            },
            {
                'id': 'place_chaharmahal_003',
                'title': 'پل تاریخی شهرکرد',
                'category': 'HISTORICAL',
                'province': 'چهارمحال و بختیاری',
                'location': 'شهرکرد',
                'address': 'چهارمحال و بختیاری، شهرکرد، پل تاریخی',
                'lat': 32.3256, 'lng': 50.8644,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'پل قدیمی بر روی رودخانه',
                'images': ['https://example.com/shahrekord-bridge.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.3, 'review_count': 1600
            },
            {
                'id': 'place_chaharmahal_004',
                'title': 'رستوران کبابی',
                'category': 'DINING',
                'province': 'چهارمحال و بختیاری',
                'location': 'شهرکرد',
                'address': 'چهارمحال و بختیاری، شهرکرد، خیابان کاشانی',
                'lat': 32.3300, 'lng': 50.8650,
                'entry_fee': 0,
                'price_tier': 'BUDGET',
                'description': 'کباب بختیاری و غذاهای محلی',
                'images': ['https://example.com/bakhtiari-kabab.jpg'],
                'opening_hours': {'daily': '11:00-23:00'},
                'rating': 4.4, 'review_count': 2100
            },

            # Kurdistan Province
            {
                'id': 'place_kurdistan_001',
                'title': 'قوری قلعه',
                'category': 'HISTORICAL',
                'province': 'کردستان',
                'location': 'پالنگان',
                'address': 'کردستان، پالنگان، قوری قلعه',
                'lat': 35.9750, 'lng': 45.9917,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'روستای کوهستانی زیبا با خانه‌های پلکانی',
                'images': ['https://example.com/quri-qaleh.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.8, 'review_count': 4200
            },
            {
                'id': 'place_kurdistan_002',
                'title': 'دریاچه زریوار',
                'category': 'NATURAL',
                'province': 'کردستان',
                'location': 'مریوان',
                'address': 'کردستان، مریوان، دریاچه زریوار',
                'lat': 35.5286, 'lng': 46.3697,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'زیباترین دریاچه آب شیرین ایران',
                'images': ['https://example.com/zarivar-lake.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.9, 'review_count': 6700
            },
            {
                'id': 'place_kurdistan_003',
                'title': 'مسجد جامع سنندج',
                'category': 'RELIGIOUS',
                'province': 'کردستان',
                'location': 'سنندج',
                'address': 'کردستان، سنندج، مسجد جامع',
                'lat': 35.3142, 'lng': 47.0059,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'مسجد تاریخی سنندج',
                'images': ['https://example.com/sanandaj-mosque.jpg'],
                'opening_hours': {'daily': '05:00-22:00'},
                'rating': 4.5, 'review_count': 2800
            },
            {
                'id': 'place_kurdistan_004',
                'title': 'رستوران نان کباب',
                'category': 'DINING',
                'province': 'کردستان',
                'location': 'سنندج',
                'address': 'کردستان، سنندج، خیابان پاسداران',
                'lat': 35.3150, 'lng': 47.0070,
                'entry_fee': 0,
                'price_tier': 'BUDGET',
                'description': 'غذاهای کردی اصیل',
                'images': ['https://example.com/kurdish-restaurant.jpg'],
                'opening_hours': {'daily': '11:00-23:00'},
                'rating': 4.6, 'review_count': 3400
            },

            # Kermanshah Province
            {
                'id': 'place_kermanshah_001',
                'title': 'طاق بستان',
                'category': 'HISTORICAL',
                'province': 'کرمانشاه',
                'location': 'کرمانشاه',
                'address': 'کرمانشاه، طاق بستان',
                'lat': 34.3875, 'lng': 47.1353,
                'entry_fee': 300000,
                'price_tier': 'MODERATE',
                'description': 'نقش برجسته‌های ساسانی، میراث یونسکو',
                'images': ['https://example.com/taq-bostan.jpg'],
                'opening_hours': {'daily': '08:00-20:00'},
                'rating': 4.8, 'review_count': 8900
            },
            {
                'id': 'place_kermanshah_002',
                'title': 'بیستون',
                'category': 'HISTORICAL',
                'province': 'کرمانشاه',
                'location': 'بیستون',
                'address': 'کرمانشاه، بیستون، کتیبه داریوش',
                'lat': 34.3931, 'lng': 47.4372,
                'entry_fee': 300000,
                'price_tier': 'MODERATE',
                'description': 'کتیبه هخامنشی داریوش، میراث یونسکو',
                'images': ['https://example.com/bisotun.jpg'],
                'opening_hours': {'daily': '08:00-19:00'},
                'rating': 4.9, 'review_count': 7800
            },
            {
                'id': 'place_kermanshah_003',
                'title': 'پل بی‌بی سیدون',
                'category': 'HISTORICAL',
                'province': 'کرمانشاه',
                'location': 'کرمانشاه',
                'address': 'کرمانشاه، روستای پران، پل بی‌بی سیدون',
                'lat': 34.3833, 'lng': 47.0833,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'پل تاریخی روی رودخانه گاماسیاب',
                'images': ['https://example.com/bibi-seydon-bridge.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.6, 'review_count': 3200
            },
            {
                'id': 'place_kermanshah_004',
                'title': 'هتل پارسیان',
                'category': 'STAY',
                'province': 'کرمانشاه',
                'location': 'کرمانشاه',
                'address': 'کرمانشاه، بلوار شهید بهشتی، هتل پارسیان',
                'lat': 34.3200, 'lng': 47.0700,
                'entry_fee': 2800000,
                'price_tier': 'MODERATE',
                'rating': 4.3, 'review_count': 1900
            },

            # Ardabil Province
            {
                'id': 'place_ardabil_001',
                'title': 'کوه سبلان',
                'category': 'NATURAL',
                'province': 'اردبیل',
                'location': 'سرعین',
                'address': 'اردبیل، سرعین، کوه سبلان',
                'lat': 38.2500, 'lng': 47.8333,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'سومین قله بلند ایران با دریاچه گل',
                'images': ['https://example.com/sabalan.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.9, 'review_count': 6200
            },
            {
                'id': 'place_ardabil_002',
                'title': 'چشمه آبگرم سرعین',
                'category': 'RECREATIONAL',
                'province': 'اردبیل',
                'location': 'سرعین',
                'address': 'اردبیل، سرعین، آبگرم معدنی',
                'lat': 38.1436, 'lng': 48.0714,
                'entry_fee': 300000,
                'price_tier': 'MODERATE',
                'description': 'چشمه آب گرم معدنی درمانی',
                'images': ['https://example.com/sarein-hotspring.jpg'],
                'opening_hours': {'daily': '06:00-23:00'},
                'rating': 4.7, 'review_count': 8900
            },
            {
                'id': 'place_ardabil_003',
                'title': 'مجموعه شیخ صفی‌الدین',
                'category': 'HISTORICAL',
                'province': 'اردبیل',
                'location': 'اردبیل',
                'address': 'اردبیل، میدان شیخ صفی، مجموعه شیخ صفی',
                'lat': 38.2498, 'lng': 48.2930,
                'entry_fee': 200000,
                'price_tier': 'BUDGET',
                'description': 'مجموعه تاریخی صفویه، میراث یونسکو',
                'images': ['https://example.com/sheikh-safi.jpg'],
                'opening_hours': {'daily': '09:00-18:00'},
                'rating': 4.6, 'review_count': 4100
            },
            {
                'id': 'place_ardabil_004',
                'title': 'رستوران سرعین',
                'category': 'DINING',
                'province': 'اردبیل',
                'location': 'سرعین',
                'address': 'اردبیل، سرعین، خیابان اصلی',
                'lat': 38.1450, 'lng': 48.0700,
                'entry_fee': 0,
                'price_tier': 'MODERATE',
                'description': 'غذاهای محلی آذری',
                'images': ['https://example.com/sarein-restaurant.jpg'],
                'opening_hours': {'daily': '11:00-23:00'},
                'rating': 4.4, 'review_count': 2700
            },

            # West Azarbaijan Province
            {
                'id': 'place_azarbaijan_west_001',
                'title': 'کلیسای تاتاووس',
                'category': 'RELIGIOUS',
                'province': 'آذربایجان غربی',
                'location': 'ماکو',
                'address': 'آذربایجان غربی، ماکو، کلیسای سنت تاتاووس',
                'lat': 39.2833, 'lng': 44.4167,
                'entry_fee': 250000,
                'price_tier': 'BUDGET',
                'description': 'کلیسای ارامنه قدیمی، میراث یونسکو',
                'images': ['https://example.com/tatavous-church.jpg'],
                'opening_hours': {'daily': '08:00-18:00'},
                'rating': 4.7, 'review_count': 2900
            },
            {
                'id': 'place_azarbaijan_west_002',
                'title': 'تخت سلیمان',
                'category': 'HISTORICAL',
                'province': 'آذربایجان غربی',
                'location': 'تکاب',
                'address': 'آذربایجان غربی، تکاب، تخت سلیمان',
                'lat': 36.6042, 'lng': 47.2331,
                'entry_fee': 400000,
                'price_tier': 'MODERATE',
                'description': 'محوطه باستانی ساسانی، میراث یونسکو',
                'images': ['https://example.com/takht-soleyman.jpg'],
                'opening_hours': {'daily': '08:00-19:00'},
                'rating': 4.8, 'review_count': 5100
            },
            {
                'id': 'place_azarbaijan_west_003',
                'title': 'کلیسای قره کلیسا',
                'category': 'RELIGIOUS',
                'province': 'آذربایجان غربی',
                'location': 'چالدران',
                'address': 'آذربایجان غربی، چالدران، کلیسای سیاه',
                'lat': 39.0833, 'lng': 44.2667,
                'entry_fee': 300000,
                'price_tier': 'BUDGET',
                'description': 'کلیسای سیاه ارامنه، میراث یونسکو',
                'images': ['https://example.com/qara-kelisa.jpg'],
                'opening_hours': {'daily': '08:00-18:00'},
                'rating': 4.8, 'review_count': 4200
            },
            {
                'id': 'place_azarbaijan_west_004',
                'title': 'هتل کایا',
                'category': 'STAY',
                'province': 'آذربایجان غربی',
                'location': 'ارومیه',
                'address': 'آذربایجان غربی، ارومیه، بلوار ارتش',
                'lat': 37.5500, 'lng': 45.0800,
                'entry_fee': 2200000,
                'price_tier': 'MODERATE',
                'description': 'هتل مدرن در ارومیه',
                'images': ['https://example.com/kaya-hotel.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.2, 'review_count': 1700
            },

            # Golestan Province
            {
                'id': 'place_golestan_001',
                'title': 'پارک ملی گلستان',
                'category': 'NATURAL',
                'province': 'گلستان',
                'location': 'مینودشت',
                'address': 'گلستان، مینودشت، پارک ملی گلستان',
                'lat': 37.3167, 'lng': 55.9167,
                'entry_fee': 500000,
                'price_tier': 'MODERATE',
                'description': 'جنگل‌های هیرکانی، میراث یونسکو',
                'images': ['https://example.com/golestan-national-park.jpg'],
                'opening_hours': {'daily': '07:00-18:00'},
                'rating': 4.8, 'review_count': 5600
            },
            {
                'id': 'place_golestan_002',
                'title': 'کاخ گلستان گرگان',
                'category': 'HISTORICAL',
                'province': 'گلستان',
                'location': 'گرگان',
                'address': 'گلستان، گرگان، کاخ گلستان',
                'lat': 36.8433, 'lng': 54.4439,
                'entry_fee': 150000,
                'price_tier': 'BUDGET',
                'description': 'کاخ تاریخی دوره قاجار',
                'images': ['https://example.com/gorgan-palace.jpg'],
                'opening_hours': {'daily': '09:00-18:00'},
                'rating': 4.5, 'review_count': 3200
            },
            {
                'id': 'place_golestan_003',
                'title': 'ساحل بندر ترکمن',
                'category': 'NATURAL',
                'province': 'گلستان',
                'location': 'بندر ترکمن',
                'address': 'گلستان، بندر ترکمن، ساحل دریای خزر',
                'lat': 36.9000, 'lng': 54.0667,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'ساحل زیبای دریای خزر',
                'images': ['https://example.com/bandar-torkman-beach.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.4, 'review_count': 6100
            },
            {
                'id': 'place_golestan_004',
                'title': 'رستوران ماهی',
                'category': 'DINING',
                'province': 'گلستان',
                'location': 'گرگان',
                'address': 'گلستان، گرگان، بلوار ناهارخوران',
                'lat': 36.8450, 'lng': 54.4450,
                'entry_fee': 0,
                'price_tier': 'MODERATE',
                'description': 'غذاهای دریایی تازه',
                'images': ['https://example.com/fish-restaurant-gorgan.jpg'],
                'opening_hours': {'daily': '11:00-23:00'},
                'rating': 4.5, 'review_count': 3800
            },

            # Alborz Province
            {
                'id': 'place_alborz_001',
                'title': 'دیزین',
                'category': 'RECREATIONAL',
                'province': 'البرز',
                'location': 'کرج',
                'address': 'البرز، کرج، پیست اسکی دیزین',
                'lat': 36.0667, 'lng': 51.3833,
                'entry_fee': 1000000,
                'price_tier': 'EXPENSIVE',
                'description': 'بزرگترین پیست اسکی ایران',
                'images': ['https://example.com/dizin-ski.jpg'],
                'opening_hours': {'daily': '08:00-16:00'},
                'rating': 4.7, 'review_count': 9800
            },
            {
                'id': 'place_alborz_002',
                'title': 'قلعه لمبسر',
                'category': 'HISTORICAL',
                'province': 'البرز',
                'location': 'کرج',
                'address': 'البرز، کرج، قلعه لمبسر',
                'lat': 35.9833, 'lng': 51.0500,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'قلعه تاریخی در کوهستان البرز',
                'images': ['https://example.com/lambesar-castle.jpg'],
                'opening_hours': {'daily': '08:00-18:00'},
                'rating': 4.5, 'review_count': 4200
            },
            {
                'id': 'place_alborz_003',
                'title': 'پارک چیتگر',
                'category': 'NATURAL',
                'province': 'البرز',
                'location': 'کرج',
                'address': 'البرز، کرج، دریاچه چیتگر',
                'lat': 35.7400, 'lng': 51.1100,
                'entry_fee': 50000,
                'price_tier': 'BUDGET',
                'description': 'پارک و دریاچه مصنوعی بزرگ',
                'images': ['https://example.com/chitgar-park.jpg'],
                'opening_hours': {'daily': '06:00-22:00'},
                'rating': 4.4, 'review_count': 8100
            },
            {
                'id': 'place_alborz_004',
                'title': 'رستوران فیلبند',
                'category': 'DINING',
                'province': 'البرز',
                'location': 'کرج',
                'address': 'البرز، کرج، جاده چالوس، رستوران فیلبند',
                'lat': 35.9000, 'lng': 51.2000,
                'entry_fee': 0,
                'price_tier': 'MODERATE',
                'description': 'رستوران روی جاده با منظره کوهستانی',
                'images': ['https://example.com/filband-restaurant.jpg'],
                'opening_hours': {'daily': '11:00-23:00'},
                'rating': 4.5, 'review_count': 4700
            },

            # North Khorasan Province
            {
                'id': 'place_khorasan_north_001',
                'title': 'آبشار زیارت',
                'category': 'NATURAL',
                'province': 'خراسان شمالی',
                'location': 'بجنورد',
                'address': 'خراسان شمالی، بجنورد، آبشار زیارت',
                'lat': 37.4758, 'lng': 57.3267,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'آبشار زیبا در دل جنگل',
                'images': ['https://example.com/ziarat-waterfall.jpg'],
                'opening_hours': {'daily': '07:00-19:00'},
                'rating': 4.6, 'review_count': 3200
            },
            {
                'id': 'place_khorasan_north_002',
                'title': 'کوه بزقوش',
                'category': 'NATURAL',
                'province': 'خراسان شمالی',
                'location': 'شیروان',
                'address': 'خراسان شمالی، شیروان، کوه بزقوش',
                'lat': 37.3833, 'lng': 57.9667,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'قله مناسب کوهنوردی',
                'images': ['https://example.com/bezqush-mountain.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.5, 'review_count': 2100
            },
            {
                'id': 'place_khorasan_north_003',
                'title': 'بازار بجنورد',
                'category': 'CULTURAL',
                'province': 'خراسان شمالی',
                'location': 'بجنورد',
                'address': 'خراسان شمالی، بجنورد، بازار سنتی',
                'lat': 37.4747, 'lng': 57.3233,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'بازار سنتی با صنایع دستی محلی',
                'images': ['https://example.com/bojnurd-bazaar.jpg'],
                'opening_hours': {'daily': '08:00-20:00'},
                'rating': 4.3, 'review_count': 1800
            },
            {
                'id': 'place_khorasan_north_004',
                'title': 'هتل بجنورد',
                'category': 'STAY',
                'province': 'خراسان شمالی',
                'location': 'بجنورد',
                'address': 'خراسان شمالی، بجنورد، خیابان شهید مطهری',
                'lat': 37.4750, 'lng': 57.3250,
                'entry_fee': 1800000,
                'price_tier': 'MODERATE',
                'description': 'هتل مناسب در مرکز شهر',
                'images': ['https://example.com/bojnurd-hotel.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.1, 'review_count': 1200
            },

            # South Khorasan Province
            {
                'id': 'place_khorasan_south_001',
                'title': 'قلعه فورگ',
                'category': 'HISTORICAL',
                'province': 'خراسان جنوبی',
                'location': 'فورگ',
                'address': 'خراسان جنوبی، فورگ، قلعه تاریخی',
                'lat': 33.3667, 'lng': 59.1833,
                'entry_fee': 150000,
                'price_tier': 'BUDGET',
                'description': 'قلعه دژ گلی بزرگ',
                'images': ['https://example.com/forg-castle.jpg'],
                'opening_hours': {'daily': '08:00-18:00'},
                'rating': 4.6, 'review_count': 2400
            },
            {
                'id': 'place_khorasan_south_002',
                'title': 'غار آیینه',
                'category': 'NATURAL',
                'province': 'خراسان جنوبی',
                'location': 'بیرجند',
                'address': 'خراسان جنوبی، بیرجند، غار آیینه',
                'lat': 32.8667, 'lng': 59.2167,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'غار با تزئینات منحصر به فرد',
                'images': ['https://example.com/ayineh-cave.jpg'],
                'opening_hours': {'daily': '08:00-17:00'},
                'rating': 4.5, 'review_count': 1900
            },
            {
                'id': 'place_khorasan_south_003',
                'title': 'باغ اکبریه',
                'category': 'HISTORICAL',
                'province': 'خراسان جنوبی',
                'location': 'بیرجند',
                'address': 'خراسان جنوبی، بیرجند، باغ اکبریه',
                'lat': 32.8700, 'lng': 59.2200,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'باغ تاریخی قاجار',
                'images': ['https://example.com/akbarieh-garden.jpg'],
                'opening_hours': {'daily': '08:00-20:00'},
                'rating': 4.4, 'review_count': 2100
            },
            {
                'id': 'place_khorasan_south_004',
                'title': 'رستوران سنتی',
                'category': 'DINING',
                'province': 'خراسان جنوبی',
                'location': 'بیرجند',
                'address': 'خراسان جنوبی، بیرجند، خیابان معلم',
                'lat': 32.8650, 'lng': 59.2150,
                'entry_fee': 0,
                'price_tier': 'BUDGET',
                'description': 'غذاهای محلی خراسان جنوبی',
                'images': ['https://example.com/birjand-restaurant.jpg'],
                'opening_hours': {'daily': '11:00-22:00'},
                'rating': 4.3, 'review_count': 1400
            },

            # Additional Tehran Province entries
            {
                'id': 'place_tehran_008',
                'title': 'موزه رضا عباسی',
                'category': 'CULTURAL',
                'province': 'تهران',
                'location': 'تهران',
                'address': 'تهران، خیابان شریعتی، موزه رضا عباسی',
                'lat': 35.7310, 'lng': 51.4490,
                'entry_fee': 150000,
                'price_tier': 'BUDGET',
                'description': 'موزه هنرهای اسلامی و ایرانی',
                'images': ['https://example.com/reza-abbasi-museum.jpg'],
                'opening_hours': {'daily': '09:00-17:00'},
                'rating': 4.7, 'review_count': 4200
            },
            {
                'id': 'place_tehran_009',
                'title': 'باغ کتاب',
                'category': 'CULTURAL',
                'province': 'تهران',
                'location': 'تهران',
                'address': 'تهران، عباس آباد، باغ کتاب',
                'lat': 35.7050, 'lng': 51.4360,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'فضای فرهنگی و کتابخانه بزرگ',
                'images': ['https://example.com/bagh-ketab.jpg'],
                'opening_hours': {'daily': '09:00-21:00'},
                'rating': 4.6, 'review_count': 8500
            },
            {
                'id': 'place_tehran_010',
                'title': 'هتل اسپیناس پالاس',
                'category': 'STAY',
                'province': 'تهران',
                'location': 'تهران',
                'address': 'تهران، ولیعصر، هتل اسپیناس',
                'lat': 35.7320, 'lng': 51.4180,
                'entry_fee': 8000000,
                'price_tier': 'LUXURY',
                'description': 'هتل پنج ستاره لوکس',
                'images': ['https://example.com/espinas-palace.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.8, 'review_count': 3200
            },

            # Additional Isfahan Province entries
            {
                'id': 'place_isfahan_005',
                'title': 'کاخ چهل ستون',
                'category': 'HISTORICAL',
                'province': 'اصفهان',
                'location': 'اصفهان',
                'address': 'اصفهان، خیابان چهارباغ، کاخ چهل ستون',
                'lat': 32.6615, 'lng': 51.6770,
                'entry_fee': 300000,
                'price_tier': 'BUDGET',
                'description': 'کاخ صفوی با نقاشی‌های دیواری عالی',
                'images': ['https://example.com/chehel-sotun.jpg'],
                'opening_hours': {'daily': '09:00-18:00'},
                'rating': 4.8, 'review_count': 7100
            },
            {
                'id': 'place_isfahan_006',
                'title': 'هتل عباسی',
                'category': 'STAY',
                'province': 'اصفهان',
                'location': 'اصفهان',
                'address': 'اصفهان، خیابان چهارباغ عباسی، هتل عباسی',
                'lat': 32.6550, 'lng': 51.6740,
                'entry_fee': 6000000,
                'price_tier': 'LUXURY',
                'description': 'هتل تاریخی پنج ستاره در کاروانسرای قدیمی',
                'images': ['https://example.com/abbasi-hotel.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.9, 'review_count': 5600
            },
            {
                'id': 'place_isfahan_007',
                'title': 'باغ چهلستون',
                'category': 'NATURAL',
                'province': 'اصفهان',
                'location': 'اصفهان',
                'address': 'اصفهان، باغ چهلستون',
                'lat': 32.6620, 'lng': 51.6765,
                'entry_fee': 200000,
                'price_tier': 'BUDGET',
                'description': 'باغ ایرانی زیبا با حوض و درختان کهنسال',
                'images': ['https://example.com/chehelsotun-garden.jpg'],
                'opening_hours': {'daily': '08:00-19:00'},
                'rating': 4.7, 'review_count': 6300
            },

            # Additional Fars Province entries
            {
                'id': 'place_fars_005',
                'title': 'آرامگاه حافظ',
                'category': 'CULTURAL',
                'province': 'فارس',
                'location': 'شیراز',
                'address': 'فارس، شیراز، حافظیه',
                'lat': 29.6274, 'lng': 52.5503,
                'entry_fee': 200000,
                'price_tier': 'BUDGET',
                'description': 'آرامگاه شاعر بزرگ ایرانی حافظ',
                'images': ['https://example.com/hafez-tomb.jpg'],
                'opening_hours': {'daily': '08:00-22:00'},
                'rating': 4.9, 'review_count': 16200
            },
            {
                'id': 'place_fars_006',
                'title': 'آرامگاه سعدی',
                'category': 'CULTURAL',
                'province': 'فارس',
                'location': 'شیراز',
                'address': 'فارس، شیراز، سعدیه',
                'lat': 29.6040, 'lng': 52.5790,
                'entry_fee': 150000,
                'price_tier': 'BUDGET',
                'description': 'آرامگاه سعدی شیرازی شاعر بنام ایرانی',
                'images': ['https://example.com/saadi-tomb.jpg'],
                'opening_hours': {'daily': '08:00-21:00'},
                'rating': 4.8, 'review_count': 12400
            },
            {
                'id': 'place_fars_007',
                'title': 'قلعه کریمخانی',
                'category': 'HISTORICAL',
                'province': 'فارس',
                'location': 'شیراز',
                'address': 'فارس، شیراز، میدان شهدا، ارگ کریمخان',
                'lat': 29.6090, 'lng': 52.5436,
                'entry_fee': 250000,
                'price_tier': 'BUDGET',
                'description': 'ارگ کریمخان زند با معماری منحصر به فرد',
                'images': ['https://example.com/karimkhan-citadel.jpg'],
                'opening_hours': {'daily': '08:00-19:00'},
                'rating': 4.6, 'review_count': 8900
            },

            # Additional Khorasan Razavi entries
            {
                'id': 'place_khorasan_005',
                'title': 'بازار رضا',
                'category': 'CULTURAL',
                'province': 'خراسان رضوی',
                'location': 'مشهد',
                'address': 'خراسان رضوی، مشهد، بازار رضا',
                'lat': 36.2870, 'lng': 59.6140,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'بازار سنتی و تاریخی مشهد',
                'images': ['https://example.com/reza-bazaar.jpg'],
                'opening_hours': {'daily': '08:00-22:00'},
                'rating': 4.5, 'review_count': 9200
            },
            {
                'id': 'place_khorasan_006',
                'title': 'هتل درویشی',
                'category': 'STAY',
                'province': 'خراسان رضوی',
                'location': 'مشهد',
                'address': 'خراسان رضوی، مشهد، هتل درویشی',
                'lat': 36.2900, 'lng': 59.6100,
                'entry_fee': 5000000,
                'price_tier': 'LUXURY',
                'description': 'هتل پنج ستاره نزدیک حرم',
                'images': ['https://example.com/darvishi-hotel.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.7, 'review_count': 4100
            },

            # Additional Yazd entries
            {
                'id': 'place_yazd_005',
                'title': 'آتشکده یزد',
                'category': 'RELIGIOUS',
                'province': 'یزد',
                'location': 'یزد',
                'address': 'یزد، آتشکده زرتشتیان',
                'lat': 31.8920, 'lng': 54.3680,
                'entry_fee': 200000,
                'price_tier': 'BUDGET',
                'description': 'آتشکده زرتشتیان با آتش همیشه افروز',
                'images': ['https://example.com/fire-temple.jpg'],
                'opening_hours': {'daily': '08:00-19:00'},
                'rating': 4.7, 'review_count': 7200
            },
            {
                'id': 'place_yazd_006',
                'title': 'مسجد جامع یزد',
                'category': 'RELIGIOUS',
                'province': 'یزد',
                'location': 'یزد',
                'address': 'یزد، میدان امام، مسجد جامع',
                'lat': 31.8978, 'lng': 54.3615,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'مسجد با دو مناره بلند و کاشی‌کاری زیبا',
                'images': ['https://example.com/yazd-jame-mosque.jpg'],
                'opening_hours': {'daily': '08:00-20:00'},
                'rating': 4.8, 'review_count': 5900
            },

            # Additional Gilan entries
            {
                'id': 'place_gilan_005',
                'title': 'دریاچه سقالکسار',
                'category': 'NATURAL',
                'province': 'گیلان',
                'location': 'رشت',
                'address': 'گیلان، رشت، دریاچه سقالکسار',
                'lat': 37.3100, 'lng': 49.5420,
                'entry_fee': 50000,
                'price_tier': 'BUDGET',
                'description': 'دریاچه زیبا با پرندگان مهاجر',
                'images': ['https://example.com/saghalaksar.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.5, 'review_count': 4200
            },
            {
                'id': 'place_gilan_006',
                'title': 'هتل کادوس',
                'category': 'STAY',
                'province': 'گیلان',
                'location': 'رشت',
                'address': 'گیلان، رشت، میدان شهرداری، هتل کادوس',
                'lat': 37.2820, 'lng': 49.5870,
                'entry_fee': 3000000,
                'price_tier': 'MODERATE',
                'description': 'هتل چهار ستاره در مرکز شهر',
                'images': ['https://example.com/kadus-hotel.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.4, 'review_count': 2800
            },

            # Additional Khuzestan entries
            {
                'id': 'place_khuzestan_005',
                'title': 'رستوران سنتی خوزستانی',
                'category': 'DINING',
                'province': 'خوزستان',
                'location': 'اهواز',
                'address': 'خوزستان، اهواز، غذای محلی',
                'lat': 31.3250, 'lng': 48.6900,
                'entry_fee': 0,
                'price_tier': 'BUDGET',
                'description': 'غذاهای سنتی عربی و خوزستانی',
                'images': ['https://example.com/khuzestan-restaurant.jpg'],
                'opening_hours': {'daily': '11:00-23:00'},
                'rating': 4.3, 'review_count': 2100
            },

            # Additional East Azerbaijan entries
            {
                'id': 'place_azarbaijan_sh_005',
                'title': 'کندوان',
                'category': 'NATURAL',
                'province': 'آذربایجان شرقی',
                'location': 'اسکو',
                'address': 'آذربایجان شرقی، اسکو، روستای کندوان',
                'lat': 37.7947, 'lng': 46.2844,
                'entry_fee': 200000,
                'price_tier': 'BUDGET',
                'description': 'روستای صخره‌ای با خانه‌های کندو شکل',
                'images': ['https://example.com/kandovan.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.9, 'review_count': 8700
            },
            {
                'id': 'place_azarbaijan_sh_006',
                'title': 'موزه آذربایجان',
                'category': 'CULTURAL',
                'province': 'آذربایجان شرقی',
                'location': 'تبریز',
                'address': 'آذربایجان شرقی، تبریز، موزه آذربایجان',
                'lat': 38.0750, 'lng': 46.2980,
                'entry_fee': 150000,
                'price_tier': 'BUDGET',
                'description': 'موزه باستان‌شناسی آذربایجان',
                'images': ['https://example.com/azarbaijan-museum.jpg'],
                'opening_hours': {'daily': '09:00-17:00'},
                'rating': 4.4, 'review_count': 2900
            },

            # Additional Mazandaran entries
            {
                'id': 'place_mazandaran_005',
                'title': 'آبشار ویسادار',
                'category': 'NATURAL',
                'province': 'مازندران',
                'location': 'نکا',
                'address': 'مازندران، نکا، آبشار ویسادار',
                'lat': 36.5300, 'lng': 53.2900,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'آبشار زیبا در دل جنگل',
                'images': ['https://example.com/visadar-waterfall.jpg'],
                'opening_hours': {'daily': '07:00-19:00'},
                'rating': 4.7, 'review_count': 5200
            },
            {
                'id': 'place_mazandaran_006',
                'title': 'رستوران ماهی سفید',
                'category': 'DINING',
                'province': 'مازندران',
                'location': 'چالوس',
                'address': 'مازندران، چالوس، رستوران ماهی',
                'lat': 36.6500, 'lng': 51.4250,
                'entry_fee': 0,
                'price_tier': 'MODERATE',
                'description': 'رستوران ماهی تازه دریا',
                'images': ['https://example.com/mahi-sefid.jpg'],
                'opening_hours': {'daily': '11:00-23:00'},
                'rating': 4.6, 'review_count': 4100
            },

            # Additional Kerman entries
            {
                'id': 'place_kerman_005',
                'title': 'موزه هنر معاصر کرمان',
                'category': 'CULTURAL',
                'province': 'کرمان',
                'location': 'کرمان',
                'address': 'کرمان، خیابان شریعتی، موزه هنر',
                'lat': 30.2850, 'lng': 57.0750,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'موزه هنرهای معاصر و سنتی',
                'images': ['https://example.com/kerman-art-museum.jpg'],
                'opening_hours': {'daily': '09:00-17:00'},
                'rating': 4.3, 'review_count': 1400
            },

            # Additional Hormozgan entries
            {
                'id': 'place_hormozgan_005',
                'title': 'جزیره هرمز',
                'category': 'NATURAL',
                'province': 'هرمزگان',
                'location': 'بندرعباس',
                'address': 'هرمزگان، جزیره هرمز',
                'lat': 27.0600, 'lng': 56.4700,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'جزیره رنگین کمانی با خاک‌های رنگی',
                'images': ['https://example.com/hormoz-island.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.8, 'review_count': 6800
            },
            {
                'id': 'place_hormozgan_006',
                'title': 'غار نمکدان',
                'category': 'NATURAL',
                'province': 'هرمزگان',
                'location': 'قشم',
                'address': 'هرمزگان، قشم، غار نمکی',
                'lat': 26.8600, 'lng': 55.9800,
                'entry_fee': 150000,
                'price_tier': 'BUDGET',
                'description': 'بلندترین غار نمکی جهان',
                'images': ['https://example.com/namakdan-cave.jpg'],
                'opening_hours': {'daily': '08:00-18:00'},
                'rating': 4.9, 'review_count': 5400
            },

            # Additional Sistan and Baluchestan entries
            {
                'id': 'place_sistan_005',
                'title': 'کوه خواجه',
                'category': 'HISTORICAL',
                'province': 'سیستان و بلوچستان',
                'location': 'زابل',
                'address': 'سیستان و بلوچستان، زابل، کوه خواجه',
                'lat': 30.9067, 'lng': 61.5783,
                'entry_fee': 150000,
                'price_tier': 'BUDGET',
                'description': 'کوه آتشفشانی با آثار باستانی',
                'images': ['https://example.com/khajeh-mountain.jpg'],
                'opening_hours': {'daily': '08:00-18:00'},
                'rating': 4.5, 'review_count': 2100
            },

            # Additional Lorestan entries
            {
                'id': 'place_lorestan_005',
                'title': 'دریاچه کیو',
                'category': 'NATURAL',
                'province': 'لرستان',
                'location': 'خرم‌آباد',
                'address': 'لرستان، خرم‌آباد، دریاچه کیو',
                'lat': 33.5200, 'lng': 48.3100,
                'entry_fee': 50000,
                'price_tier': 'BUDGET',
                'description': 'دریاچه کوهستانی زیبا',
                'images': ['https://example.com/kiu-lake.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.6, 'review_count': 3800
            },

            # Additional Bushehr entries
            {
                'id': 'place_bushehr_005',
                'title': 'کلیسای حضرت مریم',
                'category': 'RELIGIOUS',
                'province': 'بوشهر',
                'location': 'بوشهر',
                'address': 'بوشهر، کلیسای حضرت مریم',
                'lat': 28.9670, 'lng': 50.8370,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'کلیسای تاریخی ارامنه',
                'images': ['https://example.com/mary-church-bushehr.jpg'],
                'opening_hours': {'daily': '08:00-17:00'},
                'rating': 4.3, 'review_count': 1200
            },

            # Additional Zanjan entries
            {
                'id': 'place_zanjan_005',
                'title': 'آبشار گزو',
                'category': 'NATURAL',
                'province': 'زنجان',
                'location': 'ماهنشان',
                'address': 'زنجان، ماهنشان، آبشار گزو',
                'lat': 36.7800, 'lng': 47.7100,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'آبشار زیبا در کوهستان',
                'images': ['https://example.com/gezo-waterfall.jpg'],
                'opening_hours': {'daily': '07:00-19:00'},
                'rating': 4.6, 'review_count': 2400
            },

            # Additional Semnan entries
            {
                'id': 'place_semnan_005',
                'title': 'دریاچه نمک',
                'category': 'NATURAL',
                'province': 'سمنان',
                'location': 'گرمسار',
                'address': 'سمنان، گرمسار، دریاچه نمک',
                'lat': 34.8400, 'lng': 52.1200,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'دریاچه نمک بزرگ ایران',
                'images': ['https://example.com/namak-lake.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.7, 'review_count': 4600
            },

            # Additional Qazvin entries
            {
                'id': 'place_qazvin_005',
                'title': 'مسجد جامع قزوین',
                'category': 'RELIGIOUS',
                'province': 'قزوین',
                'location': 'قزوین',
                'address': 'قزوین، میدان سعدی، مسجد جامع',
                'lat': 36.2750, 'lng': 50.0030,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'مسجد تاریخی با معماری سلجوقی',
                'images': ['https://example.com/qazvin-jame-mosque.jpg'],
                'opening_hours': {'daily': '05:00-22:00'},
                'rating': 4.5, 'review_count': 2200
            },

            # Additional Qom entries
            {
                'id': 'place_qom_005',
                'title': 'موزه فیض',
                'category': 'CULTURAL',
                'province': 'قم',
                'location': 'قم',
                'address': 'قم، کوچه فیض، خانه تاریخی فیض',
                'lat': 34.6450, 'lng': 50.8750,
                'entry_fee': 50000,
                'price_tier': 'BUDGET',
                'description': 'خانه تاریخی با معماری قاجار',
                'images': ['https://example.com/feiz-museum.jpg'],
                'opening_hours': {'daily': '09:00-17:00'},
                'rating': 4.4, 'review_count': 1800
            },

            # Additional Hamedan entries
            {
                'id': 'place_hamedan_005',
                'title': 'آرامگاه باباطاهر',
                'category': 'CULTURAL',
                'province': 'همدان',
                'location': 'همدان',
                'address': 'همدان، پارک باباطاهر',
                'lat': 34.7920, 'lng': 48.5200,
                'entry_fee': 50000,
                'price_tier': 'BUDGET',
                'description': 'آرامگاه شاعر عارف همدانی',
                'images': ['https://example.com/babataher-tomb.jpg'],
                'opening_hours': {'daily': '08:00-20:00'},
                'rating': 4.6, 'review_count': 5200
            },

            # Additional Markazi entries
            {
                'id': 'place_markazi_005',
                'title': 'موزه باستان‌شناسی اراک',
                'category': 'CULTURAL',
                'province': 'مرکزی',
                'location': 'اراک',
                'address': 'مرکزی، اراک، موزه باستان‌شناسی',
                'lat': 34.0930, 'lng': 49.6880,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'موزه با آثار باستانی منطقه',
                'images': ['https://example.com/arak-museum.jpg'],
                'opening_hours': {'daily': '09:00-17:00'},
                'rating': 4.2, 'review_count': 1200
            },

            # Additional Ilam entries
            {
                'id': 'place_ilam_005',
                'title': 'دریاچه سد سیمره',
                'category': 'NATURAL',
                'province': 'ایلام',
                'location': 'ایلام',
                'address': 'ایلام، دریاچه سیمره',
                'lat': 33.5400, 'lng': 47.0200,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'دریاچه سد با منظره کوهستانی',
                'images': ['https://example.com/simreh-dam.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.5, 'review_count': 2200
            },

            # Additional Kohgiluyeh entries
            {
                'id': 'place_kohgiluyeh_005',
                'title': 'چشمه دیمه',
                'category': 'NATURAL',
                'province': 'کهگیلویه و بویراحمد',
                'location': 'یاسوج',
                'address': 'کهگیلویه و بویراحمد، یاسوج، چشمه دیمه',
                'lat': 30.6500, 'lng': 51.6200,
                'entry_fee': 50000,
                'price_tier': 'BUDGET',
                'description': 'چشمه طبیعی با آب گوارا',
                'images': ['https://example.com/dimeh-spring.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.4, 'review_count': 1900
            },

            # Additional Chaharmahal entries
            {
                'id': 'place_chaharmahal_005',
                'title': 'دریاچه سد زاینده‌رود',
                'category': 'NATURAL',
                'province': 'چهارمحال و بختیاری',
                'location': 'شهرکرد',
                'address': 'چهارمحال و بختیاری، سد زاینده‌رود',
                'lat': 32.4800, 'lng': 50.4500,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'دریاچه سد بزرگ با منظره زیبا',
                'images': ['https://example.com/zayandeh-dam.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.5, 'review_count': 2600
            },

            # Additional Kurdistan entries
            {
                'id': 'place_kurdistan_005',
                'title': 'آبشار نوژیان',
                'category': 'NATURAL',
                'province': 'کردستان',
                'location': 'مریوان',
                'address': 'کردستان، مریوان، آبشار نوژیان',
                'lat': 35.4800, 'lng': 46.4200,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'آبشار زیبا در جنگل',
                'images': ['https://example.com/nojian-waterfall.jpg'],
                'opening_hours': {'daily': '07:00-19:00'},
                'rating': 4.7, 'review_count': 2900
            },

            # Additional Kermanshah entries
            {
                'id': 'place_kermanshah_005',
                'title': 'رستوران سنتی دنج',
                'category': 'DINING',
                'province': 'کرمانشاه',
                'location': 'کرمانشاه',
                'address': 'کرمانشاه، خیابان شریعتی، رستوران سنتی',
                'lat': 34.3150, 'lng': 47.0650,
                'entry_fee': 0,
                'price_tier': 'BUDGET',
                'description': 'غذاهای کرمانشاهی اصیل',
                'images': ['https://example.com/kermanshah-restaurant.jpg'],
                'opening_hours': {'daily': '11:00-23:00'},
                'rating': 4.5, 'review_count': 2800
            },

            # Additional Ardabil entries
            {
                'id': 'place_ardabil_005',
                'title': 'دریاچه شورابیل',
                'category': 'NATURAL',
                'province': 'اردبیل',
                'location': 'اردبیل',
                'address': 'اردبیل، دریاچه شورابیل',
                'lat': 38.2400, 'lng': 48.2850,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'دریاچه زیبا در شهر اردبیل',
                'images': ['https://example.com/shorabil-lake.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.5, 'review_count': 5100
            },

            # Additional West Azerbaijan entries
            {
                'id': 'place_azarbaijan_west_005',
                'title': 'دریاچه قره‌گل',
                'category': 'NATURAL',
                'province': 'آذربایجان غربی',
                'location': 'ماکو',
                'address': 'آذربایجان غربی، ماکو، دریاچه قره‌گل',
                'lat': 39.3200, 'lng': 44.5100,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'دریاچه کوهستانی زیبا',
                'images': ['https://example.com/gharehgol-lake.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.6, 'review_count': 2400
            },

            # Additional Golestan entries
            {
                'id': 'place_golestan_005',
                'title': 'آبشار زیارت',
                'category': 'NATURAL',
                'province': 'گلستان',
                'location': 'گرگان',
                'address': 'گلستان، گرگان، آبشار زیارت',
                'lat': 36.8800, 'lng': 54.5200,
                'entry_fee': 100000,
                'price_tier': 'BUDGET',
                'description': 'آبشار معروف در جنگل',
                'images': ['https://example.com/ziarat-waterfall-golestan.jpg'],
                'opening_hours': {'daily': '07:00-19:00'},
                'rating': 4.7, 'review_count': 4800
            },

            # Additional Alborz entries
            {
                'id': 'place_alborz_005',
                'title': 'سد امیرکبیر',
                'category': 'NATURAL',
                'province': 'البرز',
                'location': 'کرج',
                'address': 'البرز، کرج، سد امیرکبیر',
                'lat': 35.9500, 'lng': 51.1900,
                'entry_fee': 50000,
                'price_tier': 'BUDGET',
                'description': 'دریاچه سد با منظره کوهستانی',
                'images': ['https://example.com/amirkabir-dam.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.6, 'review_count': 6200
            },

            # Additional North Khorasan entries
            {
                'id': 'place_khorasan_north_005',
                'title': 'دریاچه آلاگل',
                'category': 'NATURAL',
                'province': 'خراسان شمالی',
                'location': 'شیروان',
                'address': 'خراسان شمالی، شیروان، دریاچه آلاگل',
                'lat': 37.4200, 'lng': 58.0800,
                'entry_fee': 0,
                'price_tier': 'FREE',
                'description': 'دریاچه با پرندگان مهاجر',
                'images': ['https://example.com/alagol-lake.jpg'],
                'opening_hours': {'24/7': True},
                'rating': 4.4, 'review_count': 1900
            },

            # Additional South Khorasan entries
            {
                'id': 'place_khorasan_south_005',
                'title': 'کاروانسرای عین‌الرشید',
                'category': 'HISTORICAL',
                'province': 'خراسان جنوبی',
                'location': 'بیرجند',
                'address': 'خراسان جنوبی، بیرجند، کاروانسرا',
                'lat': 32.8500, 'lng': 59.1800,
                'entry_fee': 50000,
                'price_tier': 'BUDGET',
                'description': 'کاروانسرای تاریخی صفوی',
                'images': ['https://example.com/eynolrashid.jpg'],
                'opening_hours': {'daily': '08:00-18:00'},
                'rating': 4.3, 'review_count': 1100
            },
        ]

    def search_places(
            self,
            province: str = None,
            city: Optional[str] = None,
            categories: Optional[List[str]] = None,
            budget_level: Optional[str] = None,
            limit: int = 20
    ) -> List[Dict]:
        """
        Search for places based on criteria with filtering support
        """
        logger.info(f"Searching places - Province: {province}, City: {city}, Categories: {categories}, Budget: {budget_level}")

        # Start with all places
        filtered_places = self.mock_places.copy()

        # Filter by province (case-insensitive, partial match)
        if province:
            filtered_places = [
                p for p in filtered_places
                if province.lower() in p['province'].lower()
            ]

        # Filter by city/location (case-insensitive, partial match)
        if city:
            filtered_places = [
                p for p in filtered_places
                if city.lower() in p['location'].lower()
            ]

        # Filter by categories
        if categories:
            temp_places = [
                p for p in filtered_places
                if p['category'] in categories
            ]

            if temp_places:
                filtered_places = temp_places

        # Filter by budget level
        if budget_level:
            budget_map = {
                'ECONOMY': ['FREE', 'BUDGET'],
                'MEDIUM': ['BUDGET', 'MODERATE'],
                'LUXURY': ['MODERATE', 'EXPENSIVE', 'LUXURY'],
                'UNLIMITED': ['FREE', 'BUDGET', 'MODERATE', 'EXPENSIVE', 'LUXURY']
            }
            allowed_tiers = budget_map.get(budget_level, ['MODERATE'])
            filtered_places = [
                p for p in filtered_places
                if p['price_tier'] in allowed_tiers
            ]

        logger.info(f"Found {len(filtered_places)} places after filtering")

        # Return limited results
        return filtered_places[:limit]

    def get_place_by_id(self, place_id: str) -> Optional[Dict]:
        """Get detailed information about a specific place"""
        for place in self.mock_places:
            if place['id'] == place_id:
                return place
        return None

    def check_availability(
            self,
            place_id: str,
            date: str,
            start_time: str,
            end_time: str
    ) -> Dict:
        """Check if a place is available"""
        return {
            'is_available': True,
            'reason': '',
            'suggested_times': []
        }

    def close(self):
        """Close connection (no-op for mock)"""
        logger.info("FacilityClient connection closed")

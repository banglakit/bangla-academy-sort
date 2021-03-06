from bangla_sort import bangla


def test_basic():
    assert sorted(['খোলা', 'খেলা'], key=bangla) == ['খেলা', 'খোলা']
    assert sorted(['ৎ', 'ড়'], key=bangla) == ['ড়', 'ৎ']


def test_large():
    words = ['রাজধানী', 'ঢাকার', 'কুর্মিটোলা', 'জেনারেল', 'হাসপাতালের', 'সামনের', 'বিমানবন্দর', 'সড়কে', 'বাসচাপায়',
             'দুই', 'শিক্ষার্থী', 'নিহত', 'হয়েছে।', 'আহত', 'হয়েছে', '১৩', 'জন।', 'এর', 'মধ্যে', 'একজনের', 'অবস্থা',
             'আশঙ্কাজনক।', 'আজ', 'রোববার', 'দুপুর', 'সাড়ে', '১২টার', 'দিকে', 'এই', 'দুর্ঘটনা', 'ঘটে।', 'পরে',
             'বিক্ষুব্ধ', 'শিক্ষার্থীরা', 'সড়ক', 'অবরোধ', 'করে।', 'এ', 'সময়', 'যানবাহন', 'ভাঙচুরের', 'ঘটনা', 'ঘটে।',
             'নিহত', 'শিক্ষার্থীদের', 'দুজনের', 'নাম', 'জানা', 'গেছে।', 'কুর্মিটোলা', 'জেনারেল', 'হাসপাতালের', 'সহকারী',
             'পরিচালক', 'সগির', 'মিয়া', 'প্রথম', 'আলোকে', 'বলেন,', 'নিহত', 'একজনের', 'নাম', 'আবদুল', 'করিম,', 'সে',
             'শহীদ', 'রমিজ', 'উদ্দিন', 'ক্যান্টনমেন্ট', 'কলেজের', 'দ্বাদশ', 'শ্রেণিতে', 'পড়ত।', 'একই', 'কলেজের', 'আরেক',
             'শিক্ষার্থী', 'দিয়া', 'খানম', 'ওরফে', 'মিম।', 'সে', 'একাদশ', 'শ্রেণির', 'শিক্ষার্থী', 'ছিল।', 'সগির',
             'মিয়া', 'জানান,', 'গুরুতর', 'আহত', 'একজনকে', 'কুর্মিটোলা', 'জেনারেল', 'হাসপাতালে', 'ভর্তি', 'করা',
             'হয়েছে।', 'আহত', 'আরও', '১২', 'জন', 'ওই', 'হাসপাতালে', 'চিকিৎসা', 'নিয়েছে।', 'তবে', 'তারা', 'আশঙ্কামুক্ত।']
    sorted(words, key=bangla)


if __name__ == '__main__':
    test_basic()
    test_large()

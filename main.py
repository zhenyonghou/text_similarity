# -*- coding: utf-8 -*-
import time
from check_text_similarity import TextSimilarity


if __name__ == '__main__':
    textSimilarity = TextSimilarity()

    time.sleep(3)

    t0 = time.time()
    s1 = '公司😥诚招采票代👊玩😱不需要💪自己垫✌资金☝工资每天⑤OO元秒结😒免费咨询+客😌服Ｑ😨Ｑ614💪341👍626 （邀请😉好友+客服😖有额外😌奖励）'
    s2 = '公司😏诚招采票代👏玩😝不需要👈自己垫😝资金😱工资每天⑤OO元秒结✌免费咨询+客😰服Ｑ😚Ｑ614☝341😜626 （邀请😜好友+客服😏有额外😜奖励）'

    score = textSimilarity.calc_similarity(s1, s2, filter_emoji=False, punctuation=True)
    print('相似度：%f' % score)

    s1 = '公司😱诚招采票代😉玩😥不需要😨自己垫👍资金👏工资每天⑤OO元秒结👈免费咨询+客😜服Ｑ😏Ｑ614😉341😳626 （邀请😌好友+客服😖有额外😖奖励）'
    s2 = '公司😏诚招采票代👏玩😝不需要👈自己垫😝资金😱工资每天⑤OO元秒结✌免费咨询+客😰服Ｑ😚Ｑ614☝341😜626 （邀请😜好友+客服😏有额外😜奖励）'

    score = textSimilarity.calc_similarity(s1, s2, filter_emoji=False, punctuation=True)
    print('相似度：%f' % score)

    e = time.time() - t0
    print('耗时:%fs' % e)

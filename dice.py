# randを使うためにインポート
import random


# import pysnooper


# @pysnooper.snoop()
def main():
    # ターミナルから入力した文字を変数sに格納
    s: str = input('ダイスを振るのじゃ：')
    deme_list = s.split('d')

    print(type(deme_list))
    print(deme_list)
    kosu = int(deme_list[0])
    deme = int(deme_list[1])

    kekka = []
    sum = 0
    for i in range(kosu):
        kekka.append(random.randint(1, deme))
        sum += kekka[i]

    print('kekka=', kekka)
    print('合計は', sum)

    # ダイスbotの頭の部分を表示
    # 例：3d6 = [
    print(f'{kosu}d{deme} = (', end='')

    # 最後の一つ以外を繰り返し表示する
    for i in range(len(kekka) - 1):
        print(kekka[i], '+', end='', sep='')

    # 最後の一つを表示
    print(kekka[-1], ') = ', end='', sep='')

    # 合計値を表示
    print(sum)

    print('hogehoge')


'''
    try:
        deme = int(s)
    except ValueError as e:
        print('エラーが発生しました', e)
        print('プログラムを終了します')
        exit()

    # deme面ダイスを振ります
    print(f'1d{deme}の結果→', random.randint(1, deme))
'''

if __name__ == '__main__':
    main()

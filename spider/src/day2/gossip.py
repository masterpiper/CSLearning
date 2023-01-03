import requests

if __name__ == '__main__':
    url = "https://bkimg.cdn.bcebos.com/pic/c83d70cf3bc79f3df8dc58c0a5f7da11728b461083bf?x-bce-process=image/resize,m_lfit,w_536,limit_1"
    img_data = requests.get(url=url).content
    # content: byets data
    # text: strings data
    # json: object data
    with open("./storage/gossp.jpg","wb") as fp:
        fp.write(img_data)